# Simple Sundanese Translator
Program translasi Indonesia - Sunda dan Sunda - Indonesia sederhana mengggunakan _pattern matching_

## Prasyarat
Dalam pengembangan program ini, dibutuhkan:
1. __Python 3.x__  

## Cara Menggunakan
Cara menggunakan program ini adalah sebagai berikut:  

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Spesifikasi
Buatlah dalam bahasa pemrograman Python, program penerjemah sederhana yang memanfaatkan algoritma String Matching (Knuth-Morris-Pratt(KMP), Boyer-Moore(BM), dan Regex), dengan spesifikasi sebagai berikut.
1. Program mampu membaca kata atau kalimat yang akan diterjemahkan.
2. Program akan membaca file eksternal yang berisi vocabulary Bahasa Sunda - Bahasa Indonesia (file sudah disiapkan dalam repository).
3. Program akan melakukan penerjemahan secara perkata (untuk contoh akan ditampilkan di bawah).
4. Program dapat memilih mau "Bahasa Sunda ke Bahasa Indonesia" atau "Bahasa Indonesia ke Bahasa Sunda".
5. Pada saat penerjemahan "Bahasa Sunda ke Bahasa Indonesia", program mampu mengenali kata yang tidak memiliki arti (stopwords), seperti "teh" sehingga dapat diabaikan saat penerjemahan.
6. Pada saat penerjemahan "Bahasa Indonesia ke Bahasa Sunda", program mampu menambahkan kata untuk penekanan kalimat, seperti "teh".
7. Program dapat menampilkan hasil terjemahan.
8. Program dibuat secara individu.
9. Peserta akan mendapatkan nilai bonus jika mengimplementasikan dalam web (untuk bahasanya dibebaskan).
10. Dilarang meng-copy source code program yang sudah jadi, untuk source code algoritma string matching dipersilahkan menggunakan source code dari tugas yang sudah pernah dibuat (Tugas Kecil 4).
11. Batas pengerjaannya adalah 6 Juni 2020.

## Contoh Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

## Pengumpulan
1. Lakukan merge request dari hasil fork kalian ke repository ini
2. Untuk demonya, silahkan membuat video demo penggunaan programnya, diupload ke YouTube dan sertakan linknya pada Readme.

### **_(Ubah file README ini pada repository hasil fork kalian)_**
