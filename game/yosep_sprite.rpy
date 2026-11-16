# Sprite Yosep (rambut coklat + kacamata, aktivis UKM) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/yosep_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      yosep-jaket-v1.png, yosep-tertawa-v1.png, yosep-sedih-v1.png,
#      yosep-kaget-v1.png
#
# Kacamata hitam dan rambut coklatnya dipertahankan dari sprite lama,
# biar langsung beda dari Nata dan Joko. Pecinya TIDAK dipakai (Arya
# sudah dua kali tidak mau kopiah di karakter cowok: Nata dan Joko).
# Jaket navy bergaris putih juga dari sprite lama, cuma tulisan
# "Yosep" di kaosnya sudah dibuang.
#
# Di angkringan, JANGAN tampil di tengah (xalign 0.5): gerobaknya menutupi
# kaki dan dia kebaca seperti penjual di balik gerobak. Selalu berdiri di
# KANAN (xalign 0.78, area lesehan pelanggan), sama seperti aturan Kirana.
# Di dalam show block, yang boleh diubah cuma xalign/yalign, JANGAN zoom.
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# Nata, Rina, Kirana, dan Joko). Zoom sudah menempel di definisi
# gambar, jadi di scene cukup tulis: show yosep tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image yosep:
    "images/characters/yosep-jaket-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep jaket:
    "images/characters/yosep-jaket-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep tertawa:
    "images/characters/yosep-tertawa-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep sedih:
    "images/characters/yosep-sedih-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep kaget:
    "images/characters/yosep-kaget-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep marah:
    "images/characters/yosep-marah-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep almet:
    "images/characters/yosep-almet-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image yosep kemeja:
    "images/characters/yosep-kemeja-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
