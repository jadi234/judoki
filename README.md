folder terdiri dari 2 folder, folder dashboard dan folder source code

folder source code ini terdiri dari 3 file yang terdiri dari :

1. get product : file untuk akses api server
2. import mysql : untuk mengunduh database dari api server
3. import requests : untuk memasukkan databasenya kedalam database mysql (sebelum jalankan file ini,  buat database dengan nama tokoku terlebih dahulu, dan sesuaikan username password databasenya dengan yang ada pada server)

bila data sudah diunduh dan dimasukkan kedalam database mysql, maka tinggal jalankan dashboardnya pada folder dash board yang terdiri dari folder template dan file app

1. folder template ini berisikan 3 file html yang digunakan untuk memberikan 3 tampilan halaman yaitu halaman utama, halaman edit produk dan halaman tambah produk. Data yang ditampilkan hanya data yang bisa dijual dan pada fitur hapus dan edit produk akan memberikan peringatan sebelum dipilih. 

2. File app ini adalah file utama yang digunakan untuk menjalankan aplikasi, untuk menjalankanya kita dapat membuka cmd lalu masuk ke directory dimana file ini berada lalu tinggal memasukkan perintah python app.py. Maka nanti akan mendapat alamat servernya yang muncul pada console semisal :

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat

Selanjutnya  fokus pada baris ke 5 yang berisikan * Running on "http://127.0.0.1:5000", blok dan copy alamatnya, lalu paste pada browser seperti  alamatnya yaitu : http://127.0.0.1:5000, maka halaman akan terbuka 


