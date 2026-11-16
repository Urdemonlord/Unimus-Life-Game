# Sprite Pak Budi (dosen pembimbing, batik biru) + 3 ekspresi.
# Install:
#   1. Salin file ini ke game/pak_budi_sprite.rpy
#   2. Salin 4 file PNG dari folder sprites/ ke game/images/characters/:
#      pak-budi-batik-v1.png, pak-budi-tertawa-v1.png,
#      pak-budi-sedih-v1.png, pak-budi-kaget-v1.png
#   3. Timpa game/images/characters/pak_budi.png dengan
#      pak-budi-batik-v1.png.
#      PENTING: script.rpy lama masih punya "image pak_budi" yang menunjuk
#      ke pak_budi.png, dan script.rpy dimuat SETELAH file ini, jadi kalau
#      pak_budi.png tidak ditimpa, "show pak_budi" akan menampilkan sprite
#      lama (setengah badan, zoom 1.0). Definisi dasar "image pak_budi"
#      sengaja TIDAK ditulis di file ini karena akan kalah dengan
#      script.rpy; pakai atribut saja (show pak_budi batik) yang sudah
#      ber-zoom 0.80.
#
# Rambut beruban di pelipis dan kacamata hitamnya dipertahankan dari
# sprite lama, biar langsung kebaca sebagai dosen senior dan beda dari
# semua mahasiswa. Pecinya TIDAK dipakai, mengikuti aturan no-kopiah
# yang sudah berlaku buat semua karakter cowok (Nata, Joko, Yosep).
# Batik biru gelap jadi outfit dasarnya, khas dosen; almet dan kemeja
# menyusul sebagai outfit kedua dan ketiga.
#
# Ukuran tampil standar: zoom 0.80 (ala Summertime Saga, sama seperti
# semua karakter lain). Zoom sudah menempel di definisi gambar, jadi
# di scene cukup tulis: show pak_budi tertawa
# Sprite tetap 1024x1024 transparan, kaki di bawah, tengah layar.

image pak_budi batik:
    "images/characters/pak-budi-batik-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image pak_budi tertawa:
    "images/characters/pak-budi-tertawa-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image pak_budi sedih:
    "images/characters/pak-budi-sedih-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image pak_budi kaget:
    "images/characters/pak-budi-kaget-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image pak_budi marah:
    "images/characters/pak-budi-marah-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image pak_budi almet:
    "images/characters/pak-budi-almet-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0

image pak_budi kemeja:
    "images/characters/pak-budi-kemeja-v1.png"
    zoom 0.80
    xalign 0.5
    yalign 1.0
