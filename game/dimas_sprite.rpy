# Sprite Dimas (teman sekos yang jago masak, flanel merah) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/dimas_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      dimas-flanel-v1.png, dimas-tertawa-v1.png, dimas-sedih-v1.png,
#      dimas-kaget-v1.png
#   3. Timpa game/images/characters/dimas.png dengan dimas-flanel-v1.png.
#      PENTING: script.rpy lama masih punya "image dimas" yang menunjuk
#      ke dimas.png (dulu cuma siluet hijau tosca placeholder), dan
#      script.rpy dimuat SETELAH file ini, jadi kalau dimas.png tidak
#      ditimpa, "show dimas" akan menampilkan siluet hijau lama (zoom 1.0).
#      Definisi dasar "image dimas" sengaja TIDAK ditulis di file ini
#      karena akan kalah dengan script.rpy; pakai atribut saja
#      (show dimas flanel) yang sudah ber-zoom 0.80.
#
# Sprite lama Dimas cuma siluet hijau tosca dengan label "Dimas", jadi
# desainnya dibuat dari nol mengikuti perannya: teman sekos yang jago
# masak dan santai. Rambut hitam pendek acak-acakan, senyum lebar,
# kemeja flanel kotak-kotak merah bata di atas kaos putih polos,
# celana hitam, sneakers gelap.
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# Nata, Rina, Kirana, Joko, Yosep, dan Sari). Zoom sudah menempel di
# definisi gambar, jadi di scene cukup tulis: show dimas tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image dimas flanel:
    "images/characters/dimas-flanel-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image dimas tertawa:
    "images/characters/dimas-tertawa-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image dimas sedih:
    "images/characters/dimas-sedih-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image dimas kaget:
    "images/characters/dimas-kaget-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image dimas marah:
    "images/characters/dimas-marah-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image dimas almet:
    "images/characters/dimas-almet-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image dimas kemeja:
    "images/characters/dimas-kemeja-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
