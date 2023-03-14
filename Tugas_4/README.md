Nama: Ardian

NPM: 2106338173

Project: Tugas 3

1. {% csrf_token %} adalah tag yang digunakan pada Django untuk menambahkan token keamanan pada form HTML dan mencegah terjadinya serangan CSRF. Jika {% csrf_token %} tidak ada pada elemen <form>, maka Django akan menghasilkan error "CSRF verification failed", mencegah pengguna mengirimkan formulir dan menyebabkan masalah di aplikasi web. {% csrf_token %} sangat penting untuk ditambahkan pada setiap elemen <form> pada aplikasi web Django untuk menjaga keamanan data.

2. Kita dapat membuat elemen <form> secara manual tanpa menggunakan generator seperti {{ form.as_table }}. Contohnya adalah pertama kita buat elemen <form> dengan atribut "action" dan "method". Lalu tambahkan elemen input ke dalam elemen <form> dengan atribut "name" dan "value" untuk setiap elemen. Kemudian tambahkan elemen submit ke dalam elemen <form> untuk mengirimkan data ke server. Lalu tambahkan {% csrf_token %} pada elemen <form> untuk mencegah serangan CSRF.

3. Submisi data form HTML melibatkan serangkaian langkah, dimulai dari pengguna mengisi form dan mengklik tombol kirim. Ketika form dikirimkan, data dikirim ke server menggunakan metode POST. Server kemudian memverifikasi token CSRF untuk mencegah serangan CSRF dan memvalidasi data form sesuai dengan aturan validasi yang telah ditentukan. Jika data valid, maka akan disimpan di database. Jika data tidak valid, pesan kesalahan akan ditampilkan kepada pengguna. Setelah data disimpan di database, server mengambil data tersebut dan melewatkan data ke template HTML. Template menggunakan bahasa template untuk menampilkan data dalam format HTML yang sesuai. Akhirnya, halaman web yang dihasilkan dikirim ke browser pengguna untuk ditampilkan.

4. Saya megimplementasikan poin 1-4 dengan cara mengikuti tahap-tahap yang dilakukan di tutorial 3 dengan menyesuaikan permintaan tugas 3 ini. Dan juga, sebelum melaksanakan poin 1-4, saya juga membuat folder khusus Tugas 4 pada repository yang sudah saya buat sebelumnya yaitu repository PBP_Tugas.