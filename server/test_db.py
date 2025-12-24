from database import engine
from sqlalchemy import text

try:
    # Coba bikin koneksi
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'Halo Database!'"))
        print(result.scalar())
        print("✅ KONEKSI SUKSES!")
except Exception as e:
    print("❌ KONEKSI GAGAL:", e)