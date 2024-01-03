import requests
import hashlib
import requests

# Mengisi alamat API seerver


url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Menentukan username dan password

username = "tesprogrammer020124C18"
password = "bisacoding-02-01-24"

#mengubah password menjadi md5

password = password.encode()
hash_object = hashlib.md5()
hash_object.update(password)
password = hash_object.hexdigest()

#mengecek username dan password
print(username, password)

# membuat dictionary dari data yang akan di kirim
data = {
    "username": username,
    "password": password,
}

# membuat request untuk POST
response = requests.post(url, data=data)

# mengecek kode response
if response.status_code == 200:
    data = response.json() 
    print("Data yang diunduh:", data)
else:
    print("Gagal mengunduh data. Kode status:", response.status_code)
    print("Pesan respons:", response.text)
    print("response header adalah:", response.headers)
    print ("response cookies adalah", response.cookies)
    





