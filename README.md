Fitur Utama
1. Integrasi API dari website FastPrint
2. Terdapat CRUD : Create, Read, Update ,Delete
3. Filter Status : Menampilkan data yang hanya memiliki status "bisa dijual" di halaman utama.
4. Validasi Form : Validasi input nama (wajib diisi) dan harga (harus angka).
5. Notifikasi : Flash messages (pop-up) untuk setiap aksi berhasil/gagal.
6. Konfirmasi Hapus : Alert konfirmasi sebelum menghapus data.


Teknologi yang digunakan :
1. Framework : Django 4.2
2. Database : MySQL / MariaDB (via XAMPP)
3. Library Python : `requests`, `mysqlclient`
4. Styling : Bootstrap 5


Cara Instalasi Lokal
1. Pastikan XAMPP (MySQL) aktif dan buat database bernama `db_fastprint`.
2. Install requirement: `pip install -r requirements.txt`.
3. Jalankan migrasi: `python manage.py migrate`.
4. Tarik data dari API: `python manage.py tarik_data`.
5. Jalankan server: `python manage.py runserver`.
