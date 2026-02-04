import requests
import hashlib
from datetime import datetime
from django.core.management.base import BaseCommand
from produk.models import Produk, Kategori, Status

class Command(BaseCommand):
    help = 'Mengambil data dari API Fastprint dan menyimpannya ke database'

    def handle(self, *args, **kwargs):
        now = datetime.now()
        tgl = now.strftime("%d")
        bln = now.strftime("%m")
        thn = now.strftime("%y")
        
        # Pembuatan password & username (sesuai tanggal server)
        raw_password = f"bisacoding-{tgl}-{bln}-{thn}"
        password_md5 = hashlib.md5(raw_password.encode()).hexdigest()
        
        # Username mengikuti tanggal: tesprogrammer + tgl + bln + thn + kode
        username = "tesprogrammer020226C14".strip()

        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        
        payload = {
            'username': username,
            'password': password_md5
        }

        # Header tambahan sesuai HINT soal
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
        }

        self.stdout.write(f"Menembak API dengan Username: {username}")
        self.stdout.write(f"Raw Password: {raw_password}")

        try:
            # Inisialisasi session (agar cookies dari server tersimpan)
            session = requests.Session()
            
            # Kirim permintaan POST menggunakan objek session. Menggunakan session.post, bukan requests.post
            response = session.post(url, data=payload, headers=headers)
            
            # Menampilkan status untuk debugging
            self.stdout.write(f"Status Server: {response.status_code}")

            if response.status_code != 200:
                self.stdout.write(f"Response Body: {response.text}")
            
            # Parsing JSON
            try:
                data = response.json()
            except:
                self.stdout.write(self.style.ERROR(f"Server tidak kirim JSON. Isi: {response.text[:100]}"))
                return

            # Logika penyimpanan
            if data.get('error') == 0:
                for item in data['data']:
                    kat, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
                    stat, _ = Status.objects.get_or_create(nama_status=item['status'])
                    
                    Produk.objects.update_or_create(
                        id_produk=item['id_produk'],
                        defaults={
                            'nama_produk': item['nama_produk'],
                            'harga': item['harga'],
                            'kategori': kat,
                            'status': stat
                        }
                    )
                self.stdout.write(self.style.SUCCESS("BERHASIL! Data sudah masuk database."))
            else:
                self.stdout.write(self.style.ERROR(f"API Menolak: {data.get('ket')}"))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Koneksi Gagal: {str(e)}"))