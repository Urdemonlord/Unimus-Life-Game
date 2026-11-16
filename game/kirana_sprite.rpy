# Sprite Kirana (hijab navy + bomber navy, ekspresi ceria) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/kirana_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      kirana-bomber-v1.png, kirana-tertawa-v1.png, kirana-sedih-v1.png,
#      kirana-kaget-v1.png
#
# Kirana itu Momogi yang diganti nama (Arya, 2026-11-16). Bedanya dari
# Rina: hijab navy (Rina putih), jaket bomber kasual (Rina blazer almet),
# karena Kirana anaknya rame dan nongkrong di angkringan, bukan di perpus.
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# Nata dan Rina). Zoom sudah menempel di definisi gambar, jadi di scene
# cukup tulis: show kirana tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.
#
# PENEMPATAN DI ANGKRINGAN: jangan di tengah (xalign 0.5) karena di
# situ ada gerobak, jadi dia kelihatan nempel di dalam gerobak, ambigu
# penjual atau pembeli. Geser ke kanan, ke area lesehan (xalign 0.78):
#   show kirana:
#       xalign 0.78
#       yalign 1.0
# Jangan tulis zoom di blok show itu, karena zoom dari definisi gambar
# ikut nempel dan jadi dobel (0.80 x 0.80 = dia mengecil).

image kirana:
    "images/characters/kirana-bomber-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana bomber:
    "images/characters/kirana-bomber-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana tertawa:
    "images/characters/kirana-tertawa-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana sedih:
    "images/characters/kirana-sedih-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana kaget:
    "images/characters/kirana-kaget-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana marah:
    "images/characters/kirana-marah-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana almet:
    "images/characters/kirana-almet-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image kirana kemeja:
    "images/characters/kirana-kemeja-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
