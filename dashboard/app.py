from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Fungsi untuk koneksi ke database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tab123",
        database="tokoku"
    )

@app.route('/')
def index():
    try:
        db = connect_db()
        cursor = db.cursor()
        query = """
        SELECT p.id_produk, p.nama_produk, p.harga, k.nama_kategori, s.nama_status
        FROM produk p
        JOIN kategori k ON p.kategori_id = k.id_kategori
        JOIN status s ON p.status_id = s.id_status
        WHERE s.nama_status = 'bisa dijual'
        """
        cursor.execute(query)
        produk = cursor.fetchall()
        db.close()
        return render_template('simple_template.html', produk=produk)
    except Exception as e:
        return f"Error: {e}"


@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        nama_produk = request.form.get('nama_produk')
        harga = request.form.get('harga')
        kategori_id = request.form.get('kategori_id')
        status_id = request.form.get('status_id')  # Tambahkan ini

        if not nama_produk or not harga.isdigit() or not kategori_id or not status_id:
            return "Semua field harus diisi."

        try:
            db = connect_db()
            cursor = db.cursor()
            query = "INSERT INTO produk (nama_produk, harga, kategori_id, status_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nama_produk, harga, kategori_id, status_id))
            db.commit()
            db.close()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {e}"

    return render_template('add_product.html')
        

    return render_template('add_product.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])

def edit_product(id):
    if request.method == 'GET':
        try:
            db = connect_db()
            cursor = db.cursor()
            query = "SELECT id_produk, nama_produk, harga FROM produk WHERE id_produk = %s"
            cursor.execute(query, (id,))
            produk = cursor.fetchone()
            db.close()
            return render_template('edit_product.html', produk=produk)
        except Exception as e:
            return f"Error: {e}"

    if request.method == 'POST':
        nama_produk = request.form.get('nama_produk')
        harga = request.form.get('harga')

        if not nama_produk or not harga.isdigit():
            return "Nama produk harus diisi dan harga harus berupa angka."

        try:
            db = connect_db()
            cursor = db.cursor()
            query = "UPDATE produk SET nama_produk = %s, harga = %s WHERE id_produk = %s"
            cursor.execute(query, (nama_produk, harga, id))
            db.commit()
            db.close()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {e}"

@app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    if request.method == 'POST':
        try:
            db = connect_db()
            cursor = db.cursor()
            query = "DELETE FROM produk WHERE id_produk = %s"
            cursor.execute(query, (id,))
            db.commit()
            db.close()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {e}"

    return "Method not allowed", 405



if __name__ == '__main__':
    app.run(debug=True)
