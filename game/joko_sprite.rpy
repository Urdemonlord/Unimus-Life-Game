# Sprite Joko (hoodie biru, pendiam) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/joko_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      joko-hoodie-v2.png, joko-tertawa-v2.png, joko-sedih-v2.png,
#      joko-kaget-v2.png
#   3. Timpa game/images/characters/joko.png dengan joko-hoodie-v2.png.
#      PENTING: script.rpy lama masih punya "image joko" yang menunjuk
#      ke joko.png, dan script.rpy dimuat SETELAH file ini, jadi kalau
#      joko.png tidak ditimpa, "show joko" akan menampilkan sprite
#      lama (setengah badan, ada tulisan "Joko", zoom 1.0).
#      Definisi dasar "image joko" sengaja TIDAK ditulis di file ini
#      karena akan kalah dengan script.rpy; pakai atribut saja
#      (show joko hoodie) yang sudah ber-zoom 0.80.
#
# Joko itu Andi yang diganti nama (Arya, 2026-11-16). v1 pakai peci
# hitam dari sprite lama; v2 pecinya DIHILANGKAN atas perintah Arya,
# diganti rambut hitam pendek. Jenggot tipis dan hoodie biru-putih
# dipertahankan dari sprite lama (tulisan "Andi" dan logonya dibuang).
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# Nata, Rina, dan Kirana). Zoom sudah menempel di definisi gambar, jadi
# di scene cukup tulis: show joko tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image joko hoodie:
    "images/characters/joko-hoodie-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image joko tertawa:
    "images/characters/joko-tertawa-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image joko sedih:
    "images/characters/joko-sedih-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image joko kaget:
    "images/characters/joko-kaget-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image joko marah:
    "images/characters/joko-marah-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image joko almet:
    "images/characters/joko-almet-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image joko kemeja:
    "images/characters/joko-kemeja-v2.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
