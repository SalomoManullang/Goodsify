**Nama**: Salomo Immanuel Putra  
**NPM**: 2306219745  
**Kelas**: PBP B

**link** : http://salomo-immanuel-goodsify.pbp.cs.ui.ac.id **(harus dibuka di incognito)**

# TUGAS 2: Implementasi Model-View-Template (MVT) pada Django

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

<details>
  <summary></summary>

### cara mengimplementasikan _Checklist_ tugas

1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**

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

2. **Menerapkan Cookies pada halaman aplikasi**

    Saya ingin menggunakan _cookies_ pada web saya, yang pertama saya lakukan adalah meng-_import_ H`ttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py`. Kemudian, pada function `login_user`, saya menambahkan potongan kode untuk menggunakan cookies setiap kali login untuk membuat _cookies_ last_login setiap kali user login.

    ```bash
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```

    Kemudian, pada bagian `context` di function `show_main`, tambahkan juga `last_login` di dalamnya.
    ```bash
    context = {
        ....
        'last_login': request.COOKIES['last_login'],
    }
    ```
    Kemudian, saya juga menambahkan 
    ```bash
        response.delete_cookie('last_login')
    ```
    pada function `logout_user` untuk menghapus _cookies_ terakhir login pada saat pengguna logout. Kemudian, aku juga menampahkan teks yang menunjukkan kapan kita terakhir login pada berkas `main.html`.

3. **Menghubungkan model Product dengan User**

    Saya ingin membuat setiap user memiliki produk yang mereka tambahkan sendiri sendiri, oleh karena itu saya ingin menghubungkan antara user dengan produk yang mereka buat masing masing. Pertama, saya mengimport `User` pada `models.py`. Kemudian, pada model Product yang sudah dibuat, saya menambahkan

    ```bash
    class Product(models.Model):
        ....
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

    kode tersebut bertujuan untuk menghubungkan setiap produk yang dibuat dengan masing masing user. Kemudian pada `views.py`, saya juga menambahkan beberapa penambahan kode
    ```bash
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```

    kode `commit=False` bertujuan supaya sistem tidak langsung menyimpan produk yang ditambahkan oleh pengguna langsung ke _database_ tetapi dilihat dahulu siapa pengguna yang login. Kemudian, pada variabel `products` di `show_main`, ubah isinya menjadi seperti ini:

    ```bash
    def show_main(request):
    products = MoodEntry.objects.filter(user=request.user)
    context = {
         'name': request.user.username,
    }
    ```

    Ini bertujuan agar program hanya mengambil product yang terhubung dengan `user` yang terhubung saja. Kemudian setelah mengubah berbagai variabel pada `models.py` tidak lupa juga saya melakukan migrations. Ketika saya melakukan migrations, maka semua produk yang telah saya buat terhapus, tetapi itu tidak apa apa karena nanti saya akan membuat produk baru. Terakhir, saya import `os` agar program saya bersiap siap untuk _environtment production_.

4. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**

    Saya membuat 2 dummy account yang bernama `salomotes` dan `sal2`
   1) **salomotes**

   ![image](https://github.com/user-attachments/assets/9e23f742-ab7b-4fc8-8e62-2756be4615fe)

   2) **sal2** 

   ![image](https://github.com/user-attachments/assets/2493a811-9bf5-42fc-921f-694429569418)


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

Penghubungan model `Product` dengan model `User` di Django dilakukan menggunakan relasi **ForeignKey**. Ini berarti setiap objek Product dapat dihubungkan dengan satu user tertentu yang menciptakannya. Relasi ini memungkinkan kita untuk mengasosiasikan produk dengan `user` tertentu sehingga setiap produk yang ditambahkan atau dimodifikasi dapat diatur berdasarkan `user`.

misalnya pada kode ini
```bash
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

`ForeignKey(User)`: Menghubungkan produk ke `user`.
`on_delete=models.CASCADE`: Jika `user` dihapus, produk yang terkait juga dihapus.

Kemudian, sistem juga menyimpan produk yang terikat dengan `user`
```bash
product.user = request.user
```
kode ini mengasosiasikan produk yang sedang dibuat dengan user yang sedang login. Sistem juga hanya menampilkan produk yang telah dibuat oleh `user`

```bash
def show_main(request):
    products = Product.objects.filter(user=request.user)  # Filter berdasarkan user
    return render(request, "main.html", {'Products': products})
```

`Product.objects.filter(user=request.user)`: kode ini memfilter produk yang hanya dimiliki oleh user yang sedang login. Produk milik user lain tidak akan ditampilkan.


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


# TUGAS 5: Desain Web menggunakan HTML, CSS dan Framework CSS

<details>
  <summary></summary>

### cara mengimplementasikan _Checklist_ tugas


1. **Membuat fungsi untuk menghapus dan mengedit product**

    Setelah kemarin mengatur cookies website, sekarang saya ingin menambahkan fitur untuk dapat mengahpus dan mengedit produk yang telah ditambahkan ke dalam Goodsify. Pertama tama, saya ingin membuat fitur `edit_mood`. Pertama tama, pada `views.py` saya  import `reverse` dan  `HttpResponseRedirect` kemudian saya juga menambahkan method `edit_produk`. 
    
    ```bash
    def edit_produk(request, id):
    produk = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=produk)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_product.html", context)
    ```

    function `edit_produk` bekerja dengan membuat user kembali mengisi form lalu sistem akan _reverse_ informasi yang sebelumnya sudah ada lalu diganti dengan yang baru. Setelah itu saya juga membuat page html baru yang bernama `edit_produk.html`. pada html ini, sistem akan menunjukkan form sebagai tabel, jadi kita memasukkan kembali input yang ingin kita ubah. Setelah itu saya menghubungkan juga path nya lewat `urls.py`. Terakhir, pada `main.html`, saya menambahkan tombol edit produk. 

    Setelah membuat fitur edit produk, saya lanjut membuat fitur hapus produk. Pertama tama, pada `views.py` saya menambahkan method `edit_produk`. 

    ```bash
    def delete_product(request, id):
        produk = Product.objects.get(pk = id)
        produk.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

    fitur `edit_produk` ini bekerja dengan cara mencari id produk yang dipilih, lalu menghapus id tersebut. Setelah itu saya juga membuat page html baru yang bernama `delete_product.html`.  Setelah itu saya menghubungkan juga path nya lewat `urls.py`. Terakhir, pada `main.html`, saya menambahkan tombol hapus produk. 


2. **Kostumisasi halaman _login_, _register_, _Navigation bar_, edit produk, dan tambah produk agar lebih menarik**


    Agar aplikasi saya terlihat menjadi lebih menarik, saya mulai untuk memperbagus halaman utama dari aplikasi ku terlebih dahulu, terutama _login_ dan _register_ Untuk aplikasi saya, saya ingin menggunakan _vibe_ hijau dan putih, oleh karena itu untuk _login page_, saya mencari gambar furniture dan hiasan no _WaterMark_ dari internet, kemudian saya jadikan sebagai background. Namun, sebelum memulai, saya perlu untuk menambahkan _tailwind_ ke dalam html saya.


    ```bash 
    <head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
    <script src="https://cdn.tailwindcss.com">
    </script>
    </head>
    ```


    Untuk menghias website saya sendiri, saya menggunakan _tailwind_ karena dengan _tailwind_, ada beberapa tampilan yang sudah tersedia seperti icon panah, tong sampah, pensil, dan lainnya. Setelah menemukan _UI_ yang bagus untuk _login page_ saya, saya tinggal menerapkan _style_ yang sama pada _register page_ nya.


   
    ![image](https://github.com/user-attachments/assets/8862eeb4-d433-4665-9c2d-1d57a8f5e0e9)



    Sesuai gambar tersebut, saya menggunakan foto dan _vibe_ putih hijau, _style_ ini pun juga ku implementasikan pada fitur edit dan tambah produk. Ada fitur tambahan juga yang ku tambahkan, yaitu tombol kembali untuk kembali ke _main page_ :


    ```bash 
            <div class="absolute top-4 left-4">
            <a href="{% url 'main:main' %}" class="text-green-600 hover:text-green-700 transition">
                <div class="rounded-full bg-white p-2 shadow-lg"> <!-- Tambahkan highlight putih -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M15 19l-7-7 7-7" /> <!-- Garis lebih tebal stroke-width="4" -->
                    </svg>
                </div>
            </a>
        </div>
    ```

    dengan kode diatas, aku membuat tombol panah kembali di bagian kiri atas buat dan edit produk untuk kembali ke _main page_. Setelah itu, saya lanjut untuk membuat _Navigation bar_ pada atas aplikasi.  


    
    <details>
    <summary>kode Navigation Bar</summary>



    ```bash 
        <nav class="bg-green-600 shadow-lg fixed top-0 left-0 z-40 w-full">
    <div class="flex items-center justify-between px-4 sm:px-6 lg:px-8 h-16">
        
        <!-- Bagian kiri: Logo dan Nama Goodsify -->
        <div class="flex items-center space-x-4">
        <a href="#">
            <img src="https://i.ibb.co/xCD2HDR/Whats-App-Image-2024-10-01-at-11-23-06-37c90e89-removebg-preview.png" alt="Goodsify Logo" class="h-12 w-12 mr-1">
        </a>
        <h1 class="text-3xl font-bold text-white">Goodsify</h1>
        </div>

        <!-- Tombol Hamburger untuk mobile -->
        <button class="md:hidden block text-white focus:outline-none mobile-menu-button">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
        </button>

        <!-- Bagian tengah: Links lainnya (hanya tampil di desktop) -->
        <div class="hidden md:flex items-center space-x-8 flex-grow justify-center">
        <a href="#" class="text-white font-bold hover:text-gray-300">Cart</a>
        <a href="#" class="text-white font-bold hover:text-gray-300">Contact</a>
        <a href="#" class="text-white font-bold hover:text-gray-300">Download Goodsify App</a>
        <a href="#" class="text-white font-bold hover:text-gray-300">About</a>
        </div>

        <!-- Bagian kanan: Logout -->
        <div class="hidden md:flex items-center space-x-4">
        <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
        </a>
        </div>
        
    </div>

    <!-- Mobile menu (disembunyikan secara default) -->
    <div class="mobile-menu hidden md:hidden flex flex-col space-y-2 px-4 py-2 bg-green-600">
        <a href="#" class="block text-white font-bold hover:text-gray-300">Cart</a>
        <a href="#" class="block text-white font-bold hover:text-gray-300">Contact</a>
        <a href="#" class="block text-white font-bold hover:text-gray-300">Download Goodsify App</a>
        <a href="#" class="block text-white font-bold hover:text-gray-300">About</a>
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
        Logout
        </a>
    </div>

    <script>
        const btn = document.querySelector(".mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");

        btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
        });
    </script>
    </nav>

    ```
    </details>


    Kemudian, saya juga menambahkan _viewport_ agar webnya menjadi responsif pada _mobile_ dan _desktop_. 
    

    ```bash
    <head>
        {% block meta %}
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
    </head>
    ```


    dengan menggunakan viewport, maka ketika web di perkecil hingga seukuran HP, maka navigation bar dapat mengecil dan menampilkan menu hamburger.


    ![image](https://github.com/user-attachments/assets/1ce3412d-f167-4c06-824c-e2f79a28d6cf)



3. **Menampilkan Produk**

    Untuk menampilkan produk, saya menggunakan 2 file html, yaitu `main.html` dan `card_product.html`. Pertama tama, saya membuat file `card_product.html` terlebih dahulu. `card_product` ini berisi informasi terkait _models_ yang ada di produk yang saya buat seperti nama, deskripsi, harga, dan lain lain.


    <details>
    <summary>kode card_product</summary>

    ```bash
    <div class="bg-white shadow-lg rounded-lg overflow-hidden mb-4"> <!-- Hapus w-64 untuk fleksibilitas lebar -->
    <!-- Menampilkan Gambar dari URL -->
    <div class="bg-gray-200 h-48 flex items-center justify-center">
        {% if Product.image_url %}
        <img src="{{ Product.image_url }}" alt="{{ Product.name }}" class="object-cover h-full w-full">
        {% else %}
        <div class="w-full h-full bg-gray-300"></div> <!-- Placeholder gambar jika tidak ada URL gambar -->
        {% endif %}
    </div>

    <!-- Informasi Produk -->
    <div class="p-4">
        <h3 class="font-bold text-lg text-gray-800 mb-2">{{ Product.name }}</h3> <!-- Nama Produk -->
        <p class="text-gray-600 mb-2">Rp.{{ Product.price }}</p> <!-- Harga Produk -->

        <!-- Lokasi dinamis berdasarkan field city -->
        <p class="text-sm text-gray-500 mb-2">Kota {{ Product.city }}</p>

        <!-- Rating Produk -->
        <div class="flex items-center mb-2">
        <svg class="w-5 h-5 text-yellow-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2l2.9 8.1h8.5L15.5 13l2.9 8.1L12 17 8.6 21.1 11.5 13 3.1 10.1h8.5L12 2z" />
        </svg>
        <span class="ml-2 text-gray-700">{{ Product.rating }}</span>
        </div>
    </div>

    <!-- Buttons Edit & Delete -->
    <div class="flex justify-end p-2 space-x-2">
        <a href="{% url 'main:edit_product' Product.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
        </a>
        <a href="{% url 'main:delete_product' Product.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        </a>
    </div>
    </div>

    ```
    </details> 


    Pertama tama, saya menampilkan gambar dengan _link online_ yang saya masukkan sebagai salah satu atribut dari produk saya, lalu untuk bagian dari informasi produk akan saya tuliskan secara singkat dan hanya sebagian, yaitu nama, harga, kota, dan rating. Saya berencana untuk menampilkan deskripsi hanya ketika kartunya sudah dipencet, namun itu mungkin akan saya lakukan di tugas selanjutnya. Nah, tidak hanya menampilkan produk, saya juga menambahkan tombol edit dan hapus pada kartunya.


    ```bash
    <!-- Buttons Edit & Delete -->
    <div class="flex justify-end p-2 space-x-2">
        <a href="{% url 'main:edit_product' Product.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
        </a>
        <a href="{% url 'main:delete_product' Product.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        </a>
    </div>

    ```


    Ketika tombolnya dipencet, maka dia akan mengarahkan ke page `create_product` dan `edit_product`. Nah di page tersebut juga aku sudah menyambungkannya ke function `delete_product` dan `add_produk` yang ada di dalam `views.py`. Jadi, ketika tombol dipencet, kita akan mengisi form tentang informasi produk, dan katika kita selesai, infromasinya akan ditampilkan pada  `card_product.html`. Nah, saya kurang suka nih kalau tidak ada gambar apa apa ketika masih belum ada produk yang ditambahkan, jadi aku mau menambahkan gambar _static_ ketika produk masi kosong. 


    Pertama tama, saya menambahkan `static` pada `settings.py`


    ```bash
    ...
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'
    ...
    ```

    Pada page html yang menggunakan gambar _static_, saya menambahkan `{% load static %}` agar dapat mengambil gambar _static_ tersebut. Kemudian, saya membuat folder bernama `static/image` yang isinya saya masukkan gambar emoticon sedih. Nah, kemudian, saya buat jika tidak ada produk, emoticon tersebut akan ditunjukkan.
    

    ```bash
        {% if not Products %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-400 mt-4">Belum ada data Produk pada Goodsify.</p> <!-- Teks abu -->
    </div>

    ```
    ![image](https://github.com/user-attachments/assets/1e4673d1-16cb-44ea-b94d-70632d7dd21b)




### urutan prioritas pengambilan CSS selector 

Berikut ini adalah tingkatan prioritas CSS Selector dari yang paling rendah ke paling tinggi (no 1 dijalankan paling terakhir):

1. **Selector tipe elemen (Type Selector):**

    elektor ini langsung mengacu pada nama elemen HTML, seperti `div`, `p`, `h1`, dan sebagainya. Ini memiliki prioritas yang paling rendah.

2. **Selector kelas (Class Selector):**

    Selektor ini menggunakan tanda titik `(.)` diikuti dengan nama kelas, seperti `.menu`, `.header`, dan sebagainya. Prioritasnya lebih tinggi dibandingkan selektor tipe elemen.

3. **Selector atribut (Attribute Selector):**

    Selektor ini mengacu pada atribut tertentu dalam elemen HTML, seperti `[type="text"]`. Ini memiliki prioritas yang sama dengan kelas.

4. **Selector ID (ID Selector):**

    Selektor ini menggunakan tanda pagar `(#)` diikuti dengan nama ID, seperti `#header`. Prioritasnya lebih tinggi dari kelas atau atribut.

5. **Selector inline (Inline Style):**

    Jika gaya diterapkan langsung ke elemen HTML menggunakan atribut `style`, seperti `<div style="color: red;">`. Ini memiliki prioritas yang sangat tinggi.

6. **Penting (Important):**

    Aturan CSS yang memiliki deklarasi `!important`, seperti` color: red` `!important;`, akan mengesampingkan semua aturan lain, kecuali ada deklarasi `!important` lain dengan spesifisitas yang lebih tinggi.
  

### Alasan _responsive design_ penting dan contoh aplikasi yang sudah dan belum menerapkannya

_Responsive design_ penting dalam pengembangan aplikasi web karena semakin beragamnya perangkat yang digunakan untuk mengakses situs atau aplikasi web. Pengguna menjadi bisa mengakses konten web tidak hanya dari komputer desktop, tetapi juga dari tablet, smartphone, hingga perangkat lain dengan berbagai ukuran layar. Berikut ini alasan _responsive design_ penting:

1. **Pengalaman Pengguna yang Konsisten**  
    Responsive design memastikan tampilan dan fungsionalitas situs tetap nyaman di berbagai perangkat, sehingga pengguna tidak terganggu oleh masalah layout atau navigasi.

2. **Mengurangi Bounce Rate**  
    Situs yang responsif lebih mudah dinavigasi di perangkat seluler, sehingga pengunjung cenderung tinggal lebih lama di situs.

3. **Meningkatkan SEO**  
    Google mengutamakan situs responsif dalam hasil pencarian, khususnya di perangkat mobile.

4. **Efisiensi Pengembangan**  
    Dengan responsive design, cukup satu versi situs yang bekerja di berbagai perangkat, sehingga lebih efisien dalam pengembangan dan pemeliharaan.

5. **Siap untuk Teknologi Baru**  
    Responsive design membuat situs mudah beradaptasi dengan perangkat baru tanpa perubahan besar.

**Aplikasi yang menggunakan _responsive design_:**

    1. Whatsapp
    2. Discord
    3. Spotify

**Aplikasi yang belum menggunakan _responsive design_**

    1. Craiglist
    2. DJP online
    3. SIMPKB


### perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiganya

1. **Margin**

    Margin adalah ruang di luar elemen yang memisahkan elemen tersebut dengan elemen lain di sekitarnya. Margin mempengaruhi jarak antar elemen di luar batas elemen tersebut. Margin dapat diatur secara individual untuk setiap sisi (atas, kanan, bawah, kiri) atau sekaligus.

    ```bash
        div {
    margin: 10px; /* Semua sisi akan memiliki margin 10px */
    }

    div {
    margin-top: 10px; /* Hanya bagian atas yang memiliki margin 10px */
    margin-right: 20px;
    margin-bottom: 10px;
    margin-left: 20px;
    }
    ```

2. **Border**

    Border adalah garis di sekitar elemen yang membentuk batas luar elemen. Border ini dapat memiliki berbagai ketebalan, warna, dan gaya (misalnya, solid, dashed, atau dotted).Border dapat diatur untuk satu atau semua sisi elemen.

    ```bash
    div {
    border: 2px solid black; /* Border hitam dengan ketebalan 2px */
    }

    div {
    border-top: 1px dashed red; /* Hanya border atas yang berwarna merah dengan gaya dashed */
    }
    ```

3. **Padding**

    Padding adalah ruang di dalam elemen yang memisahkan konten elemen dari border. Padding membuat jarak antara konten elemen (seperti teks atau gambar) dengan batas elemen. Padding juga dapat diatur untuk setiap sisi atau secara keseluruhan.

    ```bash
    div {
    padding: 15px; /* Padding 15px untuk semua sisi */
    }

    div {
    padding-top: 10px; /* Padding untuk sisi atas */
    padding-right: 20px;
    padding-bottom: 10px;
    padding-left: 20px;
    }
    ```

### flex box dan grid layout beserta kegunaannya

1. **Flex box (Flexible Box Layout)**
    Flexbox adalah metode layout CSS yang digunakan untuk mengatur elemen secara dinamis dalam baris atau kolom. Flexbox memungkinkan kita untuk mengubah ukuran dan posisi antar elemen secara fleksibel. Flexbox sangat berguna untuk membuat layout yang fleksibel, seperti menyejajarkan elemen secara horizontal atau vertikal, membuat elemen memiliki ukuran dinamis, dan mendistribusikan elemen dengan mudah di dalam suatu kontainer.

    Contoh Implementasinya :
    ```bash
    .container {
    display: flex; /* Mengaktifkan flexbox */
    justify-content: center; /* Menyejajarkan elemen secara horizontal ke tengah */
    align-items: center; /* Menyejajarkan elemen secara vertikal ke tengah */
    }

    .item {
    flex: 1; /* Elemen akan fleksibel dan mengisi ruang yang tersedia */
    }
    ```

    **Kegunaan Flexbox**

    1. Membuat menu atau navigasi
    2. Mengatur ukuran dan posisi elemen
    3. Mengurutkan Elemen
    4. Menjadikan Elemen Fleksibel
    5. Membuat tata letak kolom yang responsif
    6. Membuat grid sederhana

2. **Grid Layout**

    Grid layout adalah sistem tata letak dua dimensi yang memungkinkan pembuatan grid yang terdiri dari baris dan kolom. Grid layout memungkinkan pengaturan elemen lebih kompleks dibandingkan dengan flexbox, karena  dapat mengatur elemen dalam bentuk kisi. Grid layout sangat cocok untuk membuat desain yang lebih kompleks, seperti layout halaman penuh, di mana kalian perlu membagi halaman menjadi beberapa bagian (header, sidebar, konten utama, footer) dengan presisi yang lebih baik.

    **Kegunaan Grid Layout**

    1. Membuat tata letak dua dimensi (Baris dan Kolom)
    2. Mengatur posisi elemen secara presisi
    3. Membangun layout responsif
    4. Membuat design yang konsisten
    5. Mengatur ukuran kolom dan baris
    6. Membuat galeri atau dashboard

    **Perbedaan Layout Grid dan Flexbox**
    
    | Aspek                     | Grid Layout                                                                 | Flexbox                                                              |
    |---------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
    | **Dimensi**                | Dua dimensi (baris dan kolom)                                                | Satu dimensi (baris atau kolom)                                       |
    | **Penggunaan Utama**       | Tata letak yang lebih kompleks (misalnya halaman penuh, dashboard)           | Tata letak elemen yang fleksibel dan sederhana                        |
    | **Penempatan Elemen**      | Posisi elemen dapat ditempatkan secara presisi di grid                       | Elemen disusun secara otomatis dalam satu arah (horizontal atau vertikal) |
    | **Responsif**              | Responsif, tetapi pengaturan lebih manual dibanding flexbox                  | Sangat responsif, mudah beradaptasi dengan berbagai ukuran layar       |
    | **Sederhana atau Kompleks**| Kompleks dan fleksibel untuk tata letak yang presisi                        | Sederhana untuk tata letak elemen dinamis dan fleksibel               |
    | **Penataan Elemen**        | Menata elemen dalam bentuk grid yang presisi                                | Menata elemen secara otomatis dalam satu baris atau kolom             |
    | **Kegunaan Utama**         | Membagi area halaman dengan struktur grid yang teratur                      | Menata elemen dalam satu dimensi secara fleksibel                     |



</details>
