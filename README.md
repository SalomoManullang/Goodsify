**Nama**: Salomo Immanuel Putra  
**NPM**: 2306219745  
**Kelas**: PBP B

**link** : http://salomo-immanuel-goodsify.pbp.cs.ui.ac.id **(harus dibuka di incognito)**

# TUGAS 2

<details>
  <summary></summary>

### Proses Pembuatan Projek Django "Goodsify"
<details>
  <summary></summary>

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

</details>

### Request Client ke Web Aplikasi Berbasis Django
<details>
    <summary></summary>

  ![WhatsApp Image 2024-09-10 at 23 17 34_49fe833e](https://github.com/user-attachments/assets/d4452b5c-5d7d-4a32-a0da-ec2f2df696d5)


1. Permintaan dari Pengguna: Pengguna mengakses URL tertentu (misalnya, /products), yang dikirimkan ke server Django.

2. urls.py: Server mencocokkan URL yang diminta dengan pola yang ada di urls.py dan meneruskannya ke fungsi yang sesuai di views.py.

3. views.py: View menangani request tersebut. Jika dibutuhkan, views.py berinteraksi dengan models.py untuk mengambil data dari basis data.

4. models.py: Data yang diperlukan diambil dari basis data melalui model, kemudian dikirim kembali ke views.py.

5. Template: views.py mengirimkan data yang diperoleh ke template HTML, yang kemudian merender data tersebut menjadi halaman web untuk dikirim kembali sebagai response kepada pengguna.

</details>


### Fungsi Git pada Pengembangan Perangkat Lunak
<details>
  <summary></summary>

Git adalah Salah satu perangkat lunak atau tools kolaborasi _coding_ yang sering digunakan oleh programmer ketika mereka ingin mengerjakan suatu proyek yang membutuhkan banyak orang untuk mengerjakannya. Git memungkinkan mereka untuk menggabungkan kode mereka ke dalam satu repository seperti penyimpanan utama. Nantinya, programmer dapat mengerjakan bagian mereka masing masing baru di-_push_ ke dalam repository tersebut. Ini adalah beberapa fungsi git dalam pengembangan perangkat lunak:

1. **Dapat digunakan untuk kolaborasi**

    dengan menggunakna git, para programmer dapat mengunggah kode mereka ataupun mengambil kode orang lain sebagai inspirasi mereka. Dengan menggunakan repository, Setiap anggota tim dapat meng-clone repository ini ke komputer mereka, yang memungkinkan mereka bekerja secara lokal tanpa langsung memodifikasi repository utama. Dengan menggunakan merge, programmer juga bisa menggabungkan program mereka dengan program orang lain ke dalam 1 repository utama. Menggunakan branch, programmer daoat mengubah atau memperbarui program mereka tanpa harus mengubah data utama. Dalam jangka panjang, git dibutuhkan jika projeknya terus di-_update_

2. **Membantu mengorganisir**

    menggunakan git, kita dapat memasukkan README yang nantinya dapat menjadi panduan programmer untuk mengerjakan proyek, selain itu git juga tidak jarang untuk digunakan sebagai tempat penyimpanan cloud karena rapi dan bersih. 

3. **digunakan dalam proyek open source**

    Proyek open source adalah proyek pengembangan proyek di mana kode sumbernya (source code) tersedia secara bebas untuk dilihat, digunakan, dimodifikasi, dan didistribusikan oleh siapa saja. Artinya, siapa pun bisa berkontribusi untuk meningkatkan perangkat lunak tersebut atau menggunakan kodenya untuk membuat produk baru, tanpa perlu membayar lisensi. menggunakan fotur seperti clone, programmer dapat mengambil kode orang lain dan mengembangkannya. Disisi lain, proyek tersebut juga bisa di-_update_ oleh semua orang lewat perantara github. 

4. **Plattform yang fleksibel**

    Git adalah plattform yang serbaguna, bisa digunakan ketika ingin menyimpan data, mengambil referensi, membuat proyek, dan masih banyak kegunaan lainnya. dengan adanya plattform yang fleksibel, programmer tak perlu menggunakan banyak plattform, sehingga lebih efektif.

5. **Menjadi backup**

    Git dapat digunakan sebagai backup ketika data dalam penyimpanan lokal kita terhapus.

</details>


### Alasan Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

<details>
  <summary></summary>
Django sering dipilih sebagai framework untuk memulai belajar pengembangan perangkat lunak karena memiliki banyak keunggulan. Salah satunya, Django dibangun menggunakan Python, bahasa pemrograman dengan sintaks yang sederhana dan mudah dipelajari oleh pemula. Django juga menggunakan pola Model-View-Template (MVT) yang memisahkan komponen aplikasi dengan jelas, sehingga mempermudah pengembang dalam memahami cara berbagai bagian aplikasi web bekerja satu sama lain. Django juga sudah dilengkapi oleh fitur yang lengkap sehingga programmer tidak mulai dari nol. Kesimpulannya, django sudah lengkap dan mudah untuk dipelajari untuk pemula.

</details>

### Mengapa Model pada Django Disebut sebagai ORM?

<details>
  <summary></summary>
ORM (Object-Relational Mapping) adalah teknik dalam pengembangan perangkat lunak yang memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan objek-objek dari bahasa pemrograman yang mereka gunakan, alih-alih menulis perintah SQL langsung. Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ORM untuk mengelola interaksi antara aplikasi dan basis data.Pada Django, setiap model merupakan representasi dari tabel dalam basis data, di mana atribut model tersebut menggambarkan kolom-kolom dalam tabel. Dengan ORM, pengembang dapat melakukan operasi seperti membuat, membaca, memperbarui, dan menghapus data menggunakan python, sementara Django akan secara otomatis menerjemahkan tindakan tersebut ke dalam perintah SQL yang sesuai untuk berinteraksi dengan basis data. 

</details>
</details>











