Dipa Alhaza (NPM 2106751543)

LINK Deploy :

[https://tugas2pbp-dipa.herokuapp.com/todolist](https://tugas2pbp-dipa.herokuapp.com/todolist)



# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Token CSRF adalah token acak yang aman (misalnya, token sinkronisasi atau token tantangan) yang digunakan untuk mencegah serangan CSRF. Token harus unik per sesi pengguna dan harus bernilai acak besar agar sulit ditebak. Sebuah _CSRF secure application_ memberikan token CSRF unik untuk setiap sesi pengguna. Token ini dimasukkan ke dalam parameter tersembunyi dari formulir HTML yang terkait dengan operasi sisi server yang penting. Mereka kemudian dikirim ke browser klien.

Token CSRF dapat mencegah serangan CSRF dengan membuat penyerang tidak mungkin membuat permintaan HTTP yang sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban.

CSRF (_Cross-Site Request Forgery_) adalah sebuah serangan yang membuat pengguna internet  tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. Sehingga, aplikasi tersebut mengeksekusi suatu tindakan yang sebenarnya tidak dikehendaki oleh pengguna internet. Misalnya mengganti foto profil Anda menjadi gambar bebek, menghapus akun secara permanen, atau metransfer uang ke suatu akun. 

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 

Kita dapat membuat `form` secara manual tanpa harus menggunakan form.as_table dengan memanfaatkan fitur yang `form` yang ada pada `HTML`.

##  Penjelasan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.\

1. Pengguna memasukan input melalui laman html, dengan fitur `form` django
2. ketika user submit, maka form akan memberikan perintah `POST` yang bisa kita gunakan sebagai sinyal untuk mengirim data input ke database
2. Data yang dimasukan akan diarahkan sesuai `models` yang dibuat ke database dengan menggunakan fungsi atau method bawaan fitur `form` di django
3. untuk data yang sudah dimasukan ke database, kita dapat membuat fungsi yang mengambil data berdasarkan ketentuan yang dibutuhkan (misal pada program ini, data ditampilkan sesuai dengan user yang login) juga berdasarkan `models` yang dibuat.
4. proses logic memasukan atau menampilkan data tersebut terjadi di `views.py`


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat Apps Django
```shell
python manage.py startapp todolist
```
2. Membuat sebuah model di `model.py` seperti berikut.

![image penjelasan-1](photo/Penjelasan1.jpg)

3. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

4. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

5. meregistrasi models ke admin site django. berikut kodenya.

![image penjelasan-7](photo/Penjelasan7.jpg)

5. membuat laman login, register (sesuai dengan tutorial `lab 3` berupa html), todolist, dan create-task s file di folder Template.

6. Membuat file baru bernama `forms.py` membuat sebuah class yang meng-inhirit ModelsForm untuk membuat custom form django. berikut representasi kodenya.

![image penjelasan-6](photo/Penjelasan6.jpg)


7. membuat fungsi register, login, dan logout sebagai berikut

![image penjelasan-2](photo/Penjelasan2.jpg)

fungsi register -> Untuk membuat sebuah regular akun
fungsi login -> Untuk melakukan login + validasi user login (data user yang login akan di store ke Cookies)
fungsi logout -> untuk keluar dari userlogin


8. membuat fungsi `show_todolist` untuk mengatur tampilan laman yang berisikan todolist user yang login dan fungsi `create-task` untuk mengatur form masukan berupa info task yang kemudian di store ke database. representasi kodenya sebagai berikut.

![image penjelasan-3](photo/Penjelasan3.jpg)


9. membuat fungsi fitur tambahan (bonus) yaitu fungsi `delete_item` untuk menghapus task dan `update_status` untuk membuat perubahan pada status sudah atau belum task dikerjakan.
berikut representasi kodenya.

![image penjelasan-4](photo/Penjelasan4.jpg)


10. mengatur url path di `urls.py`, berikut kodenya.

![image penjelasan-5](photo/Penjelasan5.jpg)


11. Program di push ke github dan deploy ke heroku

# Styling pages

## perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Internal CSS

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

### External CSS

Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

### Inline CSS

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

## Macam-macam TAG HTML
`<!DOCTYPE>`	Tag untuk menentukan tipe dokumen
`<html>`	    Tag untuk membuat sebuah dokumen HTML
`<title>`	    Tag untuk membuat judul dari sebuah halaman
`<body>`	    Tag untuk membuat tubuh dari sebuah halaman
`<h1> to <h6>`	Tag untuk membuat heading
`<p>`	        Tag untuk membuat paragraf
`<br>`	        Memasukan satu baris putus
`<hr>`	        Tag untuk membuat perubahan dasar kata didalam isi
`<!--...-->`	Tag untuk membuat komentar
`<form>`	    Tag untuk membuat sebuah form HTML untuk input pengguna
`<input>`	    Tag untuk membuat sebuah kontrol input
`<textarea>`	Tag untuk membuat sebuah kontrol input multibaris (text area)
`<button>`	    Tag untuk membuat sebuah tombol yang dapat diklik
`<select>`	    Tag untuk membuat sebuah daftar drop-down
`<img>`	        Tag untuk membuat gambar
`<a>`	        Tag untuk membuat hyperlink
`<link>`	    Tag untuk membuat hubungan antara dokumen dan sumber daya eksternal (paling sering digunakan untuk link ke style sheet)
`<nav>`	        Tag untuk membuat navigasi link (tag baru HTML5)
`<style>`	    Tag untuk membuat informasi style untuk dokumen
`<div>`	        Tag untuk membuat sebuah bagian dalam dokumen
`<span>`	    Tag untuk membuat sebuah bagian dalam dokumen
`<header>`	    Tag untuk membuat sebuah header untuk dokumen atau bagian (tag baru HTML5)
`<footer>`	    Tag untuk membuat footer untuk dokumen atau bagian (tag baru HTML5)
`<hgroup>`	    Pengelompokan elemen heading (<h1> sampai <h6>) (tag baru HTML5)
`<section>`	    Tag untuk membuat bagian dalam dokumen (tag baru HTML5)
`<article>`	    Tag untuk membuat sebuah artikel (tag baru HTML5)
`<aside>`	    Tag untuk membuat konten lain selain dari konten halaman (tag baru HTML5)


## Tipe Selector di CSS

1. SeleKtor Tag = Selektor ini akan memilih elemen berdasarkan nama tag.

2. Selektor Class = selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.contohnya `.namaClass`

3.Selektor ID = Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja. Selektor ID ditandai dengan tanda pagar `(#)` di depannya. Contohnya, `#namaId`

4.Selektor Atribut = selektor yang memilih elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag. 
contohnya `input[type=text]`, Artinya kita akan memilih semua elemen `<input>` yang memiliki atribut `type='text'`.

5.Selektor Universal = Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkauan (scope)tertentu dengan menggunakan (`*`).

6. Pseudo Selektor = selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.

Ada dua macam pseudo selektor:

    1. pseudo-class selektor untuk state elemen;
    2.pseudo-element selektor untuk elemen semu di HTML.

## Cara Implementasi Styling Pages

1. copy link CDN Bootstrap, lalu di taruh pada kode HTML (link tersebut di `base.html`).
2. edit tag html di folder template sesuai ketentuan bootstrap.



