from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. URL Koneksi Database
# Format: mysql+pymysql://username:password@host:port/nama_database
# Karena XAMPP default user 'root' dan tanpa password, bagian password kita kosongkan.
URL_DATABASE = "mysql+pymysql://root:@localhost:3306/task_manager"

# 2. Membuat Engine (Mesin Penggerak)
engine = create_engine(URL_DATABASE)

# 3. Membuat SessionLocal (Pabrik Sesi)
# Setiap kali kita mau akses data (CRUD), kita akan buat sesi dari sini.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base Model
# Semua tabel (User, Task) nanti akan mewarisi class ini.
Base = declarative_base()

# 5. Dependency (Fungsi Pembantu)
# Fungsi ini akan dipanggil oleh FastAPI setiap ada request yang butuh database.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()