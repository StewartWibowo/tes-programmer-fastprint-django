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
3. Library Python : `requests`, `mysqlclient`, 'pytz'
4. Styling : Bootstrap 5


Cara Instalasi Lokal
1. Pastikan XAMPP (MySQL) aktif dan buat database bernama `db_fastprint`.
2. Install requirement: `pip install -r requirements.txt`.
3. Jalankan migrasi: `python manage.py migrate`.
4. Tarik data dari API: `python manage.py tarik_data`.
5. Jalankan server: `python manage.py runserver`.

Halaman Produk Jual
<img width="1707" height="709" alt="Halaman Tambah Produk" src="https://github.com/user-attachments/assets/e2b8f4d3-0ab3-44d3-8f23-aa2ab16944c4" />

Halaman Tambah Produk
<img width="1707" height="709" alt="Halaman Tambah Produk" src="https://github.com/user-attachments/assets/8ba62d5d-3094-47f8-a3b2-2f122c484de8" />

Halaman Edit Produk
<img width="1725" height="655" alt="Halaman Edit Produk" src="https://github.com/user-attachments/assets/56745ce2-750c-400f-8383-a06e0ce7d200" />

Halaman Notifikasi Berhasil Ditambahkan
<img width="1709" height="964" alt="Halaman Notifikasi Berhasil Ditambahkan" src="https://github.com/user-attachments/assets/8f8e3131-268b-417b-878e-8dedc437e3f7" />

Halaman Notifikasi Diupdate
<img width="1729" height="976" alt="Halaman Notifikasi Berhasil Diupdate" src="https://github.com/user-attachments/assets/ecbabb09-998f-4dc0-8f91-4ba0be10861a" />

Halaman Notifikasi Berhasil Dihapus
<img width="1679" height="974" alt="Halaman Notifikasi Berhasil Dihapus" src="https://github.com/user-attachments/assets/284a9680-e136-4724-b4ec-35be32b3e30b" />

Halaman Notifikasi Konfirmasi Penghapusan
<img width="1688" height="961" alt="Halaman Notifikasi Konfirmasi Penghapusan" src="https://github.com/user-attachments/assets/ebb68fd0-f852-4e3a-997f-bad833f9e536" />
