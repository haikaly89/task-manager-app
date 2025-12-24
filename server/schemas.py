from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS UNTUK TASK ---

# Bentuk dasar task (data yang pasti ada)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

# Saat user MEMBUAT task, mereka hanya perlu kirim data dasar
class TaskCreate(TaskBase):
    pass

# Saat sistem MENGEMBALIKAN data task ke user (Read), kita kasih ID dan Statusnya
class Task(TaskBase):
    id: int
    status: str
    user_id: int

    class Config:
        from_attributes = True  # Supaya Pydantic bisa baca data dari SQLAlchemy

# --- SCHEMAS UNTUK USER ---

class UserBase(BaseModel):
    username: str
    email: str

# Saat daftar (Register), user WAJIB kirim password
class UserCreate(UserBase):
    password: str

# Saat user melihat profil (Response), JANGAN tampilkan password!
class User(UserBase):
    id: int
    tasks: List[Task] = [] # Tampilkan juga daftar tugasnya

    class Config:
        from_attributes = True