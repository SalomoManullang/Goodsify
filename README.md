**Proses Pembuatan Projek Django "Goodsify"**

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
   - Windows:
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
