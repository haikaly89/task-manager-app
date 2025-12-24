from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas

# 1. Setup Hashing Password
# Ini alat untuk mengacak password. Kita pakai algoritma "bcrypt".
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# --- LOGIKA USER ---

# Mencari user berdasarkan ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Mencari user berdasarkan Email (Penting untuk cek login/registrasi agar tidak dobel)
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Membuat User Baru (Register)
def create_user(db: Session, user: schemas.UserCreate):
    # Langkah 1: Acak password user
    hashed_password = get_password_hash(user.password)
    
    # Langkah 2: Buat object User baru dari model
    db_user = models.User(
        username=user.username, 
        email=user.email, 
        hashed_password=hashed_password
    )
    
    # Langkah 3: Masukkan ke database
    db.add(db_user)
    db.commit()      # Simpan permanen
    db.refresh(db_user) # Ambil data terbaru (termasuk ID yang baru dibuat)
    return db_user

# --- LOGIKA TASK ---

# Mengambil daftar tugas
# skip & limit digunakan untuk pagination (halaman 1, 2, dst)
def get_tasks(db: Session, skip: int = 0, limit: int = 100, user_id: int = None):
    # Jika ada user_id, ambil tugas milik user itu saja
    if user_id:
        return db.query(models.Task).filter(models.Task.user_id == user_id).offset(skip).limit(limit).all()
    # Jika tidak (Admin), ambil semua
    return db.query(models.Task).offset(skip).limit(limit).all()

# Membuat Tugas Baru
def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    # Buat object Task, dan tempelkan ID pemiliknya
    db_task = models.Task(**task.dict(), user_id=user_id)
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task