from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from jose import JWTError, jwt

import crud, models, schemas, auth
from database import SessionLocal, engine

# Buat tabel database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- SETUP CORS (Frontend React izin masuk) ---
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DEPENDENCY DATABASE ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- DEPENDENCY AUTH (Polisi Token) ---
# Ini fungsi KUNCI: Dia akan membaca token, mendekode, dan mencari siapa pemiliknya
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token tidak valid atau kadaluarsa",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Dekode Token
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Cari user di database
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# ================= ENDPOINTS =================

@app.get("/")
def read_root():
    return {"message": "Server Task Manager Berjalan! 🚀"}

# 1. DAFTAR USER BARU
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email sudah terdaftar")
    return crud.create_user(db=db, user=user)

# 2. LOGIN (Dapat Token)
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not crud.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username atau Password salah",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# 3. GET TUGAS SAYA (Butuh Login)
@app.get("/me/tasks", response_model=List[schemas.Task])
def read_own_tasks(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Ambil tugas yang user_id nya sama dengan user yang sedang login
    return crud.get_tasks(db, user_id=current_user.id)

# 4. BUAT TUGAS BARU (Butuh Login)
@app.post("/me/tasks", response_model=schemas.Task)
def create_own_task(task: schemas.TaskCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Otomatis tempelkan ID user yang sedang login ke tugas baru
    return crud.create_user_task(db=db, task=task, user_id=current_user.id)