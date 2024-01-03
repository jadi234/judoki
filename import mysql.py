import json
import mysql.connector

# Buka file data JSON
with open("unduhan.json", "r") as f:
    data = json.load(f)

data = data["data"]
print(data)

# Buat koneksi ke MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tab123",
    database="tokoku"  # Pilih database
)

# Buat cursor
cursor = db.cursor()

tables = ["produk", "status", "kategori"]

for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table};")
    print(f"Tabel {table} telah dihapus.")

# Membuat skema tabel (jika belum ada)
cursor.execute('''
CREATE TABLE IF NOT EXISTS kategori (
    id_kategori INTEGER PRIMARY KEY AUTO_INCREMENT,
    nama_kategori TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS status (
    id_status INTEGER PRIMARY KEY AUTO_INCREMENT,
    nama_status TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS produk (
    id_produk INTEGER PRIMARY KEY AUTO_INCREMENT,
    nama_produk TEXT,
    harga INTEGER,
    kategori_id INTEGER NOT NULL,
    status_id INTEGER,
    FOREIGN KEY(kategori_id) REFERENCES kategori(id_kategori),
    FOREIGN KEY(status_id) REFERENCES status(id_status)
)
''')

kategori_ids = {}
status_ids = {}

for item in data:
    kategori = item['kategori']
    status = item['status']

    if kategori not in kategori_ids:
        cursor.execute("INSERT INTO kategori (nama_kategori) VALUES (%s)", (kategori,))
        kategori_ids[kategori] = cursor.lastrowid

    if status not in status_ids:
        cursor.execute("INSERT INTO status (nama_status) VALUES (%s)", (status,))
        status_ids[status] = cursor.lastrowid

# Memasukkan data ke tabel Produk
for item in data:
    cursor.execute("INSERT INTO produk (id_produk, nama_produk, harga, kategori_id, status_id) VALUES (%s, %s, %s, %s, %s)",
                   (item['id_produk'], item['nama_produk'], item['harga'], kategori_ids[item['kategori']], status_ids[item['status']]))
    
print("selesai")

# Menyimpan perubahan
db.commit()

# Menutup koneksi
db.close()