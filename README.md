# PERTEMUAN 07 - FUNGSI PYTHON

## Identitas Mahasiswa

* **Nama:** Reva Liyanasari
* **NIM:** 2225250101
* **Kelas:** 3A
* **Mata Kuliah:** Algoritma dan Pemrograman
* **Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.

## Tujuan Repositori

Repositori ini dibuat untuk memenuhi kegiatan praktik mata kuliah Algoritma dan Pemrograman pada Pertemuan 07 dengan materi fungsi, parameter, return value, dan scope variabel dalam Python.

Melalui praktik ini, mahasiswa diharapkan mampu:
- Membuat fungsi dengan tugas yang jelas dan terstruktur.
- Menggunakan parameter untuk menerima data masukan.
- Menggunakan `return` untuk mengembalikan hasil perhitungan.
- Menerapkan perulangan dan seleksi dalam program.
- Membuat program utilitas matematika yang modular.
- Melakukan pengujian program berdasarkan test case yang ditentukan.

## Daftar Berkas

### Praktik 2 - Utilitas Matematika Modular

**`praktik/utilitas_matematika.py`**

Program utilitas matematika berbasis menu yang menyediakan empat operasi, yaitu:
1. Menghitung luas persegi panjang.
2. Menghitung luas segitiga.
3. Menghitung jumlah bilangan dari 1 sampai n.
4. Menghitung faktorial suatu bilangan.

Program menggunakan fungsi untuk memisahkan setiap proses perhitungan, perulangan untuk melakukan penjumlahan dan perkalian, serta seleksi untuk menjalankan operasi berdasarkan pilihan pengguna. Program juga menerapkan validasi agar nilai n tidak negatif pada operasi jumlah bilangan dan faktorial.

## Cara Menjalankan

1. Buka folder repositori melalui Visual Studio Code.
2. Buka terminal pada direktori utama repositori.
3. Jalankan perintah berikut:

   ```bash
   python praktik/utilitas_matematika.py
   ```
4. Pilih operasi sesuai menu yang ditampilkan.
5. Masukkan nilai yang diminta dan periksa hasil perhitungannya.

## Struktur Fungsi

1. `luas_persegi_panjang(p, l)`: Menghitung luas persegi panjang dengan parameter panjang (`p`) dan lebar (`l`), lalu mengembalikan hasil perkalian `p * l`.

2. `luas_segitiga(a, t)`: Menghitung luas segitiga dengan parameter alas (`a`) dan tinggi (`t`), lalu mengembalikan hasil perhitungan `0.5 * a * t`.

3. `jumlah_n(n)`: Menghitung jumlah bilangan dari 1 sampai `n` menggunakan perulangan, kemudian mengembalikan nilai totalnya.

4. `faktorial(n)`: Menghitung faktorial bilangan `n` menggunakan perulangan, kemudian mengembalikan hasilnya. Jika `n = 0`, fungsi mengembalikan nilai `1`.

5. `tampilkan_menu()`: Menampilkan daftar pilihan operasi matematika kepada pengguna.

## Hasil Pengujian

## Hasil Pengujian

| No. | Pengujian | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Luas persegi panjang | Pilihan: `1`<br/>Panjang: `8`<br/>Lebar: `5` | `Luas persegi panjang = 40.0` | `Luas persegi panjang = 40.0` | Berhasil |
| 2 | Luas segitiga | Pilihan: `2`<br/>Alas: `10`<br/>Tinggi: `6` | `Luas segitiga = 30.0` | `Luas segitiga = 30.0` | Berhasil |
| 3 | Jumlah bilangan 1 sampai n | Pilihan: `3`<br/>n: `10` | `Jumlah 1 sampai 10 = 55` | `Jumlah 1 sampai 10 = 55` | Berhasil |
| 4 | Faktorial bilangan | Pilihan: `4`<br/>n: `5` | `Faktorial 5 = 120` | `Faktorial 5 = 120` | Berhasil |
| 5 | Faktorial nol | Pilihan: `4`<br/>n: `0` | `Faktorial 0 = 1` | `Faktorial 0 = 1` | Berhasil |
| 6 | Validasi bilangan negatif | Pilihan: `3`<br/>n: `-2` | `Error: n harus bilangan bulat nonnegatif.` | `Error: n harus bilangan bulat nonnegatif.` | Berhasil |

## Refleksi

Melalui praktik ini, saya mempelajari bahwa fungsi dapat membantu membagi program menjadi bagian-bagian yang lebih terstruktur dan mudah dipahami. Penggunaan parameter memungkinkan fungsi menerima nilai yang berbeda, sedangkan `return` digunakan untuk mengembalikan hasil perhitungan agar dapat diproses atau ditampilkan oleh bagian program lainnya.

Selain itu, penggunaan perulangan membantu proses penjumlahan dan perkalian secara berulang, sedangkan seleksi memungkinkan program menjalankan operasi sesuai pilihan pengguna. Praktik ini membantu saya memahami penerapan fungsi dalam membangun program matematika yang modular dan mudah diuji.

## Sumber

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 07, Fungsi, Parameter, Return Value, dan Scope dalam Python.
- Python Software Foundation, dokumentasi Python 3 mengenai definisi fungsi.