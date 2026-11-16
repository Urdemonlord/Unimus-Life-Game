# Sprite Sari (kakak tingkat + asdos, cardigan hijau) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/sari_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      sari-cardigan-v1.png, sari-tertawa-v1.png, sari-sedih-v1.png,
#      sari-kaget-v1.png
#   3. Timpa game/images/characters/sari.png dengan sari-cardigan-v1.png.
#      PENTING: script.rpy lama masih punya "image sari" yang menunjuk
#      ke sari.png (dulu cuma siluet oranye placeholder), dan script.rpy
#      dimuat SETELAH file ini, jadi kalau sari.png tidak ditimpa,
#      "show sari" akan menampilkan siluet oranye lama (zoom 1.0).
#      Definisi dasar "image sari" sengaja TIDAK ditulis di file ini
#      karena akan kalah dengan script.rpy; pakai atribut saja
#      (show sari cardigan) yang sudah ber-zoom 0.80.
#
# Sprite lama Sari cuma siluet oranye dengan label "Sari", jadi desainnya
# dibuat dari nol mengikuti perannya: kakak tingkat yang jadi asdos,
# hangat dan rapi. Rambut hitam panjang diikat ekor kuda, TANPA hijab,
# biar langsung beda dari Rina dan Kirana. Cardigan hijau sage di atas
# kemeja putih, rok panjang abu-abu gelap, sepatu flat hitam.
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# Nata, Rina, Kirana, Joko, dan Yosep). Zoom sudah menempel di definisi
# gambar, jadi di scene cukup tulis: show sari tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image sari cardigan:
    "images/characters/sari-cardigan-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image sari tertawa:
    "images/characters/sari-tertawa-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image sari sedih:
    "images/characters/sari-sedih-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image sari kaget:
    "images/characters/sari-kaget-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image sari marah:
    "images/characters/sari-marah-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image sari almet:
    "images/characters/sari-almet-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image sari kemeja:
    "images/characters/sari-kemeja-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
