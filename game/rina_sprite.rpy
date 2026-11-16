# Sprite Rina (hijab putih + almet navy, KACAMATA bulat) + 4 ekspresi.
# Install:
#   1. Salin file ini ke game/rina_sprite.rpy
#   2. Salin 5 file PNG dari folder sprites/ ke game/images/characters/:
#      rina-almet-hijab-v1.png, rina-tertawa-v1.png, rina-sedih-v1.png,
#      rina-marah-v1.png, rina-kaget-v1.png
#   3. Timpa game/images/characters/rina.png dengan
#      rina-almet-hijab-v1.png (sprite lama diganti, supaya `show rina`
#      yang dipakai rute lama langsung tampil baru).
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# Nata). Zoom sudah menempel di definisi gambar, jadi di scene cukup
# tulis: show rina tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image rina almet:
    "images/characters/rina-almet-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image rina tertawa:
    "images/characters/rina-tertawa-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image rina sedih:
    "images/characters/rina-sedih-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image rina marah:
    "images/characters/rina-marah-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image rina kaget:
    "images/characters/rina-kaget-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image rina kemeja:
    "images/characters/rina-kemeja-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image rina bomber:
    "images/characters/rina-bomber-kacamata-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
