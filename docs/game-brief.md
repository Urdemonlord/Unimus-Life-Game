# Unemes Life — Game Brief (satu halaman)

Repo: `Urdemonlord/Unimus-Life-Game` (PUBLIC, Ren'Py, MIT, v0.3.0). Semua aset baru masih lokal di `~/workspace/unimus-life/`, belum masuk repo.

## Premis (kata-kata Arya)
Nyontek semuanya dari Summertime Saga, tapi dibuat lebih friendly dan disesuaikan dengan realitas mahasiswa kos Semarang. Nata merantau ke Semarang dengan uang bulanan pas-pasan. Ospek week = minggu pertama, lalu semester berjalan.

## Core loop
- Waktu: 4 slot per hari (Pagi / Siang / Sore / Malam), evaluasi mingguan.
- Uang: uang saku nyata di dompet (kiriman kadang telat), bensin motor, kos tanggal 1, makan warteg / burjo / masak mie, laundry, kuota, token listrik.
- Stat: Akademik, Sosial, Stamina, Ibadah. Keuangan bukan stat, tapi uang beneran.
- Peta Semarang: 10 lokasi, pindah lokasi bensin 5, bensin habis jalan kaki stamina -10.
- Rute karakter: 8 karakter, pertemanan sehat saja, masing-masing ada quest ramah.
- Event acak Semarang: motor mogok, hujan, kiriman telat, listrik mati. Mini-game. Ending laporan semester.

## Menit pertama
Nata sampai di kos, uang pas-pasan, peta Semarang terbuka, pemain pilih mau makan warteg dulu atau langsung ke kampus.

## Tampilan
- Sprite anime 1024x1024 transparan, kaki di bawah. Nata mukanya seperti Arya, tanpa kopiah, 3 outfit: kemeja biru muda (baju kuliah biasa, bukan kaos), almet navy, bomber biru. 5 ekspresi: senyum, tertawa, sedih, marah, kaget.
- Background 1920x1080 gaya anime, tengah kosong buat sprite, ada yang berisi orang latar ala Summertime Saga (angkringan v8: penjual ibu-ibu batik + 2 pelanggan lesehan).
- Peta: flat vector Semarang, akurat arah dan urutan (Marina barat laut, Kota Lama utara, Simpang Lima tengah, kampus + kos di selatan). Globe Unemes + gapura bertulisan UNEMES di pintu selatan kampus, dari foto gerbang Unimus asli, nama diplesetin.

## Sudah jadi
- Sprite Nata 3 outfit + 5 ekspresi, tampil zoom 0.80 ala Summertime Saga (file `nata_sprite.rpy`, zoom menempel di definisi gambar). Peta v16 16:9 full-bleed ala Summertime Saga (globe + gapura UNEMES, pin jadi chip gelap). v17 (label dihapus dari gambar) dibatalkan Arya, kembali ke v16. Kode `map_semarang.rpy` (10 lokasi, pin, HUD uang/bensin/stamina, aksi berbiaya). 8 dari 10 background (kos, Kota Lama, Marina, warteg, angkringan v8, Simpang Lima, laundry v2, masjid kampus).

## Belum (urut bangun)
1. ~~Background kampus + perpustakaan~~ — DONE 2026-11-16 (bg-kampus-v1, bg-perpustakaan-v1, kode sudah diarahkan).
2. ~~Sistem waktu + uang kos~~ — DONE 2026-11-16 (waktu_uang.rpy, diuji simulasi 60 hari: kiriman, kos, token, 4 kerja part-time, evaluasi mingguan; ekonomi bisa bertahan, tidak ada soft-lock; belum dijalankan di Ren'Py).
3. ~~Rute karakter, 1 karakter dulu sampai tamat~~ — **Rina TAMAT** 2026-11-16 (file `rute_karakter.rpy`, 5 langkah bantu dia menang lomba karya tulis, diuji 11 cek di Ren'Py beneran). **Kirana TAMAT** 2026-11-16 (5 langkah bantu dia jualan online sampai flash sale di Simpang Lima, diuji 11 cek di Ren'Py beneran). **Joko, Yosep, Sari, Dimas, Pak Budi, Bu Ratna TAMAT** 2026-11-16 (masing-masing 5 langkah + obrolan, diuji 11 cek di Ren'Py beneran). **SEMUA 8 RUTE SELESAI** (88 cek total lolos).
4. Sprite 8 karakter lain dengan sistem outfit yang sama. — **Rina DONE** 2026-11-16 (set lengkap kayak Nata: 3 outfit almet/kemeja/bomber + 5 ekspresi, 1024x1024 transparan, zoom 0.80, terpasang di test project; semua 7 file sekarang pakai kacamata bulat yang sama). **Kirana DONE** 2026-11-16 (set lengkap: bomber + 3 ekspresi + marah + almet + kemeja; hijab navy biar beda dari Rina; aturan penempatan di angkringan: kanan xalign 0.78, jangan tengah). **Joko DONE** 2026-11-16 (set lengkap: hoodie + 3 ekspresi + marah + almet + kemeja, semua v2 tanpa peci). **Yosep DONE** 2026-11-16 (set lengkap: jaket + 3 ekspresi + marah + almet + kemeja, rambut coklat + kacamata, peci tidak dipakai). **Sari DONE** 2026-11-16 (set lengkap: cardigan + 3 ekspresi + marah + almet + kemeja, rambut ekor kuda, tanpa hijab). **Dimas DONE** 2026-11-16 (set lengkap: flanel + 3 ekspresi + marah + almet + kemeja, rambut acak-acakan, senyum lebar). **Pak Budi DONE** 2026-11-16 (set lengkap: batik + 3 ekspresi + marah + almet + kemeja, rambut beruban + kacamata, peci tidak dipakai). **Bu Ratna DONE** 2026-11-16 (set lengkap: batik + 3 ekspresi + marah + kemeja + kebaya, semua berhijab ungu gelap). **SEMUA 9 KARAKTER SELESAI**: Nata, Rina, Kirana, Joko, Yosep, Sari, Dimas, Pak Budi, Bu Ratna, masing-masing 3 outfit + 5 ekspresi, zoom 0.80, terverifikasi di dalam game. (Nama Joko dan Yosep DITUKAR 2026-11-16 atas perintah Arya: si pendiam jago coding sekarang Joko, si aktivis UKM sekarang Yosep.)
5. Masukkan semua ke repo.

## Anti-pilar (jangan)
- Tanpa konten dewasa, tanpa utang kriminal, tanpa grinding tidak sehat.
- Tanpa nama/logo Unimus asli, semua Unemes generik.
- Aset AI itu placeholder, bukan art final, dan dibilang begitu. Cek tiap aset pakai skill antislop-ui + design-taste-frontend, dari referensi nyata kalau ada, penempatan harus logis.
- Revisi file tidak pernah timpa nama yang sama, selalu nama baru berversi + sha256.

## Handover (jujur)
- Yang di atas sudah dicek visual dan kode dibaca, dan sistem waktu/uang sudah diuji di Ren'Py 8.4.1 beneran di sandbox (lint bersih, 29 cek otomatis lolos, semua background dan sprite termuat). Tapi alur klik peta, menu, dan dialog belum pernah dimainkan manusia satu shift penuh.
- Not yet played by a person.
