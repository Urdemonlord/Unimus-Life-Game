# Sprite Bu Ratna (ibu kos, batik ungu) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/bu_ratna_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      bu-ratna-batik-v2.png, bu-ratna-tertawa-v2.png,
#      bu-ratna-sedih-v2.png, bu-ratna-kaget-v2.png
#   3. Timpa game/images/characters/bu_ratna.png dengan
#      bu-ratna-batik-v2.png.
#      PENTING: script.rpy lama masih punya "image bu_ratna" yang menunjuk
#      ke bu_ratna.png (dulu cuma siluet ungu placeholder), dan script.rpy
#      dimuat SETELAH file ini, jadi kalau bu_ratna.png tidak ditimpa,
#      "show bu_ratna" akan menampilkan siluet ungu lama (zoom 1.0).
#      Definisi dasar "image bu_ratna" sengaja TIDAK ditulis di file ini
#      karena akan kalah dengan script.rpy; pakai atribut saja
#      (show bu_ratna batik) yang sudah ber-zoom 0.80.
#
# Sprite lama Bu Ratna cuma siluet ungu dengan label "Bu Ratna", jadi
# desainnya dibuat dari nol mengikuti perannya: ibu kos, hangat tapi
# tegas soal bayar kos dan kebersihan. Rambut gelap disanggul rendah,
# senyum keibuan, batik ungu gelap (mengambil warna siluet lamanya),
# hijab ungu gelap menutupi rambut dan leher, senada dengan batiknya
# (perintah Arya 2026-11-16 21:14 WIB; v1 tanpa hijab sudah diganti v2).
# rok panjang gelap, sepatu flat hitam.
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# semua karakter lain). Zoom sudah menempel di definisi gambar, jadi
# di scene cukup tulis: show bu_ratna tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image bu_ratna batik:
    "images/characters/bu-ratna-batik-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image bu_ratna tertawa:
    "images/characters/bu-ratna-tertawa-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image bu_ratna sedih:
    "images/characters/bu-ratna-sedih-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image bu_ratna kaget:
    "images/characters/bu-ratna-kaget-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image bu_ratna marah:
    "images/characters/bu-ratna-marah-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image bu_ratna kemeja:
    "images/characters/bu-ratna-kemeja-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image bu_ratna kebaya:
    "images/characters/bu-ratna-kebaya-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
