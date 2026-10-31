![Tengkorak Banner](3c81b6b26da2cee6b2964abf254ac8b9.jpg)

  # HTTP Load Tester
   
   Alat pengujian beban server (Load Tester) berbasis CLI yang ditulis menggunakan Python. Alat ini mensimulasikan banyak koneksi HTTP secara bersamaan untuk mengukur performa dan ketahanan server lokal.
   
   ## Fitur
   - Multi-threading.
   - Menampilkan total request dan RPS (Requests per second).
   - Tampilan antarmuka terminal (CLI) interaktif.
   
   ## Instalasi
   ```bash
   pip install requests
   ```
   Cara Pakai
   1. Jalankan script:
      ```bash
      python load_tester.py
      ```
   2. Masukkan URL target (contoh: http://localhost:8080).
   3. Tekan CTRL+C untuk menghentikan proses.
   Catatan
   Alat ini hanya ditujukan untuk pengujian server lokal atau server milik sendiri.
