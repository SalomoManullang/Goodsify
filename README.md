**Nama**: Salomo Immanuel Putra  
**NPM**: 2306219745  
**Kelas**: PBP B
**link** : http://salomo-immanuel-goodsify.pbp.cs.ui.ac.id/ **(harus dibukan di incognito)**

## Proses Pembuatan Projek Django "Goodsify"

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

3. **Melakukan routing pada `main` agar dapat menjalankan aplikasi**

    kita perlu melakukan routing pada main agar web yang kita buat dapat diakses melalui web. pertama tama aku mengubah isi `urls.py` dan sesuaikan dengan appku yang namanya `main` dengan kode seperti ini:
    ```bash
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Kemudian aku juga menambahkan `main.urls` ke dalam url patterns agar nantinya ketika aplikasi mau di run, yang ditampilkan adalah tampilan aplikasi main. 

4. **Membuat model pada aplikasi `main` dengan nama produk dan punya beberapa atribut wajib**

    Pertama tama, aku membuka `models.py` pada main, kemudian didalam models.py tersebut, aku menambahkan beberapa atribut seperti ini :
    ```bash 
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    ```
    atribut yang aku tambahkan adalah nama, harga, deskripsi produk, serta rating bintang 1-5. 

5. **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan   nama aplikasi serta nama dan kelas kamu.**

    pertama tama, aku buat dahulu template HTML untuk nantinya akan menunjukkan beberapa artribut yang sudah kubuat. 
    ```bash
        <h3>Nama Produk:</h3>
    <p><strong>{{ name }}</strong></p> 

    <h3>Harga:</h3>
    <p><em>{{ price }}</em></p> 
    <h3>Deskripsi:</h3>
    <p>{{ description }}</p>

    <h3>Rating:</h3>
    <p>{{ rating }}</p>
    ```
    dengan menggunakan template ini, nantinya saya dapat mengubah konteks dari value masing masing atribut yang akan ditunjukkan. saya juga menggunakan beberapa syntax seperti strong untuk membuat HTML yang ditujukkan lebih rapi. Kemudian, saya menyesuaikan context yang terdapat dalam `views.py` agar sesuai dengan produk saya.

6. **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.**

    aku menyesuaikan isi pada `urlspatterns` dan menambahkan main sebagai nama aplikasi
    ```bash
    urlpatterns = [
    path('', show_main, name='show_main'),
    ]
    ```
    show main digunakan agar nantinya yang ditujukkan adalah aplikasi main. path nya masih diisi kosong agar nantinya aplikasi dapat diakses secara langsung.

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

    pertama tama aku membuat projek baru pada PWS yang aku beri nama goodsify, kemudian aku ubah isi `ALLOWED_HOST` pada `settings.py` dengan format <username-sso>-<nama proyek>.pbp.cs.ui.ac.id. sehingga link situsku menjadi `salomo-immanuel-goodsify.pbp.cs.ui.ac.id` kemudian saya memasukkan username dan password yang sudah diberikan sebelumnya. Kemudian, aku melakukan push ke dalam PWS dari penyimpanan lokalku. 
    ```bash
    git push pws main:master
    ```

## Request Client ke Web Aplikasi Berbasis Django
---

## Fungsi Git pada Pengembangan Perangkat Lunak
---

## Alasan Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak
---

## Mengapa Model pada Django Disebut sebagai ORM?
---









