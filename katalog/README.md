# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Dipa Alhaza (NPM 2106751543)
Link Deploy: [https://tugas2pbp-dipa.herokuapp.com/](https://tugas2pbp-dipa.herokuapp.com/)

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Bagan _request client_ 

![image bagan](photo/Beige%20Colorful%20Minimal%20Flowchart%20Infographic%20Graph.png)

penjelasan:

1. User menggunakan Web browser untuk memberikan request berupa URLconf 
2. Django secara default akan mengecek permintaan user pada `usrls.py`.
3. `urls.py`, digunakan sebagai tempat untuk mengarahkan atau memilih View `views.py` sesuai yang diminta.
4. Pada View, jika dibutuhkan data dari database, maka `views.py` akan meminta data (QuarySet) 
   via Model `models.py` yang akan melakukan transaksi data pada Database.
5.	Setelah Model `models.py`  mendapatkan data dari Database akan memberikan respon data kepada View  `views.py`.
6.	view akan memilih Template (Webpage / `html`), jika template tersebut membutuhkan data, View akan mengirimkan 
   data yang sudah diambil dari Model `models.py` untuk dapat digunakan pada template.
   Fungsi View sebagai penghubung antara Model dan Template.
7.	Template `html` akan ditampilkan berupa Webpage kepada USER.



##  kenapa menggunakan virtual environment?


_Virtual environment_ digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Secara sederhana, _virtual environment_ digunakan untuk menjaga versi tools atau eksternal library yang di-_install_ untuk suatu proyek kerja , sehingga ketika terjadi _update version_ (bisa perubahan fitur atau sintaks, sejenisnya) terhadap library tersebut, project django akan tetap berjalan dengan _version apps_  yang tersimpan di _virtual environment_. 


## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Project django dapat berjalan tanpa _virtual environment_ '`Env`. Env hanya menjaga version django pada project django kita, jika mau membuat proyek django secara lokal, cukup memastikan bahwa django sudah terinstall pada _environment_ lokal. Namun, `Env` sangat membantu dalam pengembangan proyek yang django yang memiliki host dimana proyek tersebut harus di-_deploy_ ke suatu platform, `Env` dapat menampung `requirements.txt`, yang menyimpan data _tools_ yang digunakan untuk membantu penyusunan Web tersebut.


## Penjelasan cara implementasi template program tugas-2 PBP

1.	Membuat repository dengan mengambil template yang sudah ada, kemudian di-_remote_ ke lokal repositori.
2.	Pada file `views.py`, buat fungsi untuk me-_return_ _request_ url dengan mengarahkan pada file `katalog.html` 
   sekaligus memberikan data field yang diambil pada file (database) di folder `fixtures`.
3.	Melakukan routing untuk memetakan fungsi yang telah dibuat pada `views.py` dengan menambahkan path di file `urls.py` 
   (pada folder katalog dan juga project_django[main url]).
4.	Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template dengan membuat kelas di file `models.py`.
   (pada template yang dikasih, sudah dibuat class untuk pemetaannya).
5.	lakukan _migrate_ untuk membuat skema model yang nantinya dapat diakses oleh html.

   Dengan cara:
   Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal. 
   Jalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

6.	Edit file `katalog.html` sesuai kebutuhan.

7.	Dalam proses deploy, pertama, buat apps baru di HEROKU, dan melakukan deploy dari fitur yang ada di web HEROKU, 
   dengan membuat koneksi ke repositori github.

8.	Cara deploy lain, yang juga dapat digunakan [tutorial deploy lab 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0#tutorial-melakukan-deploy-aplikasi-django-ke-heroku)

