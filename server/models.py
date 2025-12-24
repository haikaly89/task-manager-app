from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

# 1. Model User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    
    # Relasi: Satu User bisa punya banyak Task
    # 'tasks' ini akan berisi daftar tugas milik user tersebut
    tasks = relationship("Task", back_populates="owner")

# 2. Model Task
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text, nullable=True)
    status = Column(String(20), default="todo") # Opsional: Bisa pakai Boolean juga
    user_id = Column(Integer, ForeignKey("users.id")) # Kunci Tamu (Foreign Key)

    # Relasi: Setiap Task punya satu pemilik (owner)
    owner = relationship("User", back_populates="tasks")