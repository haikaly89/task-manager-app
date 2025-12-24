from datetime import datetime, timedelta
from jose import jwt
from typing import Optional

# KUNCI RAHASIA (Di aplikasi nyata, ini harus sangat rahasia & acak!)
SECRET_KEY = "kunci_rahasia_super_aman_task_manager"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token berlaku 30 menit

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    
    # Tentukan kapan token kadaluarsa
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    
    # Buat Token (String panjang yang sudah di-enkripsi)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt