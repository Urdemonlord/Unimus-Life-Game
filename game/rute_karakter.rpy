# ------------------------------------------------------------------------- #
#  Rute Karakter (Unemes Life, adaptasi Summertime Saga)
# ------------------------------------------------------------------------- #
#  Cara pasang:
#    1. Salin file ini ke game/rute_karakter.rpy
#    2. Pastikan game/map_semarang.rpy sudah memakai menu
#       "Ngobrol dengan karakter di sini" -> call pilih_karakter_semarang
#    3. Dari cerita, panggil:  call peta_semarang
#
#  Sistemnya (dipakai semua karakter, semua 8 karakter tamat):
#    - kedekatan: 0-100 per karakter. Level: Baru Kenal / Kenalan /
#      Teman Dekat / Sahabat / Gebetan.
#    - tahap_rute: 0-4 = langkah quest, 5 = tamat. Tiap langkah makan
#      1 slot waktu (maju_slot) dan cuma bisa di lokasi yang tepat.
#      Syarat stat yang kurang = ditolak halus, slot tidak terpakai.
#    - Karakter bicara pakai define satu huruf dari script.rpy:
#      e = Nata, r = Rina, s = Sari, d = Dimas, p = Pak Budi,
#      br = Bu Ratna (define satu huruf dari script.rpy).
#      Riwayat nama 2026-11-16 (Arya): Momogi -> Kirana, Andi -> Joko,
#      lalu Joko <-> Yosep DITUKAR: si pendiam jago coding (dulu Yosep)
#      sekarang Joko, si aktivis UKM (dulu Joko) sekarang Yosep.
#      Define lama a/l/j di script.rpy masih bernama Andi/Momogi/Joko,
#      jadi rute baru pakai define sendiri di bawah (kr/ys/jk), bukan a/l/j.
# ------------------------------------------------------------------------- #

default kedekatan = {"rina": 0, "kirana": 0, "joko": 0, "yosep": 0,
                     "sari": 0, "dimas": 0, "pak_budi": 0, "bu_ratna": 0}
default tahap_rute = {"rina": 0, "kirana": 0, "joko": 0, "yosep": 0,
                      "sari": 0, "dimas": 0, "pak_budi": 0, "bu_ratna": 0}
default topik_rina = None
default rina_juara = False
default produk_kirana = None
default kirana_laris = False
default proyek_joko = None
default joko_menang = False
default divisi_yosep = None
default yosep_sukses = False
default tugas_sari = None
default sari_rekomendasi = False
default menu_dimas = None
default dimas_laris = False
default topik_budi = None
default budi_setuju = False
default tugas_ratna = None
default ratna_diskon = False

define kr = Character("Kirana", who_color="#e74c3c")
define jk = Character("Joko", who_color="#2ecc71")
define ys = Character("Yosep", who_color="#1abc9c")

transform sprite_normal:
    zoom 0.80
    xalign 0.5
    yalign 1.0

init python:
    KARAKTER = {
        "rina":     {"nama": "Rina"},
        "kirana":   {"nama": "Kirana"},
        "joko":    {"nama": "Joko"},
        "yosep":     {"nama": "Yosep"},
        "sari":     {"nama": "Sari"},
        "dimas":    {"nama": "Dimas"},
        "pak_budi": {"nama": "Pak Budi"},
        "bu_ratna": {"nama": "Bu Ratna"},
    }

    def level_kedekatan(nilai):
        if nilai >= 80:
            return "Gebetan"
        if nilai >= 60:
            return "Sahabat"
        if nilai >= 40:
            return "Teman Dekat"
        if nilai >= 20:
            return "Kenalan"
        return "Baru Kenal"

    def tambah_kedekatan(kunci, jumlah):
        kedekatan[kunci] = max(0, min(100, kedekatan.get(kunci, 0) + jumlah))


label pilih_karakter_semarang(lokasi):
    $ _chars = LOCATIONS_SEMARANG[lokasi]["characters"]
    $ _pilihan = [(KARAKTER[c]["nama"] + "  (" + level_kedekatan(kedekatan[c]) + ")", c) for c in _chars]
    $ _pilihan.append(("Kembali", None))
    $ _cid = renpy.display_menu(_pilihan)
    if _cid is None:
        return
    if _cid == "rina":
        call ketemu_rina(lokasi)
    elif _cid == "kirana":
        call ketemu_kirana(lokasi)
    elif _cid == "joko":
        call ketemu_joko(lokasi)
    elif _cid == "yosep":
        call ketemu_yosep(lokasi)
    elif _cid == "sari":
        call ketemu_sari(lokasi)
    elif _cid == "dimas":
        call ketemu_dimas(lokasi)
    elif _cid == "pak_budi":
        call ketemu_pak_budi(lokasi)
    elif _cid == "bu_ratna":
        call ketemu_bu_ratna(lokasi)
    else:
        $ renpy.say(None, KARAKTER[_cid]["nama"] + ": \"Eh, Nata! Nanti kita ngobrol lagi ya, aku lagi buru-buru.\" (Rute karakter ini belum dibuat.)")
    return


# --- Rina: teman sekelas, rajin, suka belajar bareng di perpus. ------- #
# Rute: bantu dia lomba karya tulis ilmiah mahasiswa baru (5 langkah).   #
# Langkah 0-2 di Perpustakaan, langkah 3-4 di Kampus (lomba di aula).   #

label ketemu_rina(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show rina at sprite_normal
        r "Nata, kamu kelihatan capek banget. Istirahat dulu, tidur siang di kos itu gratis. Nanti kita ngobrol lagi."
        hide rina
        return
    $ _tahap = tahap_rute["rina"]
    if _tahap < 3 and lokasi != "perpustakaan":
        show rina at sprite_normal
        r "Aku lagi di perpus, Nat. Kalau mau bantuin lombaku, ketemu di sana ya."
        hide rina
        return
    if _tahap >= 3 and _tahap < 5 and lokasi != "kampus_unemes":
        show rina at sprite_normal
        r "Latihan sama lombanya di kampus, Nat. Ketemu di sana ya."
        hide rina
        return
    if _tahap == 0:
        call rina_0
    elif _tahap == 1:
        call rina_1
    elif _tahap == 2:
        call rina_2
    elif _tahap == 3:
        call rina_3
    elif _tahap == 4:
        call rina_4
    else:
        call rina_selesai
    return


label rina_0:
    # Langkah 0: kenalan di perpus. Rina mentok pilih topik lomba.
    show rina at sprite_normal
    r "Eh, ini meja masih kosong kan? Semua meja penuh, aku bawa buku segunung."
    e "Boleh, silakan. Kamu Rina kan? Anak baru sekelas, yang duduk baris depan terus."
    r "Iya! Kamu Nata. Eh, pas banget ketemu kamu. Aku lagi pusing milih topik buat lomba karya tulis."
    r "Lomba karya tulis ilmiah mahasiswa baru. Deadline dua minggu lagi, hadiahnya uang pembinaan sama piala."
    r "Aku pengen nulis soal Semarang, tapi idenya masih ngambang semua."
    e "Aku bantuin deh. Dua kepala lebih gampang daripada satu, apalagi kalau yang satu lagi pusing."
    r "Beneran? Makasih, Nat! Besok kita ketemu di sini lagi ya, kita cari referensi bareng."
    $ tambah_kedekatan("rina", 15)
    $ tahap_rute["rina"] = 1
    $ maju_slot()
    hide rina
    call cek_peristiwa_harian
    return


label rina_1:
    # Langkah 1: cari referensi di perpus. Pilih topik dulu.
    show rina at sprite_normal
    if topik_rina is None:
        r "Jadi, topiknya mau yang mana? Aku sudah nyiapin tiga ide, kamu pilih satu."
        menu:
            "Sampah plastik di Semarang":
                $ topik_rina = "sampah"
            "Transportasi umum buat mahasiswa":
                $ topik_rina = "transportasi"
            "UMKM digital di kampung halaman":
                $ topik_rina = "umkm"
    if topik_rina == "sampah":
        $ _topik = "sampah plastik di Semarang"
    elif topik_rina == "transportasi":
        $ _topik = "transportasi umum buat mahasiswa"
    else:
        $ _topik = "UMKM digital di kampung halaman"
    r "Oke, topiknya [_topik]. Sekarang kita cari jurnalnya. Rak sebelah sana, ayo."
    e "Ketemu dua jurnal bagus. Satu soal data lapangan, satu soal solusi yang sudah dicoba di kota lain."
    r "Ini persis yang aku cari! Kamu jago juga nyari referensi. Tinggal ditulis sekarang."
    $ ospek_tracker.update_stat("academic_potential", 3)
    $ tambah_kedekatan("rina", 10)
    $ tahap_rute["rina"] = 2
    $ maju_slot()
    hide rina
    call cek_peristiwa_harian
    return


label rina_2:
    # Langkah 2: nulis bareng. Syarat: akademik >= 20.
    show rina at sprite_normal
    if ospek_tracker.stats["academic_potential"] < 20:
        r "Nat, tulisan ini lumayan berat. Kejar dulu tugas kuliahmu sampai akademikmu lumayan, nanti kita lanjut nulis bareng ya."
        hide rina
        return
    r "Hari ini kita nulis drafnya. Kamu ketik, aku dikte. Kalau ada kalimat yang aneh, bilang ya."
    e "Bab satu selesai. Bab dua... selesai juga. Ternyata nulis bareng lebih cepat daripada nulis sendirian."
    r "Drafnya sudah jadi! Tinggal diprint buat dibaca ulang. Printnya aku yang bayar, kamu sudah bantu banyak."
    if uang_nata >= 5000:
        $ uang_nata -= 5000
        e "Biar aku yang bayar printnya, Rp5.000 doang. Anggap aja patungan."
        r "Ya sudah, makasih! Nanti kalau menang, aku yang traktir."
    $ ospek_tracker.update_stat("academic_potential", 5)
    $ tambah_kedekatan("rina", 15)
    $ tahap_rute["rina"] = 3
    $ maju_slot()
    hide rina
    call cek_peristiwa_harian
    return


label rina_3:
    # Langkah 3: latihan presentasi di kampus. Syarat: sosial >= 10.
    show rina at sprite_normal
    if ospek_tracker.stats["leadership"] < 10:
        r "Aku masih grogi kalau presentasi. Kamu latihan ngomong dulu di depan teman-teman, biar pede. Nanti kita latihan bareng ya."
        hide rina
        return
    r "Ruang kelas ini kosong, pas buat latihan. Kamu jadi jurinya, tanya yang susah-susah."
    e "Pertanyaan pertama: kenapa topik ini penting buat Semarang? ... Bagus. Kedua: datanya dari mana?"
    r "Aduh, pertanyaanmu lebih susah daripada juri beneran. Tapi sekarang aku jadi pede. Makasih, Nat."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("rina", 15)
    $ tahap_rute["rina"] = 4
    $ maju_slot()
    hide rina
    call cek_peristiwa_harian
    return


label rina_4:
    # Langkah 4: hari lomba di aula. Hasil tergantung akademik.
    scene bg aula
    show rina kaget
    r "Ini dia harinya. Aku deg-degan banget. Kamu duduk di barisan depan ya, biar aku bisa lihat kamu."
    e "Semangat, Rin. Kamu sudah latihan, materinya kuat. Tinggal ngomong seperti waktu latihan."
    show rina almet
    r "Hadirin sekalian, saya Rina, dari Universitas... (presentasi berjalan lancar, juri mengangguk-angguk.)"
    if ospek_tracker.stats["academic_potential"] >= 30:
        show rina tertawa
        r "NATA! AKU JUARA SATU! Hadiahnya Rp500.000! Ini, Rp50.000 buat kamu, uang saku. Sisanya aku tabung."
        r "Tanpa kamu, naskah ini tidak akan jadi. Kamu sahabat terbaikku, Nat."
        $ uang_nata += 50000
        $ rina_juara = True
        $ tambah_kedekatan("rina", 20)
    else:
        show rina sedih
        r "Aku dapat juara harapan. Tidak apa-apa, ini lomba pertamaku, dan naskahnya jadi karena bantuanmu."
        show rina almet
        r "Tahun depan kita coba lagi, dan kita menang. Makasih ya, Nat, kamu sahabat terbaikku."
        $ tambah_kedekatan("rina", 10)
    $ tahap_rute["rina"] = 5
    $ maju_slot()
    hide rina
    call cek_peristiwa_harian
    return


label rina_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show rina at sprite_normal
    if rina_juara:
        r "Pialanya aku taruh di meja belajar, biar ingat terus. Eh, ada lomba lagi bulan depan, ikut bantuin lagi ya?"
    else:
        r "Naskah lomba kemarin aku revisi lagi. Tahun depan kita coba lagi, dan kita menang."
    $ tambah_kedekatan("rina", 2)
    $ maju_slot()
    hide rina
    call cek_peristiwa_harian
    return


# --- Kirana: teman kos sebelah, rame, suka ngajak nongkrong. --------- #
# Rute: bantu dia jualan online sampai flash sale (5 langkah).          #
# Langkah 0-2 di Kos (foto produk, tulis deskripsi, upload),            #
# langkah 3-4 di Simpang Lima (latihan live, hari flash sale).          #
# Kirana ditambahkan ke daftar karakter kos di map_semarang.rpy,       #
# karena dia tetangga sebelah yang sering mampir ke kos Nata.          #

label ketemu_kirana(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show kirana at sprite_normal
        kr "Nata, muka kamu pucat banget. Tidur dulu sana, jualan bisa nunggu. Nanti kita ngobrol lagi."
        hide kirana
        return
    $ _tahap = tahap_rute["kirana"]
    if _tahap < 3 and lokasi != "kos_nata":
        show kirana at sprite_normal
        kr "Urusan jualanku di kos, Nat. Mampir ke kamarku atau ketemu di kos kamu, ya."
        hide kirana
        return
    if _tahap >= 3 and _tahap < 5 and lokasi != "simpang_lima":
        show kirana at sprite_normal
        kr "Live sama flash sale-nya di Simpang Lima, Nat. Ketemu di sana ya."
        hide kirana
        return
    if _tahap == 0:
        call kirana_0
    elif _tahap == 1:
        call kirana_1
    elif _tahap == 2:
        call kirana_2
    elif _tahap == 3:
        call kirana_3
    elif _tahap == 4:
        call kirana_4
    else:
        call kirana_selesai
    return


label kirana_0:
    # Langkah 0: kenalan di kos. Kirana cerita toko online-nya sepi.
    show kirana at sprite_normal
    kr "Eh, tetangga sebelah! Kamu yang baru pindah ke kos Bu Ratna kan? Aku Kirana, kamar ujung."
    e "Iya, aku Nata. Baru seminggu di sini, masih hafalin jalan ke kampus."
    kr "Pas banget ketemu kamu. Aku lagi pusing, Nat. Toko online-ku sepi banget, seminggu cuma laku dua."
    kr "Foto produkku jelek, deskripsinya asal-asalan. Yang beli cuma temanku sendiri, itupun karena kasihan."
    e "Aku bantuin deh. Foto sama nulis deskripsi, gampang. Nanti kita bikin tokomu kelihatan meyakinkan."
    kr "Beneran? Makasih, Nat! Besok kita mulai dari foto produk, di kosku ya. Bawa HP kamu yang kameranya bagus."
    $ tambah_kedekatan("kirana", 15)
    $ tahap_rute["kirana"] = 1
    $ maju_slot()
    hide kirana
    call cek_peristiwa_harian
    return


label kirana_1:
    # Langkah 1: foto produk di kos. Pilih produk dulu.
    show kirana at sprite_normal
    if produk_kirana is None:
        kr "Jadi, produk andalan kita yang mana? Aku sudah siapin tiga, kamu pilih satu yang paling laku."
        menu:
            "Hijab segi empat":
                $ produk_kirana = "hijab"
            "Makanan ringan (basreng)":
                $ produk_kirana = "basreng"
            "Aksesoris (gantungan kunci)":
                $ produk_kirana = "aksesoris"
    if produk_kirana == "hijab":
        $ _produk = "hijab segi empat"
    elif produk_kirana == "basreng":
        $ _produk = "basreng"
    else:
        $ _produk = "gantungan kunci"
    kr "Oke, andalannya [_produk]. Sekarang fotoin yang bagus, Nat. Cari cahaya dari jendela, jangan pakai flash."
    e "Cekrek, cekrek... ini bagus. Yang ini juga. Angle dari samping, biar kelihatan detailnya."
    kr "Wah, beda banget sama fotoku yang dulu! Sekarang tokomu... eh, tokoku kelihatan niat. Tinggal ditulis deskripsinya."
    $ ospek_tracker.update_stat("leadership", 3)
    $ tambah_kedekatan("kirana", 10)
    $ tahap_rute["kirana"] = 2
    $ maju_slot()
    hide kirana
    call cek_peristiwa_harian
    return


label kirana_2:
    # Langkah 2: tulis deskripsi + upload. Syarat: akademik >= 20.
    show kirana at sprite_normal
    if ospek_tracker.stats["academic_potential"] < 20:
        kr "Nat, deskripsi produk ini lumayan susah. Kejar dulu tugas kuliahmu sampai akademikmu lumayan, nanti kita lanjut nulis bareng ya."
        hide kirana
        return
    kr "Hari ini kita nulis deskripsinya. Kamu ketik, aku dikte. Harus meyakinkan, tapi jangan lebay."
    e "Judul... selesai. Deskripsi... selesai juga. Harga, ongkir, stok, semua jelas. Sekarang upload."
    kr "Upload-nya butuh kuota, HP-ku tinggal dikit. Beli kuota dulu, Rp10.000, ya."
    if uang_nata >= 10000:
        $ uang_nata -= 10000
        e "Biar aku yang beli kuotanya, Rp10.000 doang. Anggap aja patungan."
        kr "Ya sudah, makasih! Nanti kalau laris, aku yang traktir."
    $ ospek_tracker.update_stat("academic_potential", 5)
    $ tambah_kedekatan("kirana", 15)
    $ tahap_rute["kirana"] = 3
    $ maju_slot()
    hide kirana
    call cek_peristiwa_harian
    return


label kirana_3:
    # Langkah 3: latihan live jualan di Simpang Lima. Syarat: sosial >= 10.
    show kirana at sprite_normal
    if ospek_tracker.stats["leadership"] < 10:
        kr "Aku masih grogi kalau live. Kamu latihan ngomong dulu di depan teman-teman, biar pede. Nanti kita live bareng ya."
        hide kirana
        return
    kr "Lapangan ini rame, pas buat latihan live. Kamu jadi penontonnya, tanya yang susah-susah."
    e "Pertanyaan pertama: bahannya apa? ... Bagus. Kedua: bisa COD tidak?"
    kr "Aduh, pertanyaanmu lebih susah daripada pembeli beneran. Tapi sekarang aku jadi pede. Makasih, Nat."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("kirana", 15)
    $ tahap_rute["kirana"] = 4
    $ maju_slot()
    hide kirana
    call cek_peristiwa_harian
    return


label kirana_4:
    # Langkah 4: hari flash sale di Simpang Lima. Hasil tergantung sosial.
    scene bg simpang_lima
    show kirana kaget
    kr "Ini dia harinya. Flash sale pertama, aku deg-degan banget. Kamu duduk di depan ya, biar aku bisa lihat kamu."
    e "Semangat, Kir. Kamu sudah latihan, produknya bagus. Tinggal ngomong seperti waktu latihan."
    show kirana
    kr "Halo semua, selamat datang di live kami... (live berjalan lancar, penonton nanya terus, pesanan masuk satu-satu.)"
    if ospek_tracker.stats["leadership"] >= 30:
        show kirana tertawa
        kr "NATA! LARIS MANIS! Flash sale-nya habis dalam sejam! Ini, Rp100.000 buat kamu, bagi hasil. Sisanya aku putar lagi buat stok."
        kr "Tanpa kamu, tokoku masih sepi. Kamu sahabat terbaikku, Nat."
        $ uang_nata += 100000
        $ kirana_laris = True
        $ tambah_kedekatan("kirana", 20)
    else:
        show kirana sedih
        kr "Laku sih, tapi tidak seberapa. Tidak apa-apa, ini flash sale pertamaku, dan tokonya jadi karena bantuanmu."
        show kirana
        kr "Bulan depan kita coba lagi, dan kita laris. Makasih ya, Nat, kamu sahabat terbaikku."
        $ tambah_kedekatan("kirana", 10)
    $ tahap_rute["kirana"] = 5
    $ maju_slot()
    hide kirana
    call cek_peristiwa_harian
    return


label kirana_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show kirana at sprite_normal
    if kirana_laris:
        kr "Tokoku sekarang ramai terus, Nat. Eh, bulan depan ada flash sale lagi, bantuin lagi ya?"
    else:
        kr "Stok bulan depan aku tambah lagi. Flash sale berikutnya kita bikin lebih rame, ya."
    $ tambah_kedekatan("kirana", 2)
    $ maju_slot()
    hide kirana
    call cek_peristiwa_harian
    return


# --- Joko: teman satu jurusan, pendiam, jago coding. ------------------ #
# Rute: kerjain proyek bareng sampai demo (5 langkah).                  #
# Langkah 0-2 di Perpustakaan (ngoding, debug), langkah 3-4 di Kampus  #
# (demo ke teman-teman, hari demo).                                     #

label ketemu_joko(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show joko at sprite_normal
        jk "Nata... kamu kelihatan capek. Tidur dulu. Kode bisa nunggu."
        hide joko
        return
    $ _tahap = tahap_rute["joko"]
    if _tahap < 3 and lokasi != "perpustakaan":
        show joko at sprite_normal
        jk "Aku di perpus, Nat. Kalau mau ngoding bareng, ketemu di sana."
        hide joko
        return
    if _tahap >= 3 and _tahap < 5 and lokasi != "kampus_unemes":
        show joko at sprite_normal
        jk "Demo-nya di kampus, Nat. Ketemu di sana ya."
        hide joko
        return
    if _tahap == 0:
        call joko_0
    elif _tahap == 1:
        call joko_1
    elif _tahap == 2:
        call joko_2
    elif _tahap == 3:
        call joko_3
    elif _tahap == 4:
        call joko_4
    else:
        call joko_selesai
    return


label joko_0:
    # Langkah 0: kenalan di perpus. Joko mentok ngoding sendirian.
    show joko at sprite_normal
    jk "..."
    e "Eh, ini meja masih kosong kan? Kamu Joko, kan? Anak sekelas yang tugas kodingnya selalu paling rapi."
    jk "Iya. Nata."
    e "Kamu lagi bikin apa? Mukanya serius banget."
    jk "Proyek. Aplikasi buat anak kos. Sudah seminggu, mentok di satu bug. Sendirian, susah."
    e "Aku bantuin deh. Dua kepala, dua keyboard. Bug-nya kita cari bareng."
    jk "...Boleh. Besok, di sini lagi. Bawa laptop."
    $ tambah_kedekatan("joko", 15)
    $ tahap_rute["joko"] = 1
    $ maju_slot()
    hide joko
    call cek_peristiwa_harian
    return


label joko_1:
    # Langkah 1: pilih proyek di perpus.
    show joko at sprite_normal
    if proyek_joko is None:
        jk "Proyeknya mau yang mana? Aku sudah siapin tiga ide. Kamu pilih satu."
        menu:
            "Aplikasi cari kos":
                $ proyek_joko = "kos"
            "Website UKM":
                $ proyek_joko = "ukm"
            "Game sederhana":
                $ proyek_joko = "game"
    if proyek_joko == "kos":
        $ _proyek = "aplikasi cari kos"
    elif proyek_joko == "ukm":
        $ _proyek = "website UKM"
    else:
        $ _proyek = "game sederhana"
    jk "Oke. Proyeknya [_proyek]. Aku backend, kamu frontend. Mulai sekarang."
    e "Struktur folder sudah jadi. Besok kita isi fiturnya satu-satu."
    jk "Bagus. Kamu cepat. Tinggal debug-nya sekarang."
    $ ospek_tracker.update_stat("academic_potential", 3)
    $ tambah_kedekatan("joko", 10)
    $ tahap_rute["joko"] = 2
    $ maju_slot()
    hide joko
    call cek_peristiwa_harian
    return


label joko_2:
    # Langkah 2: debug bareng. Syarat: akademik >= 20.
    show joko at sprite_normal
    if ospek_tracker.stats["academic_potential"] < 20:
        jk "Nat, bug ini lumayan berat. Kejar dulu tugas kuliahmu sampai akademikmu lumayan, nanti kita lanjut debug bareng ya."
        hide joko
        return
    jk "Hari ini kita debug. Error-nya di sini. Lihat log-nya, pelan-pelan."
    e "Ketemu! Variabelnya ketukar. Satu baris doang, tapi bikin semua error."
    jk "Bagus. Sekarang jalan. Kopi dulu, Rp8.000, biar tidak ngantuk."
    if uang_nata >= 8000:
        $ uang_nata -= 8000
        e "Biar aku yang beli kopinya, Rp8.000 doang. Anggap aja patungan."
        jk "...Makasih."
    $ ospek_tracker.update_stat("academic_potential", 5)
    $ tambah_kedekatan("joko", 15)
    $ tahap_rute["joko"] = 3
    $ maju_slot()
    hide joko
    call cek_peristiwa_harian
    return


label joko_3:
    # Langkah 3: demo ke teman-teman di kampus. Syarat: sosial >= 10.
    show joko at sprite_normal
    if ospek_tracker.stats["leadership"] < 10:
        jk "Aku masih grogi kalau demo di depan orang. Kamu latihan ngomong dulu di depan teman-teman, biar pede. Nanti kita demo bareng ya."
        hide joko
        return
    jk "Ruang kelas ini kosong, pas buat latihan demo. Kamu jadi penontonnya, tanya yang susah-susah."
    e "Pertanyaan pertama: fiturnya buat siapa? ... Bagus. Kedua: kalau error, gimana?"
    jk "Aduh, pertanyaanmu lebih susah daripada penonton beneran. Tapi sekarang aku jadi pede. Makasih, Nat."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("joko", 15)
    $ tahap_rute["joko"] = 4
    $ maju_slot()
    hide joko
    call cek_peristiwa_harian
    return


label joko_4:
    # Langkah 4: hari demo di kampus. Hasil tergantung akademik.
    scene bg kampus
    show joko kaget
    jk "Ini dia harinya. Aku deg-degan. Kamu duduk di depan ya."
    e "Semangat, Jok. Proyeknya sudah jalan, kodenya bersih. Tinggal demo seperti waktu latihan."
    show joko hoodie
    jk "Selamat pagi, teman-teman, ini proyek kami... (demo berjalan lancar, penonton mengangguk-angguk, ada yang langsung coba.)"
    if ospek_tracker.stats["academic_potential"] >= 30:
        show joko tertawa
        jk "NATA! PROYEKNYA MENANG! Juara satu lomba proyek mahasiswa! Hadiahnya Rp150.000, ini Rp75.000 buat kamu."
        jk "Tanpa kamu, bug itu tidak akan ketemu. Kamu sahabat terbaikku, Nat."
        $ uang_nata += 75000
        $ joko_menang = True
        $ tambah_kedekatan("joko", 20)
    else:
        show joko sedih
        jk "Tidak menang. Tidak apa-apa, ini demo pertamaku, dan proyeknya jadi karena bantuanmu."
        show joko hoodie
        jk "Semester depan kita coba lagi, dan kita menang. Makasih ya, Nat, kamu sahabat terbaikku."
        $ tambah_kedekatan("joko", 10)
    $ tahap_rute["joko"] = 5
    $ maju_slot()
    hide joko
    call cek_peristiwa_harian
    return


label joko_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show joko at sprite_normal
    if joko_menang:
        jk "Proyeknya sekarang dipakai anak kos, Nat. Ada ide fitur baru, kerjain lagi ya?"
    else:
        jk "Proyek kemarin aku perbaiki lagi. Semester depan kita coba lagi, dan kita menang."
    $ tambah_kedekatan("joko", 2)
    $ maju_slot()
    hide joko
    call cek_peristiwa_harian
    return


# --- Yosep: anak organisasi, aktif UKM. ------------------------------- #
# Rute: ikut kepanitiaan acara kampus sampai hari-H (5 langkah).        #
# Langkah 0-2 di Simpang Lima (rekrut, rapat panitia), langkah 3-4 di  #
# Kampus (gladi bersih, hari acara).                                    #

label ketemu_yosep(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show yosep at sprite_normal
        ys "Nata, kamu kelihatan capek banget. Istirahat dulu, rapat bisa nunggu. Nanti kita ngobrol lagi."
        hide yosep
        return
    $ _tahap = tahap_rute["yosep"]
    if _tahap < 3 and lokasi != "simpang_lima":
        show yosep at sprite_normal
        ys "Rapat panitianya di Simpang Lima, Nat. Kalau mau ikut, ketemu di sana ya."
        hide yosep
        return
    if _tahap >= 3 and _tahap < 5 and lokasi != "kampus_unemes":
        show yosep at sprite_normal
        ys "Gladi sama acaranya di kampus, Nat. Ketemu di sana ya."
        hide yosep
        return
    if _tahap == 0:
        call yosep_0
    elif _tahap == 1:
        call yosep_1
    elif _tahap == 2:
        call yosep_2
    elif _tahap == 3:
        call yosep_3
    elif _tahap == 4:
        call yosep_4
    else:
        call yosep_selesai
    return


label yosep_0:
    # Langkah 0: kenalan di Simpang Lima. Yosep rekrut panitia acara.
    show yosep at sprite_normal
    ys "Eh, anak baru! Kamu Nata, kan? Aku Yosep, anak UKM. Lagi cari panitia buat acara kampus bulan depan."
    e "Acara apa? Aku baru seminggu di Semarang, belum kenal siapa-siapa."
    ys "Festival kampus! Panggung, bazar, lomba. Butuh orang yang bisa diandalkan. Kamu kelihatan bisa diandalkan."
    e "Boleh deh, ikut. Tapi aku belum pernah jadi panitia apa-apa."
    ys "Tidak apa-apa, semua juga mulai dari nol. Besok rapat pertama, di sini lagi ya. Bawa semangat."
    $ tambah_kedekatan("yosep", 15)
    $ tahap_rute["yosep"] = 1
    $ maju_slot()
    hide yosep
    call cek_peristiwa_harian
    return


label yosep_1:
    # Langkah 1: pilih divisi di Simpang Lima.
    show yosep at sprite_normal
    if divisi_yosep is None:
        ys "Jadi, divisinya mau yang mana? Aku sudah siapin tiga, kamu pilih satu."
        menu:
            "Divisi acara":
                $ divisi_yosep = "acara"
            "Divisi humas":
                $ divisi_yosep = "humas"
            "Divisi logistik":
                $ divisi_yosep = "logistik"
    if divisi_yosep == "acara":
        $ _divisi = "divisi acara"
    elif divisi_yosep == "humas":
        $ _divisi = "divisi humas"
    else:
        $ _divisi = "divisi logistik"
    ys "Oke, kamu di [_divisi]. Tugas pertama: cari tahu siapa saja yang bisa bantu. Aku percaya sama kamu."
    e "Sudah kutanya lima orang, tiga mau bantu. Besok kita rapat lagi."
    ys "Bagus! Kamu cepat. Tinggal rapat panitianya sekarang."
    $ ospek_tracker.update_stat("leadership", 3)
    $ tambah_kedekatan("yosep", 10)
    $ tahap_rute["yosep"] = 2
    $ maju_slot()
    hide yosep
    call cek_peristiwa_harian
    return


label yosep_2:
    # Langkah 2: rapat panitia. Syarat: sosial >= 15.
    show yosep at sprite_normal
    if ospek_tracker.stats["leadership"] < 15:
        ys "Nat, rapat panitia ini lumayan berat. Latihan ngomong dulu di depan teman-teman, biar pede. Nanti kita rapat bareng ya."
        hide yosep
        return
    ys "Hari ini kita rapat. Kamu pimpin, aku catat. Kalau ada yang ribut, bilang ya."
    e "Agenda satu selesai. Agenda dua... selesai juga. Ternyata rapat bareng lebih cepat daripada rapat sendirian."
    ys "Rapatnya sudah jadi! Tinggal iuran panitia, Rp10.000, buat konsumsi rapat."
    if uang_nata >= 10000:
        $ uang_nata -= 10000
        e "Biar aku yang bayar iurannya, Rp10.000 doang. Anggap aja patungan."
        ys "Ya sudah, makasih! Nanti kalau acara sukses, aku yang traktir."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("yosep", 15)
    $ tahap_rute["yosep"] = 3
    $ maju_slot()
    hide yosep
    call cek_peristiwa_harian
    return


label yosep_3:
    # Langkah 3: gladi bersih di kampus. Syarat: akademik >= 15.
    show yosep at sprite_normal
    if ospek_tracker.stats["academic_potential"] < 15:
        ys "Aku masih bingung bikin rundown-nya. Kamu kejar dulu tugas kuliahmu, biar otakmu encer. Nanti kita gladi bareng ya."
        hide yosep
        return
    ys "Lapangan ini kosong, pas buat gladi. Kamu jadi penontonnya, tanya yang susah-susah."
    e "Pertanyaan pertama: rundown-nya jam berapa mulai? ... Bagus. Kedua: kalau hujan, gimana?"
    ys "Aduh, pertanyaanmu lebih susah daripada panitia beneran. Tapi sekarang aku jadi pede. Makasih, Nat."
    $ ospek_tracker.update_stat("academic_potential", 5)
    $ tambah_kedekatan("yosep", 15)
    $ tahap_rute["yosep"] = 4
    $ maju_slot()
    hide yosep
    call cek_peristiwa_harian
    return


label yosep_4:
    # Langkah 4: hari acara di kampus. Hasil tergantung sosial.
    scene bg kampus
    show yosep kaget
    ys "Ini dia harinya. Aku deg-degan banget. Kamu duduk di depan ya, biar aku bisa lihat kamu."
    e "Semangat, Sep. Acaranya sudah siap, rundown-nya rapi. Tinggal jalan seperti waktu gladi."
    show yosep jaket
    ys "Selamat datang di festival kampus... (acara berjalan lancar, penonton ramai, semua divisi jalan.)"
    if ospek_tracker.stats["leadership"] >= 30:
        show yosep tertawa
        ys "NATA! ACARANYA SUKSES! Ramai banget! Ini, Rp50.000 buat kamu, honor panitia. Sisanya buat kas UKM."
        ys "Tanpa kamu, rapat itu tidak akan jadi. Kamu sahabat terbaikku, Nat."
        $ uang_nata += 50000
        $ yosep_sukses = True
        $ tambah_kedekatan("yosep", 20)
    else:
        show yosep sedih
        ys "Acara jalan, tapi tidak seramai harapan. Tidak apa-apa, ini acara pertamaku, dan rapatnya jadi karena bantuanmu."
        show yosep jaket
        ys "Semester depan kita coba lagi, dan kita ramai. Makasih ya, Nat, kamu sahabat terbaikku."
        $ tambah_kedekatan("yosep", 10)
    $ tahap_rute["yosep"] = 5
    $ maju_slot()
    hide yosep
    call cek_peristiwa_harian
    return


label yosep_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show yosep at sprite_normal
    if yosep_sukses:
        ys "Festival kemarin ramai terus, Nat. Eh, semester depan ada acara lagi, ikut panitia lagi ya?"
    else:
        ys "Evaluasi acara kemarin sudah kubuat. Semester depan kita coba lagi, dan kita ramai."
    $ tambah_kedekatan("yosep", 2)
    $ maju_slot()
    hide yosep
    call cek_peristiwa_harian
    return


# --- Sari: kakak senior, asisten dosen. ------------------------------- #
# Rute: jadi asistennya, belajar manajemen waktu (5 langkah).           #
# Semua langkah di Kampus (dia cuma ada di sana).                      #

label ketemu_sari(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show sari at sprite_normal
        s "Nata, kamu kelihatan capek banget. Istirahat dulu, tugas bisa nunggu. Nanti kita ngobrol lagi."
        hide sari
        return
    $ _tahap = tahap_rute["sari"]
    if _tahap < 5 and lokasi != "kampus_unemes":
        show sari at sprite_normal
        s "Aku di kampus, Nat. Kalau mau bantuin tugas asdos, ketemu di sana ya."
        hide sari
        return
    if _tahap == 0:
        call sari_0
    elif _tahap == 1:
        call sari_1
    elif _tahap == 2:
        call sari_2
    elif _tahap == 3:
        call sari_3
    elif _tahap == 4:
        call sari_4
    else:
        call sari_selesai
    return


label sari_0:
    # Langkah 0: kenalan di kampus. Sari cari asisten buat tugas asdos.
    show sari at sprite_normal
    s "Eh, anak baru! Kamu Nata, kan? Aku Sari, kakak tingkat, asisten dosen. Lagi cari asisten buat bantu tugasku."
    e "Tugas apa, Kak? Aku baru seminggu kuliah, belum ngerti apa-apa."
    s "Rekap nilai, siapkan materi, jaga lab. Santai, semua juga mulai dari nol. Kamu kelihatan rajin."
    e "Boleh deh, Kak. Tapi ajarin ya, jangan langsung disuruh."
    s "Pasti. Besok ketemu di sini lagi ya, kita mulai dari yang gampang."
    $ tambah_kedekatan("sari", 15)
    $ tahap_rute["sari"] = 1
    $ maju_slot()
    hide sari
    call cek_peristiwa_harian
    return


label sari_1:
    # Langkah 1: pilih tugas di kampus.
    show sari at sprite_normal
    if tugas_sari is None:
        s "Jadi, tugasnya mau yang mana? Aku sudah siapin tiga, kamu pilih satu."
        menu:
            "Rekap nilai":
                $ tugas_sari = "nilai"
            "Siapkan materi":
                $ tugas_sari = "materi"
            "Jaga lab":
                $ tugas_sari = "lab"
    if tugas_sari == "nilai":
        $ _tugas = "rekap nilai"
    elif tugas_sari == "materi":
        $ _tugas = "siapkan materi"
    else:
        $ _tugas = "jaga lab"
    s "Oke, tugasmu [_tugas]. Kerjakan pelan-pelan, kalau bingung tanya aku. Aku percaya sama kamu."
    e "Sudah kubuat daftarnya, tinggal dicek. Besok kita lanjut lagi."
    s "Bagus! Kamu cepat. Tinggal rekap nilainya sekarang."
    $ ospek_tracker.update_stat("academic_potential", 3)
    $ tambah_kedekatan("sari", 10)
    $ tahap_rute["sari"] = 2
    $ maju_slot()
    hide sari
    call cek_peristiwa_harian
    return


label sari_2:
    # Langkah 2: bantu rekap nilai. Syarat: akademik >= 25.
    show sari at sprite_normal
    if ospek_tracker.stats["academic_potential"] < 25:
        s "Nat, rekap nilai ini lumayan berat. Kejar dulu tugas kuliahmu sampai akademikmu lumayan, nanti kita lanjut rekap bareng ya."
        hide sari
        return
    s "Hari ini kita rekap nilainya. Kamu ketik, aku dikte. Kalau ada angka yang aneh, bilang ya."
    e "Baris satu selesai. Baris dua... selesai juga. Ternyata rekap bareng lebih cepat daripada rekap sendirian."
    s "Rekapnya sudah jadi! Tinggal diprint buat dosen. Printnya aku yang bayar, kamu sudah bantu banyak."
    if uang_nata >= 5000:
        $ uang_nata -= 5000
        e "Biar aku yang bayar printnya, Rp5.000 doang. Anggap aja patungan."
        s "Ya sudah, makasih! Nanti kalau nilaiku bagus, aku yang traktir."
    $ ospek_tracker.update_stat("academic_potential", 5)
    $ tambah_kedekatan("sari", 15)
    $ tahap_rute["sari"] = 3
    $ maju_slot()
    hide sari
    call cek_peristiwa_harian
    return


label sari_3:
    # Langkah 3: atur jadwal belajar di kampus. Syarat: sosial >= 15.
    show sari at sprite_normal
    if ospek_tracker.stats["leadership"] < 15:
        s "Aku masih bingung atur jadwal. Kamu latihan ngatur waktu dulu, biar rapi. Nanti kita atur bareng ya."
        hide sari
        return
    s "Ruang kelas ini kosong, pas buat atur jadwal. Kamu jadi pengingatnya, tanya yang susah-susah."
    e "Pertanyaan pertama: kuliah jam berapa mulai? ... Bagus. Kedua: kalau ada tugas mendadak, gimana?"
    s "Aduh, pertanyaanmu lebih susah daripada dosen beneran. Tapi sekarang aku jadi rapi. Makasih, Nat."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("sari", 15)
    $ tahap_rute["sari"] = 4
    $ maju_slot()
    hide sari
    call cek_peristiwa_harian
    return


label sari_4:
    # Langkah 4: evaluasi akhir di kampus. Hasil tergantung akademik.
    scene bg kampus
    show sari kaget
    s "Ini dia harinya. Evaluasi asisten. Aku deg-degan banget. Kamu duduk di depan ya."
    e "Semangat, Kak. Rekapnya sudah rapi, jadwalnya jelas. Tinggal jawab seperti waktu latihan."
    show sari cardigan
    s "Baik, Pak, ini hasil rekapnya... (evaluasi berjalan lancar, dosen mengangguk-angguk.)"
    if ospek_tracker.stats["academic_potential"] >= 35:
        show sari tertawa
        s "NATA! AKU DAPAT REKOMENDASI! Dosen bilang rekapku paling rapi! Ini, Rp50.000 buat kamu, honor asisten. Sisanya aku tabung."
        s "Tanpa kamu, rekap ini tidak akan jadi. Kamu sahabat terbaikku, Nat."
        $ uang_nata += 50000
        $ sari_rekomendasi = True
        $ tambah_kedekatan("sari", 20)
    else:
        show sari sedih
        s "Rekomendasinya belum dapat. Tidak apa-apa, ini evaluasi pertamaku, dan rekapnya jadi karena bantuanmu."
        show sari cardigan
        s "Semester depan kita coba lagi, dan kita dapat. Makasih ya, Nat, kamu sahabat terbaikku."
        $ tambah_kedekatan("sari", 10)
    $ tahap_rute["sari"] = 5
    $ maju_slot()
    hide sari
    call cek_peristiwa_harian
    return


label sari_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show sari at sprite_normal
    if sari_rekomendasi:
        s "Rekomendasinya sudah kupakai buat daftar beasiswa, Nat. Eh, semester depan jadi asdos lagi ya?"
    else:
        s "Rekap semester ini aku perbaiki lagi. Semester depan kita coba lagi, dan kita dapat."
    $ tambah_kedekatan("sari", 2)
    $ maju_slot()
    hide sari
    call cek_peristiwa_harian
    return


# --- Dimas: teman sekamar kos, suka masak. ---------------------------- #
# Rute: patungan dapur kos, bagi tugas bersih-bersih (5 langkah).       #
# Semua langkah di Kos (dia teman sekamar).                            #

label ketemu_dimas(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show dimas at sprite_normal
        d "Nata, kamu kelihatan capek banget. Tidur dulu, masak bisa nunggu. Nanti kita ngobrol lagi."
        hide dimas
        return
    $ _tahap = tahap_rute["dimas"]
    if _tahap < 5 and lokasi != "kos_nata":
        show dimas at sprite_normal
        d "Aku di kos, Nat. Kalau mau patungan dapur, ketemu di sana ya."
        hide dimas
        return
    if _tahap == 0:
        call dimas_0
    elif _tahap == 1:
        call dimas_1
    elif _tahap == 2:
        call dimas_2
    elif _tahap == 3:
        call dimas_3
    elif _tahap == 4:
        call dimas_4
    else:
        call dimas_selesai
    return


label dimas_0:
    # Langkah 0: kenalan di kos. Dimas ajak patungan dapur.
    show dimas at sprite_normal
    d "Eh, teman sekamar! Kamu Nata, kan? Aku Dimas. Baru seminggu, tapi kos ini sudah berantakan."
    e "Iya, aku Nata. Kamarku masih isi kardus semua."
    d "Dengerin, Nat. Aku jago masak. Daripada tiap hari beli makan, mending kita patungan dapur. Masak bareng, hemat, enak."
    e "Boleh deh. Tapi aku tidak bisa masak, bisanya makan doang."
    d "Tidak apa-apa, semua juga mulai dari nol. Besok kita atur menunya, di sini lagi ya."
    $ tambah_kedekatan("dimas", 15)
    $ tahap_rute["dimas"] = 1
    $ maju_slot()
    hide dimas
    call cek_peristiwa_harian
    return


label dimas_1:
    # Langkah 1: pilih menu mingguan di kos.
    show dimas at sprite_normal
    if menu_dimas is None:
        d "Jadi, menu mingguannya yang mana? Aku sudah siapin tiga, kamu pilih satu."
        menu:
            "Sayur lodeh":
                $ menu_dimas = "lodeh"
            "Ayam goreng":
                $ menu_dimas = "ayam"
            "Tempe orek":
                $ menu_dimas = "tempe"
    if menu_dimas == "lodeh":
        $ _menu = "sayur lodeh"
    elif menu_dimas == "ayam":
        $ _menu = "ayam goreng"
    else:
        $ _menu = "tempe orek"
    d "Oke, menunya [_menu]. Besok kita belanja bahannya. Aku yang masak, kamu yang cuci piring."
    e "Deal. Tapi jangan pedas-pedas, perutku tidak kuat."
    d "Tenang, aku atur. Tinggal patungan bahannya sekarang."
    $ ospek_tracker.update_stat("leadership", 3)
    $ tambah_kedekatan("dimas", 10)
    $ tahap_rute["dimas"] = 2
    $ maju_slot()
    hide dimas
    call cek_peristiwa_harian
    return


label dimas_2:
    # Langkah 2: patungan dapur Rp50.000. Syarat: uang >= 50000.
    show dimas at sprite_normal
    if uang_nata < 50000:
        d "Nat, patungan dapurnya Rp50.000. Uangmu belum cukup, kumpulin dulu ya. Nanti kita belanja bareng."
        hide dimas
        return
    d "Hari ini kita belanja bahan. Kamu pegang daftarnya, aku yang pilih. Kalau ada yang mahal, bilang ya."
    e "Bawang selesai. Cabai... selesai juga. Ternyata belanja bareng lebih cepat daripada belanja sendirian."
    d "Bahan sudah lengkap! Patungannya Rp50.000, ya."
    $ uang_nata -= 50000
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("dimas", 15)
    $ tahap_rute["dimas"] = 3
    $ maju_slot()
    hide dimas
    call cek_peristiwa_harian
    return


label dimas_3:
    # Langkah 3: bagi tugas bersih-bersih di kos. Syarat: sosial >= 10.
    show dimas at sprite_normal
    if ospek_tracker.stats["leadership"] < 10:
        d "Kos ini berantakan banget. Kamu latihan ngatur waktu dulu, biar rapi. Nanti kita bersih-bersih bareng ya."
        hide dimas
        return
    d "Hari ini kita bersih-bersih. Kamu sapu, aku pel. Kalau ada yang kotor, bilang ya."
    e "Lantai selesai. Kamar mandi... selesai juga. Ternyata bersih-bersih bareng lebih cepat daripada sendirian."
    d "Kosnya sudah bersih! Sekarang tinggal masak besarnya."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("dimas", 15)
    $ tahap_rute["dimas"] = 4
    $ maju_slot()
    hide dimas
    call cek_peristiwa_harian
    return


label dimas_4:
    # Langkah 4: masak besar + makan bareng di kos. Hasil tergantung sosial.
    scene bg kos
    show dimas kaget
    d "Ini dia harinya. Masak besar pertama, aku deg-degan banget. Kamu duduk di depan ya."
    e "Semangat, Dim. Bahannya sudah lengkap, dapurnya bersih. Tinggal masak seperti biasa."
    show dimas flanel
    d "Makan, semuanya... (masakan disajikan, anak kos makan lahap, ada yang nambah dua kali.)"
    if ospek_tracker.stats["leadership"] >= 25:
        show dimas tertawa
        d "NATA! MASAKANKU LARIS! Anak kos pada nambah! Ini, Rp50.000 buat kamu, hasil jualan masakan sisa. Sisanya buat belanja besok."
        d "Tanpa kamu, dapur ini tidak akan jadi. Kamu sahabat terbaikku, Nat."
        $ uang_nata += 50000
        $ dimas_laris = True
        $ tambah_kedekatan("dimas", 20)
    else:
        show dimas sedih
        d "Masakan laku, tapi tidak seberapa. Tidak apa-apa, ini masak besar pertamaku, dan dapurnya jadi karena bantuanmu."
        show dimas flanel
        d "Minggu depan kita coba lagi, dan kita laris. Makasih ya, Nat, kamu sahabat terbaikku."
        $ tambah_kedekatan("dimas", 10)
    $ tahap_rute["dimas"] = 5
    $ maju_slot()
    hide dimas
    call cek_peristiwa_harian
    return


label dimas_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show dimas at sprite_normal
    if dimas_laris:
        d "Dapur kos sekarang ramai terus, Nat. Eh, minggu depan masak besar lagi ya?"
    else:
        d "Menu minggu depan aku perbaiki lagi. Minggu depan kita coba lagi, dan kita laris."
    $ tambah_kedekatan("dimas", 2)
    $ maju_slot()
    hide dimas
    call cek_peristiwa_harian
    return


# --- Pak Budi: dosen pembimbing, tegas tapi baik. --------------------- #
# Rute: bimbingan, jangan sampai dimarahi (5 langkah).                  #
# Semua langkah di Kampus (dia cuma ada di sana).                      #

label ketemu_pak_budi(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show pak_budi at sprite_normal
        p "Nata, kamu kelihatan capek. Istirahat dulu, bimbingan bisa nunggu. Nanti kita ngobrol lagi."
        hide pak_budi
        return
    $ _tahap = tahap_rute["pak_budi"]
    if _tahap < 5 and lokasi != "kampus_unemes":
        show pak_budi at sprite_normal
        p "Saya di kampus, Nata. Kalau mau bimbingan, ketemu di sana ya."
        hide pak_budi
        return
    if _tahap == 0:
        call pak_budi_0
    elif _tahap == 1:
        call pak_budi_1
    elif _tahap == 2:
        call pak_budi_2
    elif _tahap == 3:
        call pak_budi_3
    elif _tahap == 4:
        call pak_budi_4
    else:
        call pak_budi_selesai
    return


label pak_budi_0:
    # Langkah 0: kenalan di kampus. Pak Budi jadi dosen pembimbing Nata.
    show pak_budi at sprite_normal
    p "Nata, ya? Saya Pak Budi, dosen pembimbingmu. Duduk. Kita bicara sebentar."
    e "Iya, Pak. Saya Nata, baru seminggu kuliah."
    p "Bagus. Saya dengar kamu rajin. Tapi rajin saja tidak cukup, harus terarah. Saya akan bimbing kamu, asal kamu serius."
    e "Siap, Pak. Saya serius."
    p "Bagus. Besok bawa idemu, di sini lagi. Jangan telat."
    $ tambah_kedekatan("pak_budi", 15)
    $ tahap_rute["pak_budi"] = 1
    $ maju_slot()
    hide pak_budi
    call cek_peristiwa_harian
    return


label pak_budi_1:
    # Langkah 1: pilih topik bimbingan di kampus.
    show pak_budi at sprite_normal
    if topik_budi is None:
        p "Jadi, topik bimbingannya yang mana? Saya sudah siapin tiga, kamu pilih satu."
        menu:
            "Proposal skripsi":
                $ topik_budi = "skripsi"
            "Proyek akhir":
                $ topik_budi = "proyek"
            "Lomba karya tulis":
                $ topik_budi = "lomba"
    if topik_budi == "skripsi":
        $ _topik = "proposal skripsi"
    elif topik_budi == "proyek":
        $ _topik = "proyek akhir"
    else:
        $ _topik = "lomba karya tulis"
    p "Oke, topiknya [_topik]. Kerjakan pelan-pelan, kalau bingung tanya saya. Saya percaya sama kamu."
    e "Sudah kubuat garis besarnya, Pak. Tinggal dicek."
    p "Bagus. Kamu cepat. Tinggal revisi proposalnya sekarang."
    $ ospek_tracker.update_stat("academic_potential", 3)
    $ tambah_kedekatan("pak_budi", 10)
    $ tahap_rute["pak_budi"] = 2
    $ maju_slot()
    hide pak_budi
    call cek_peristiwa_harian
    return


label pak_budi_2:
    # Langkah 2: revisi proposal. Syarat: akademik >= 25.
    show pak_budi at sprite_normal
    if ospek_tracker.stats["academic_potential"] < 25:
        p "Nata, proposal ini lumayan berat. Kejar dulu tugas kuliahmu sampai akademikmu lumayan, nanti kita lanjut revisi bareng ya."
        hide pak_budi
        return
    p "Hari ini kita revisi proposalnya. Kamu ketik, saya dikte. Kalau ada kalimat yang aneh, bilang ya."
    e "Bab satu selesai. Bab dua... selesai juga. Ternyata revisi bareng lebih cepat daripada revisi sendirian."
    p "Proposalnya sudah jadi! Tinggal diprint buat dibaca ulang. Printnya saya yang bayar, kamu sudah kerja keras."
    if uang_nata >= 5000:
        $ uang_nata -= 5000
        e "Biar saya yang bayar printnya, Pak. Rp5.000 doang."
        p "Ya sudah, terima kasih. Nanti kalau disetujui, saya yang traktir."
    $ ospek_tracker.update_stat("academic_potential", 5)
    $ tambah_kedekatan("pak_budi", 15)
    $ tahap_rute["pak_budi"] = 3
    $ maju_slot()
    hide pak_budi
    call cek_peristiwa_harian
    return


label pak_budi_3:
    # Langkah 3: presentasi bimbingan di kampus. Syarat: sosial >= 10.
    show pak_budi at sprite_normal
    if ospek_tracker.stats["leadership"] < 10:
        p "Kamu masih grogi kalau presentasi. Latihan ngomong dulu di depan teman-teman, biar pede. Nanti kita presentasi bareng ya."
        hide pak_budi
        return
    p "Ruang kelas ini kosong, pas buat latihan presentasi. Saya jadi pengujinya, tanya yang susah-susah."
    e "Pertanyaan pertama: kenapa topik ini penting? ... Bagus. Kedua: datanya dari mana?"
    p "Aduh, pertanyaan saya lebih susah daripada penguji beneran. Tapi sekarang kamu jadi pede. Bagus, Nata."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("pak_budi", 15)
    $ tahap_rute["pak_budi"] = 4
    $ maju_slot()
    hide pak_budi
    call cek_peristiwa_harian
    return


label pak_budi_4:
    # Langkah 4: sidang mini di kampus. Hasil tergantung akademik.
    scene bg kampus
    show pak_budi kaget
    p "Ini dia harinya. Sidang mini. Saya deg-degan juga. Kamu duduk di depan ya."
    e "Semangat, Pak. Proposalnya sudah rapi, datanya kuat. Tinggal jawab seperti waktu latihan."
    show pak_budi batik
    p "Baik, hadirin sekalian, ini proposal bimbingan kami... (sidang berjalan lancar, penguji mengangguk-angguk.)"
    if ospek_tracker.stats["academic_potential"] >= 35:
        show pak_budi tertawa
        p "NATA! PROPOSALNYA DISETUJUI! Penguji bilang proposalmu paling rapi! Bimbingan intensif lanjut, akademikmu naik."
        p "Tanpa kamu, proposal ini tidak akan jadi. Kamu mahasiswa terbaikku, Nata."
        $ ospek_tracker.update_stat("academic_potential", 5)
        $ budi_setuju = True
        $ tambah_kedekatan("pak_budi", 20)
    else:
        show pak_budi sedih
        p "Proposalnya belum disetujui. Tidak apa-apa, ini sidang pertamamu, dan proposalnya jadi karena kerja kerasmu."
        show pak_budi batik
        p "Semester depan kita coba lagi, dan kita disetujui. Terima kasih ya, Nata, kamu mahasiswa terbaikku."
        $ tambah_kedekatan("pak_budi", 10)
    $ tahap_rute["pak_budi"] = 5
    $ maju_slot()
    hide pak_budi
    call cek_peristiwa_harian
    return


label pak_budi_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show pak_budi at sprite_normal
    if budi_setuju:
        p "Proposalnya sudah kulanjutkan ke tahap berikutnya, Nata. Eh, semester depan bimbingan lagi ya?"
    else:
        p "Proposal semester ini saya perbaiki lagi. Semester depan kita coba lagi, dan kita disetujui."
    $ tambah_kedekatan("pak_budi", 2)
    $ maju_slot()
    hide pak_budi
    call cek_peristiwa_harian
    return


# --- Bu Ratna: ibu kos, galak di luar, perhatian di dalam. ------------ #
# Rute: bayar kos tepat waktu, bantu bersih-bersih kos (5 langkah).    #
# Semua langkah di Kos (dia cuma ada di sana).                         #

label ketemu_bu_ratna(lokasi):
    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show bu_ratna at sprite_normal
        br "Nata, kamu kelihatan capek banget. Istirahat dulu, bersih-bersih bisa nunggu. Nanti kita ngobrol lagi."
        hide bu_ratna
        return
    $ _tahap = tahap_rute["bu_ratna"]
    if _tahap < 5 and lokasi != "kos_nata":
        show bu_ratna at sprite_normal
        br "Ibu di kos, Nata. Kalau mau bayar kos atau bersih-bersih, ketemu di sana ya."
        hide bu_ratna
        return
    if _tahap == 0:
        call bu_ratna_0
    elif _tahap == 1:
        call bu_ratna_1
    elif _tahap == 2:
        call bu_ratna_2
    elif _tahap == 3:
        call bu_ratna_3
    elif _tahap == 4:
        call bu_ratna_4
    else:
        call bu_ratna_selesai
    return


label bu_ratna_0:
    # Langkah 0: kenalan di kos. Bu Ratna ingatkan bayar kos tepat waktu.
    show bu_ratna at sprite_normal
    br "Eh, anak baru! Kamu Nata, kan? Saya Bu Ratna, ibu kos di sini. Duduk. Kita bicara sebentar."
    e "Iya, Bu. Saya Nata, baru seminggu di sini."
    br "Bagus. Dengar, Nak. Di kos ini aturannya jelas: bayar kos tanggal satu, jangan telat. Bersih-bersih bergiliran. Kalau nurut, ibu sayang."
    e "Siap, Bu. Saya nurut."
    br "Bagus. Besok bantu ibu bersih-bersih, di sini lagi. Jangan telat."
    $ tambah_kedekatan("bu_ratna", 15)
    $ tahap_rute["bu_ratna"] = 1
    $ maju_slot()
    hide bu_ratna
    call cek_peristiwa_harian
    return


label bu_ratna_1:
    # Langkah 1: pilih tugas bersih-bersih di kos.
    show bu_ratna at sprite_normal
    if tugas_ratna is None:
        br "Jadi, tugas bersih-bersihnya yang mana? Ibu sudah siapin tiga, kamu pilih satu."
        menu:
            "Sapu halaman":
                $ tugas_ratna = "halaman"
            "Bersihkan kamar mandi":
                $ tugas_ratna = "mandi"
            "Siram tanaman":
                $ tugas_ratna = "tanaman"
    if tugas_ratna == "halaman":
        $ _tugas = "sapu halaman"
    elif tugas_ratna == "mandi":
        $ _tugas = "bersihkan kamar mandi"
    else:
        $ _tugas = "siram tanaman"
    br "Oke, tugasmu [_tugas]. Kerjakan pelan-pelan, kalau bingung tanya ibu. Ibu percaya sama kamu."
    e "Sudah kubuat daftarnya, Bu. Tinggal dicek."
    br "Bagus! Kamu cepat. Tinggal bayar kosnya sekarang."
    $ ospek_tracker.update_stat("leadership", 3)
    $ tambah_kedekatan("bu_ratna", 10)
    $ tahap_rute["bu_ratna"] = 2
    $ maju_slot()
    hide bu_ratna
    call cek_peristiwa_harian
    return


label bu_ratna_2:
    # Langkah 2: bayar kos Rp600.000. Syarat: uang >= 600000.
    show bu_ratna at sprite_normal
    if uang_nata < 600000:
        br "Nak, bayar kosnya Rp600.000. Uangmu belum cukup, kumpulin dulu ya. Tapi jangan telat-telat, ibu hitung harinya."
        hide bu_ratna
        return
    br "Hari ini bayar kos. Kamu hitung, ibu yang terima. Kalau ada yang kurang, bilang ya."
    e "Enam ratus ribu, Bu. Pas. Ini uangnya."
    br "Bagus! Anak yang bayar tepat waktu, ibu sayang. Sekarang tinggal kerja baktinya."
    $ uang_nata -= 600000
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("bu_ratna", 15)
    $ tahap_rute["bu_ratna"] = 3
    $ maju_slot()
    hide bu_ratna
    call cek_peristiwa_harian
    return


label bu_ratna_3:
    # Langkah 3: kerja bakti kos. Syarat: sosial >= 10.
    show bu_ratna at sprite_normal
    if ospek_tracker.stats["leadership"] < 10:
        br "Kos ini berantakan banget. Kamu latihan ngatur waktu dulu, biar rapi. Nanti kita kerja bakti bareng ya."
        hide bu_ratna
        return
    br "Hari ini kita kerja bakti. Kamu sapu, ibu yang pel. Kalau ada yang kotor, bilang ya."
    e "Halaman selesai. Kamar mandi... selesai juga. Ternyata kerja bakti bareng lebih cepat daripada sendirian."
    br "Kosnya sudah bersih! Sekarang tinggal kerja bakti besarnya."
    $ ospek_tracker.update_stat("leadership", 5)
    $ tambah_kedekatan("bu_ratna", 15)
    $ tahap_rute["bu_ratna"] = 4
    $ maju_slot()
    hide bu_ratna
    call cek_peristiwa_harian
    return


label bu_ratna_4:
    # Langkah 4: kerja bakti besar di kos. Hasil tergantung sosial.
    scene bg kos
    show bu_ratna kaget
    br "Ini dia harinya. Kerja bakti besar, ibu deg-degan juga. Kamu duduk di depan ya."
    e "Semangat, Bu. Kosnya sudah bersih, anak kos kompak. Tinggal kerja seperti biasa."
    show bu_ratna batik
    br "Makan, semuanya... (kerja bakti selesai, kos bersih, anak kos senang, ibu tersenyum.)"
    if ospek_tracker.stats["leadership"] >= 25:
        show bu_ratna tertawa
        br "NATA! KOSNYA PALING BERSIH! Anak kos pada senang! Ini, potongan kos Rp100.000 buat kamu. Bulan depan bayarnya dikurangi."
        br "Tanpa kamu, kos ini tidak akan sebersih ini. Kamu anak kos terbaikku, Nata."
        $ uang_nata += 100000
        $ ratna_diskon = True
        $ tambah_kedekatan("bu_ratna", 20)
    else:
        show bu_ratna sedih
        br "Kos bersih, tapi belum sempurna. Tidak apa-apa, ini kerja bakti pertamamu, dan kosnya jadi karena bantuanmu."
        show bu_ratna batik
        br "Bulan depan kita coba lagi, dan kita sempurna. Makasih ya, Nata, kamu anak kos terbaikku."
        $ tambah_kedekatan("bu_ratna", 10)
    $ tahap_rute["bu_ratna"] = 5
    $ maju_slot()
    hide bu_ratna
    call cek_peristiwa_harian
    return


label bu_ratna_selesai:
    # Rute tamat: obrolan ringan, bisa diulang.
    show bu_ratna at sprite_normal
    if ratna_diskon:
        br "Kos bulan depan sudah dipotong, Nak. Eh, bulan depan kerja bakti lagi ya?"
    else:
        br "Kos bulan depan ibu perbaiki lagi. Bulan depan kita coba lagi, dan kita sempurna."
    $ tambah_kedekatan("bu_ratna", 2)
    $ maju_slot()
    hide bu_ratna
    call cek_peristiwa_harian
    return
