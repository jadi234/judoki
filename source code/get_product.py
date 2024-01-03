import requests
import hashlib
import requests
import json
# URL API
url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Menentukan username dan password

username = "tesprogrammer020124C18"
password = "bisacoding-02-01-24"

#mengubah password menjadi md5

password = password.encode()
hash_object = hashlib.md5()
hash_object.update(password)
password = hash_object.hexdigest()

# Buat data username dan password 
data = {
    "username": username,
    "password": password,
}

# membuat request untuk ambil data
response = requests.post(url, data=data)


# Cek status kode
if response.status_code == 200:

    # Data JSON
    unduhan = response.json()

    # Simpan data JSON ke file
    with open("unduhan.json", "w") as f:
        json.dump(unduhan, f)
        print("data berhasil diunduh")

else:

    print(f"Status kode: {response.status_code}")