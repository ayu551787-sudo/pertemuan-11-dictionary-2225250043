
# Pertemuan 11 - Dictionary/Map

Nama: Ayu Syarifatu Zahra  
NIM: 2225250043  
Kelas: 3B

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value dalam bahasa pemrograman Python.

## Struktur Data

Program menggunakan dictionary `data_mahasiswa` untuk menyimpan data mahasiswa.

Setiap mahasiswa memiliki NIM sebagai key utama, sedangkan value berupa dictionary yang berisi nama, kelas, dan nilai.

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}
```

Keterangan:
- Key utama: NIM mahasiswa, seperti A001, A002, dan A003.
- `nama`: Menyimpan nama mahasiswa.
- `kelas`: Menyimpan kelas mahasiswa.
- `nilai`: Menyimpan nilai mahasiswa.

## Cara Menjalankan

Jalankan program melalui terminal VS Code menggunakan perintah:

```bash
python3 praktik/data_mahasiswa.py
```

Jika menggunakan Windows, dapat menggunakan:

```bash
python praktik/data_mahasiswa.py
```

## Algoritma

1. Menyiapkan dictionary `data_mahasiswa` yang berisi minimal lima mahasiswa.
2. Membuat fungsi `cari_mahasiswa(data, nim)` untuk mencari data berdasarkan NIM.
3. Membuat fungsi `rata_rata_nilai(data)` untuk menghitung rata-rata nilai seluruh mahasiswa.
4. Melakukan pencarian NIM yang tersedia dan tidak tersedia.
5. Menampilkan pesan "Data tidak ditemukan" jika NIM tidak tersedia.
6. Menambahkan satu mahasiswa baru dengan NIM A006.
7. Memperbarui nilai mahasiswa dengan NIM A002 menjadi 82.
8. Menampilkan seluruh data mahasiswa menggunakan `items()`.
9. Menghitung dan menampilkan rata-rata nilai seluruh mahasiswa.

## Test Case

| No | Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Pencarian tersedia | A003 | Data Citra ditampilkan | Data Citra ditampilkan | Sesuai |
| 2 | Pencarian tidak tersedia | A999 | Data tidak ditemukan | Data tidak ditemukan | Sesuai |
| 3 | Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 menjadi 82 | Sesuai |
| 4 | Penambahan data | A006 | Key A006 tersedia setelah ditambahkan | Key A006 tersedia | Sesuai |
| 5 | Rekap | items() | Semua NIM dan data tampil | Semua data mahasiswa tampil | Sesuai |

## Refleksi

Salah satu kesalahan yang dapat terjadi dalam penggunaan dictionary adalah mengakses key yang tidak tersedia. Jika menggunakan akses langsung seperti `data_mahasiswa["A999"]`, program dapat mengalami `KeyError`.

Cara memperbaikinya adalah dengan menggunakan method `get()` atau memeriksa keberadaan key menggunakan `in` sebelum mengakses data.

Dengan demikian, program dapat menampilkan pesan "Data tidak ditemukan" tanpa mengalami error.

Melalui tugas ini, saya memahami bahwa dictionary dapat digunakan untuk menyimpan data mahasiswa secara terstruktur menggunakan pasangan key-value. Selain itu, dictionary memudahkan proses pencarian, penambahan, pembaruan, dan pengolahan data.

## Kesimpulan

Pada pertemuan 11, saya mempelajari penggunaan dictionary dalam Python untuk mengelola data mahasiswa. Program dapat mencari mahasiswa berdasarkan NIM, menambahkan data baru, memperbarui nilai, menampilkan seluruh data, dan menghitung rata-rata nilai mahasiswa.

Penggunaan dictionary membuat pengelolaan data menjadi lebih mudah, terstruktur, dan efisien.
