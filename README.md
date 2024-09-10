**Nama**: Salomo Immanuel Putra  
**NPM**: 2306219745  
**Kelas**: PBP B

**Proses Pembuatan Projek Django "Goodsify"**

setelah mencoba mencari ide tentang aplikasi yang sesuai saya akhirnya terpikirkan untuk membuat aplikasi yang berfokus pada jual beli barang online atau _e-commerce_ yang akan saya beri nama `goodsify`. goodsify sendiri adalah aplikasi yang berfokus pada penjualan barang barang bekas atau tidak terpakai. nantinya user dapat menampilkan nama, gambar, harga, dan deskripsi produk yang mereka jual disana. dan dapat bertransaksi menggunakan kartu atau rekening yang sudah ditautkan. 

1. **Membuat sebuah proyek django baru**

    1. **Membuat sebuah repository Github baru** bernama `goodsify`.

    2. **Meng-clone repository kosong tersebut** ke komputer lokal:  
    ```bash
    git clone https://github.com/SalomoManullang/goodsify.git
    cd goodsify
    ```

    3. **Menghubungkan penyimpanan lokal dengan GitHub:**  
    ```bash
    git remote add origin https://github.com/SalomoManullang/goodsify.git
    ```

    4. **Membuat _Virtual Environment_ :**  
    ```bash
    python -m venv env
    ```

    5. **Mengaktifkan _Virtual Environment_ :**  
        ```bash
        env\Scripts\activate
        ```

    6. **Membuat file bernama `requirements.txt` dengan isi sebagai berikut:**

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```

    7. **Menginstall dependensi yang ada di `requirements.txt` dengan perintah berikut:**  
    ```bash
    pip install -r requirements.txt
    ```

    8. **buat projek django baru**
    ```bash
    django-admin startproject goodsify .
    ```
    9. **Menjalankan server**
    dengan mengubah isi dari allowed host agar terhubung dengan localhost komputer, saya dapat menentukan dimana server akan berjalan. kemudian saya juga men-run servernya.
    ```bash
    python manage.py runserver
    ```
    kemudian dengan mengecek di http://localhost:8000 saya bisa melihat apakah projek saya sudah berjalan atau belum

2. **Membuat aplikasi dengan nama `main` pada projek tersebut :**
   
   pertama tama saya membuat dahulu projek aplikasi dengan nama `main`
   ```bash
   python manage.py startapp main
   ```
   setelah itu saya mendaftarkan nama aplikasi main tersebut ke dalam `INSTALLED_APPS`






