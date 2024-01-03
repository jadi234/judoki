import requests
import hashlib

# Informasi kredensial
username = "tesprogrammer311223C21"
password = "bisacoding-30-12-23"
password_md5 = hashlib.md5(password_string.encode()).hexdigest()

# URL API
api_url = "https://example.com/api/data"

# Kredensial otentikasi
auth = (username, password_md5)

# Data yang akan dikirim
data_to_send = {
    "key1": "value1",
    "key2": "value2"
}

try:
    # Permintaan POST ke API dengan otentikasi
    response = requests.post(api_url, auth=auth, data=data_to_send)

    # Cek respons
    print("Kode status respons:", response.status_code)
    print("Isi respons:", response.text)

    # Cek header
    headers = response.headers
    print("Headers respons:", headers)

    # Cek cookies
    cookies = response.cookies
    print("Cookies respons:", cookies)

    if response.status_code == 200:
        data = response.json()  # Menangani respons JSON (contoh)
        print("Data yang diunduh:", data)
    else:
        print("Gagal mengunduh data. Kode status:", response.status_code)
        print("Pesan respons:", response.text)

except Exception as e:
    print("Terjadi kesalahan:", str(e))