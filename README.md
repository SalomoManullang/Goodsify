**Nama**: Salomo Immanuel Putra  
**NPM**: 2306219745  
**Kelas**: PBP B

**link** : http://salomo-immanuel-goodsify.pbp.cs.ui.ac.id **(harus dibuka di incognito)**

# TUGAS 2: Implementasi Model-View-Template (MVT) pada Django
================================================================

<details>
  <summary></summary>

### Proses Pembuatan Projek Django "Goodsify"


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


### Request Client ke Web Aplikasi Berbasis Django

  ![WhatsApp Image 2024-09-10 at 23 17 34_49fe833e](https://github.com/user-attachments/assets/d4452b5c-5d7d-4a32-a0da-ec2f2df696d5)


1. Permintaan dari Pengguna: Pengguna mengakses URL tertentu (misalnya, /products), yang dikirimkan ke server Django.

2. urls.py: Server mencocokkan URL yang diminta dengan pola yang ada di urls.py dan meneruskannya ke fungsi yang sesuai di views.py.

3. views.py: View menangani request tersebut. Jika dibutuhkan, views.py berinteraksi dengan models.py untuk mengambil data dari basis data.

4. models.py: Data yang diperlukan diambil dari basis data melalui model, kemudian dikirim kembali ke views.py.

5. Template: views.py mengirimkan data yang diperoleh ke template HTML, yang kemudian merender data tersebut menjadi halaman web untuk dikirim kembali sebagai response kepada pengguna.



### Fungsi Git pada Pengembangan Perangkat Lunak

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



### Alasan Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

Django sering dipilih sebagai framework untuk memulai belajar pengembangan perangkat lunak karena memiliki banyak keunggulan. Salah satunya, Django dibangun menggunakan Python, bahasa pemrograman dengan sintaks yang sederhana dan mudah dipelajari oleh pemula. Django juga menggunakan pola Model-View-Template (MVT) yang memisahkan komponen aplikasi dengan jelas, sehingga mempermudah pengembang dalam memahami cara berbagai bagian aplikasi web bekerja satu sama lain. Django juga sudah dilengkapi oleh fitur yang lengkap sehingga programmer tidak mulai dari nol. Kesimpulannya, django sudah lengkap dan mudah untuk dipelajari untuk pemula.


### Mengapa Model pada Django Disebut sebagai ORM?

ORM (Object-Relational Mapping) adalah teknik dalam pengembangan perangkat lunak yang memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan objek-objek dari bahasa pemrograman yang mereka gunakan, alih-alih menulis perintah SQL langsung. Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ORM untuk mengelola interaksi antara aplikasi dan basis data.Pada Django, setiap model merupakan representasi dari tabel dalam basis data, di mana atribut model tersebut menggambarkan kolom-kolom dalam tabel. Dengan ORM, pengembang dapat melakukan operasi seperti membuat, membaca, memperbarui, dan menghapus data menggunakan python, sementara Django akan secara otomatis menerjemahkan tindakan tersebut ke dalam perintah SQL yang sesuai untuk berinteraksi dengan basis data. 

</details>


# TUGAS 3: Implementasi Form dan Data Delivery pada Django
===================================================================

<details>
  <summary></summary>

### Cara mengimplementasi _checklist_ diatas

1. **Cara mengimplementasikan form**

    pertama tama, saya membuat `forms.py` pada direktori `main`. pada file tersebut, saya membuat sebuah _blueprint_ forms dengan kode: 

    ```bash
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "rating"]
    ```

    kemudian, dalam `views.py` saya membuat sebuah method untuk menciptakan produk sesuai dengan yang kita masukkan pada form. 

    ```bash
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```

    Kemudian, untuk melakukan routing ke URL yang bersangkutan, aku menambahkan path baru ke dalam `URL_PATTERN`
    ```bash
        path('create-product', create_product, name='create_product'),
    ```

    Kemudian, dalam `views.py`, ubah context nya menjadi produk
    ```bash
        context = {
            'Products': products  # Ganti key menjadi 'Products' agar sesuai dengan template
        }
    ```
    Tidak lupa juga, saya kembali melengkapi `urls.py` agar tetap terhubung satu dengan lainnya. Setelah itu saya juga membuat halaman HTML baru pada direktori `main/templates`. yang bernama `create_product.html` yang isinya adalah _blueprint_ saat kita ingin membuat tombol membuat produk baru. Setelah itu, saya juga memodifikasi main.html untuk menampilkan tabel berisi produk produk yang sudah ditambahkan. 

    ```bash
    <table>
    <tr>
        <th>Nama Produk</th>
        <th>Harga</th>
        <th>Deskripsi</th>
        <th>Rating</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data Produk di bawah baris ini 
    {% endcomment %} 
    {% for Product in Products %}
    <tr>
        <td>{{ Product.name }}</td>
        <td>{{ Product.price }}</td>
        <td>{{ Product.description }}</td>
        <td>{{ Product.rating }}</td>
    </tr>
    {% endfor %}
    </table>
    ```

    dengan begitu, saya dapat membuat forum yang berisi pertanyaan terkait nama produk, harga, rating, dan deskripsi produk. Nantinya hasil jawaban tersebut akan tersimpan sebagai objek dan dituliskan dalam tabel.

    pertama tama, saya membuat `forms.py` pada direktori `main`. pada file tersebut, saya membuat sebuah _blueprint_ forms dengan kode: 

    ```bash
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "rating"]
    ```

    kemudian, dalam `views.py` saya membuat sebuah method untuk menciptakan produk sesuai dengan yang kita masukkan pada form. 

    ```bash
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```

    Kemudian, untuk melakukan routing ke URL yang bersangkutan, aku menambahkan path baru ke dalam `URL_PATTERN`
    ```bash
        path('create-product', create_product, name='create_product'),
    ```

    Kemudian, dalam `views.py`, ubah context nya menjadi produk
    ```bash
        context = {
            'Products': products  # Ganti key menjadi 'Products' agar sesuai dengan template
        }
    ```
    Tidak lupa juga, saya kembali melengkapi `urls.py` agar tetap terhubung satu dengan lainnya. Setelah itu saya juga membuat halaman HTML baru pada direktori `main/templates`. yang bernama `create_product.html` yang isinya adalah _blueprint_ saat kita ingin membuat tombol membuat produk baru. Setelah itu, saya juga memodifikasi main.html untuk menampilkan tabel berisi produk produk yang sudah ditambahkan. 

    ```bash
    <table>
    <tr>
        <th>Nama Produk</th>
        <th>Harga</th>
        <th>Deskripsi</th>
        <th>Rating</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data Produk di bawah baris ini 
    {% endcomment %} 
    {% for Product in Products %}
    <tr>
        <td>{{ Product.name }}</td>
        <td>{{ Product.price }}</td>
        <td>{{ Product.description }}</td>
        <td>{{ Product.rating }}</td>
    </tr>
    {% endfor %}
    </table>
    ```

    dengan begitu, saya dapat membuat forum yang berisi pertanyaan terkait nama produk, harga, rating, dan deskripsi produk. Nantinya hasil jawaban tersebut akan tersimpan sebagai objek dan dituliskan dalam tabel.


2. **Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**

    untuk membuat kita dapat melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Kita pertama tama perlu membuat methodnya terlebih dahulu. Oleh karena itu, saya pertama tama import asset yang dibutuhkan terlebih dahulu.
    ```bash
    from django.http import HttpResponse
    from django.core import serializers
    ```

    Setelah itu, saya barulah membuat keempat method untuk melihat objek dalam format XML, JSON, XML by ID, dan JSON by ID. method ini saya masukkan dalam ``views.py``

    ```bash
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    dengan keempat method tersebut, kita dapat melihat objek dalam berbagai format.

3. **Membuat routing URL untuk masing-masing views yang telah ditambahkan**
    
    untuk menghubungkan masing masing URL, pertama saya import terlebih dahulu function dari `views.py`

    ```bash
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```

    Kemudian, dalam `urls.py`, saya menambahkan path keempat method tersebut 
    ```bash
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ```

    dengan menambahkan keempat path tersebut, url nya menjadi saling terhubung dengan sistem utama. 

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

**Data delivery** adalah proses pengiriman dan pertukaran data dari satu sistem, aplikasi, atau perangkat ke sistem lainnya. Ini melibatkan transfer informasi secara efisien, akurat, dan aman melalui jaringan atau infrastruktur komunikasi. Data delivery sangat diperlukan dalam suatu platform karena:

1. **Medium Pengiriman yang Luas**  
   Data dapat dikirim melalui berbagai jaringan, seperti internet, intranet, atau jaringan lokal. Data delivery mencakup penggunaan protokol tertentu, seperti HTTP, TCP/IP, atau protokol khusus seperti MQTT untuk IoT.

2. **Dapat Menghubungkan Berbagai Komponen Platform**  
   Data delivery menghubungkan berbagai bagian platform (frontend, backend, database), sehingga pengguna dapat berinteraksi dengan platform dan data diproses sesuai kebutuhan.

3. **Pengelolaan dan Penyimpanan Data yang konsisten**  
   Saat data dikirimkan dari satu bagian platform ke bagian lain (misalnya dari frontend ke server atau dari server ke database), data delivery memastikan bahwa informasi yang dikirim disimpan dengan benar dan dapat diakses kembali jika diperlukan. Data delivery memastikan data yang dihasilkan atau diubah oleh satu komponen atau pengguna bisa diakses dan diperbarui di seluruh platform, menjaga konsistensi.

4. **Pengelolaan Data yang Aman**  
   Data delivery juga mencakup pengiriman data secara aman. Dalam platform, informasi sensitif seperti data pengguna atau transaksi keuangan harus dikirimkan dengan protokol aman (misalnya menggunakan enkripsi). Hal ini untuk mencegah peretasan atau penyalahgunaan data selama proses pengiriman.


### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

**XML** (Extensible Markup Language) adalah format data berbasis tag yang kompleks dan menggunakan elemen-elemen dengan struktur hierarkis, sementara **JSON** (JavaScript Object Notation) adalah format data berbasis objek yang lebih sederhana, dengan pasangan key-value.**XML** lebih cocok digunakan dalam aplikasi yang memerlukan validasi data yang ketat dan integritas struktural tinggi, seperti dalam sistem perbankan atau asuransi. **JSON** lebih tepat digunakan dalam aplikasi web dan mobile karena sifatnya yang ringan dan cepat diproses. Format ini banyak dipakai dalam API modern seperti REST, di mana kecepatan dan efisiensi transfer data sangat penting. **XML** memiliki banyak fitur seperti schema validation dan namespace yang membuatnya ideal untuk dokumen dengan struktur yang lebih rumit, sedangkan **JSON** lebih ringan dan cepat untuk parsing, menjadikannya pilihan yang lebih populer untuk aplikasi web dan transfer data modern. 

Menurut saya pribadi, **JSON** lebih baik untuk digunakan dalam platform karena saya sendiri masih belajar dalam membuat platform sehingga saya lebih membutuhkan kemudahan dibandingkan fitur yang lengkap. Saya sendiri juga masih belum butuh untuk membuat platform yang cukup rumit untuk menggunakan **XML**. Kemudahan **JSON** itulah yang membuat saya berpikir **JSON** lebih baik.

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang telah ditentukan. Saat form diisi dan disubmit, Django menggunakan `is_valid()` untuk memastikan bahwa semua input memenuhi persyaratan, seperti format data, panjang karakter, dan tipe data yang benar. Method ini memeriksa setiap field, mendeteksi kesalahan, dan mengembalikan False jika ada data yang tidak valid, memungkinkan pengguna untuk memperbaiki input. Selain itu, `is_valid()` menghentikan proses lebih lanjut, seperti penyimpanan ke database, guna mencegah data yang salah atau rusak masuk ke sistem. Dengan demikian, method ini juga meningkatkan keamanan aplikasi, mencegah serangan injeksi (seperti SQL injection) dengan memastikan hanya data yang sah dan sesuai aturan yang diproses.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**CSRF** (Cross-Site Request Forgery) adalah jenis serangan di mana penyerang dapat memaksa pengguna untuk mengirim permintaan yang tidak diinginkan dari browser mereka tanpa sepengetahuan mereka. Django menggunakan `csrf_token` untuk melindungi form dari serangan ini. Token ini adalah nilai unik yang dihasilkan setiap kali halaman dengan form dimuat dan harus dikirim bersama dengan permintaan POST. Ini memastikan bahwa permintaan hanya valid jika berasal dari sumber yang sah.

Jika `csrf_token` tidak ditambahkan, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat membuat pengguna tanpa sadar mengirimkan permintaan berbahaya, seperti mengubah pengaturan akun atau melakukan transaksi yang tidak diinginkan, tanpa persetujuan pengguna.

Penyerang bisa memanfaatkan celah keamanan ini dengan membuat sebuah halaman berbahaya yang secara diam-diam mengirimkan permintaan ke aplikasi Django atas nama pengguna yang sedang aktif masuk. Misalnya, penyerang bisa membuat skrip yang secara otomatis melakukan permintaan POST ke server tanpa sepengetahuan pengguna. Tanpa adanya csrf_token, server tidak akan memiliki cara untuk membedakan apakah permintaan itu sah atau tidak. Hal ini dapat dimanfaatkan untuk mengubah pengaturan akun kalian.

### Sreenshot Postman

1. **Format JSON**
   ![image](https://github.com/user-attachments/assets/2965dd12-4283-426c-941a-371f35f45411)

2. **Format XML**
   ![image](https://github.com/user-attachments/assets/b4cbfe47-4669-452f-b4d1-a381133f3ec0)

3. **Format JSON by ID**
   ![image](https://github.com/user-attachments/assets/fe4a42af-6197-43c5-a024-aa2c9d4b5c22)

4. **Format XML by ID**
   ![image](https://github.com/user-attachments/assets/169fd8ae-e934-4ff1-a4e9-be9eea537a9a)

</details>

# TUGAS 4: Implementasi Autentikasi, Session, dan Cookies pada Django
===============================================================================

<details>
  <summary></summary>

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Setelah sebelumnya sudah membuat form untuk menambahkan produk yang ingin ditambahkan ke dalam aplikasi, selanjutnya saya akan membuat setiap pengguna memiliki akun mereka sendiri sendiri, sehingga setiap akun memiliki produk mereka sendiri sendiri. Pertama tama, Saya import dahulu `UserCreationForm` dan `messages` dalam `views.py`. kemudian, saya menambahkan fungsi `register`.

```bash
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Selanjutnya, saya juga membuat sebuah file html baru yang bernama `register.html` Ini berisi template tampilan register page pada aplikasi saya 

```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

Setelah itu, saya juga menambahkan _path url_nya ke dalam `urls.py`. Sejauh ini, saya sudah berhasil membuat ragister page. Selanjutnya, saya akan membuat fungsi login. Pertama tama, pada `views.py`, saya mengimport dahulu `authenticate`, `login`, dan `AuthenticationForm`. Kemudian, saya membuat fungsi untuk login user

```bash
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Selanjutnya, sama dengan pembuatan page register, saya membuat juga page html untuk page login yang bernama `login.html`. tidak lupa juga saya menambahkan _path url_nya ke dalam `URL_PATTERNS` pada `urls.py`. Fungsi login sudah selesai, selanjutnya, saya akan membuat fungsi logout. Pertama tama, pada `views.py` saya mengimport `logout`. Kemudian, saya menambahkan function logout.

```bash
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Tidak lupa, saya menambahkan tombol logout juga di samping tombol tambah produk. Setelah itu, saya menambahkan _path url_nya ke dalam `urls.py`. Setelah selesai membuat page register, login, dan logout, saya ingin merestriksi page main agar hanya bisa dibuka dengan login terlebih dahulu. Pertama tama, pada `views.py`, saya mengimport `login_required` dan menambahkan
```bash
@login_required(login_url='/login')
```
diatas function `show_main`. Setelah itu, main hanya bisa dibuka juga pengguna sudah melakukan login terlebih dahulu. 

### Menerapkan Cookies pada halaman aplikasi 



### Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

`HttpResponseRedirect()` adalah kelas di Django yang digunakan untuk mengarahkan pengguna menuju URL tertentu. kalian harus memberikan URL valid dan lengkap sebagai argumen. Misalnya, untuk mengarahkan ke `/some/url/`, kalian harus menggunakan `HttpResponseRedirect('/some/url/')`. Di sini, kalian perlu mengatur URL secara manual.

Sedangkan, `redirect()` adalah fungsi yang lebih mudah dan fleksibel. Selain URL, fungsi ini bisa menerima nama tampilan atau objek Django sebagai argumen. Fungsi ini secara otomatis mengonversi argumen menjadi URL yang benar untuk pengalihan, sehingga kalian tidak perlu mengelola URL sendiri. Contohnya adalah: 

```bash
def my_view(request):
    return redirect('/some/url/')
```

| **Aspek**                 | **HttpResponseRedirect()**                                      | **redirect()**                                               |
|---------------------------|-----------------------------------------------------------------|--------------------------------------------------------------|
| **Jenis**                 | Kelas respons HTTP                                             | Fungsi bantu (helper function)                               |
| **Argumen yang Diterima**  | URL absolut atau relatif                                        | URL, nama tampilan (view name), atau objek (instance model)   |
| **Pengelolaan URL**        | Harus mengelola pembuatan URL secara manual                     | Mengonversi argumen menjadi URL secara otomatis               |
| **Fleksibilitas**          | Hanya menerima URL                                             | Lebih fleksibel, dapat menerima URL, nama tampilan, atau objek|
| **Kemudahan Penggunaan**   | Mengharuskan pengguna mengelola detail URL                     | Lebih sederhana dan otomatis dalam pembuatan URL              |
| **Contoh Penggunaan**      | `HttpResponseRedirect('/some/url/')`                           | `redirect('/some/url/')` atau `redirect('view-name')`         |

kesimpulannya, `redirect()` adalah cara yang lebih sederhana dan fleksibel untuk melakukan pengalihan (redirect) di Django dibandingkan dengan `HttpResponseRedirect()`. Dengan menggunakan `redirect()`, kalian dapat memberikan berbagai jenis argumen seperti URL, nama tampilan, atau objek model. Django akan secara otomatis mengonversi argumen tersebut ke URL yang benar, sehingga Anda tidak perlu mengelola pembuatan URL secara manual.

### Cara kerja penghubungan model Product dengan User


### perbedaan antara _authentication_ dan _authorization_ dan cara django mengimplementasikannya

**Authentication** adalah proses memverifikasi identitas pengguna untuk memastikan mereka adalah pengguna yang sah dengan menggunakan kredensial seperti username dan password.

**Authorization** adalah proses yang terjadi setelah otentikasi berhasil, di mana sistem menentukan tindakan dan sumber daya apa yang dapat diakses oleh pengguna berdasarkan peran atau izin yang dimilikinya. 

Contohnya adalah ketika pengguna memasukkan nama dan password mereka, itu merupakan tahap **authentication**. Setelah itu, barulah sistem menentukan apa yang bisa dilakukan pengguna lewat **Authorization**. Misalnya pengguna adalah Customer, mereka hanya bisa membeli barang, sedangkan jika pengguna adalah Admin, mereka dapat menambahkan barang dan mengubah properti pada page. 

Dalam Django, autentikasi dan otorisasi diimplementasikan melalui modul bawaan `django.contrib.auth`, yang mengelola proses login, logout, dan izin akses pengguna. Autentikasi memverifikasi identitas pengguna dengan memeriksa kredensial seperti username dan password menggunakan fungsi `authenticate()`, dan jika valid, pengguna akan diautentikasi serta diberikan sesi melalui `login()`. Setelah pengguna berhasil masuk, Django menerapkan otorisasi dengan menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu menggunakan permissions dan groups. 


### Cara Django mengingat pengguna yang login

Django mengingat pengguna yang telah login dengan menggunakan **cookies** dan **session**. Setelah pengguna berhasil login, Django menyimpan informasi sesi pada server dan mengirimkan _session ID_ ke browser pengguna dalam bentuk cookie. Setiap kali pengguna membuat permintaan baru (misalnya memuat halaman lain), browser mengirimkan cookie tersebut kembali ke server, memungkinkan Django untuk mengidentifikasi pengguna yang sedang aktif.

### Apakah semua Cookies aman digunakan?

Tidak semua cookies aman untuk digunakan, karena beberapa cookies rentan terhadap serangan dan eksploitasi oleh pihak yang tidak berwenang. Ada beberapa resiko keamanan yang dapat dilakukan peretas melalui cookies:

1. **Cookies bisa dicuri**

    Cookies disimpan di browser pengguna dan dapat dicuri melalui serangan tertentu, seperti **Cross-Site Scripting** (XSS). Jika cookie yang dicuri berisi informasi seperti session ID, penyerang bisa mengambil alih sesi pengguna dan berpura-pura menjadi pengguna yang sah.

2. **Cookies bisa diintip**

    Jika website menggunakan `HTTP` (bukan HTTPS), maka data yang dikirimkan, termasuk cookies, tidak dienkripsi. Ini berarti data tersebut dapat dengan mudah diintip oleh pihak ketiga di jaringan yang sama, seperti pada Wi-Fi publik. Penyerang bisa mendapatkan akses ke cookies dan menggunakan informasi tersebut untuk mencuri sesi atau informasi pribadi pengguna.

3. **Cookies bisa dimanipulasi**

    Cookies dapat dimodifikasi oleh penyerang jika mereka memiliki akses ke cookies di browser. Dengan cookies berisi session pengguna, penyerang bisa mendapatkan akses ke data atau area aplikasi yang tidak seharusnya mereka akses.

4. **Serangan CSRF (Cross-Site Request Forgery)**

    **CSRF** (Cross-Site Request Forgery) adalah jenis serangan di mana penyerang memanfaatkan sesi pengguna yang sah untuk melakukan tindakan berbahaya di situs web tanpa sepengetahuan atau persetujuan pengguna. Misalnya, kalian sedang login di _M - Banking_ dan seorang penyerang membuat Anda mengklik link berbahaya yang secara otomatis mengirim permintaan ke situs bank untuk mentransfer uang sebesar Rp.1.000.000,00 ke akun penyerang. Karena Anda sudah login, browser akan menyertakan cookies session kalian, dan situs bank akan memproses transfer tersebut seolah-olah kalian yang memintanya, padahal kalian tidak pernah memberikan persetujuan untuk itu.

5. **Beberapa cookies memiliki waktu Experation yang lama**

    Cookies bisa disetel untuk bertahan dalam waktu lama, bahkan setelah pengguna menutup browser. Jika cookies tetap aktif terlalu lama, ada risiko bahwa jika perangkat pengguna hilang atau dicuri, cookies tersebut bisa dimanfaatkan oleh orang lain untuk mengakses akun tanpa harus login ulang.


</details>





