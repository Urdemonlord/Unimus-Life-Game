# ------------------------------------------------------------------------- #
#  Peta Semarang + Lokasi (Unemes Life, adaptasi Summertime Saga)
# ------------------------------------------------------------------------- #
#  Cara pasang:
#    1. Salin file ini ke game/map_semarang.rpy
#    2. Salin peta-semarang-v15.png ke game/images/peta_semarang.png
#       (koordinat pin di file ini sudah disesuaikan dengan peta v15 (globe + gapura bertulisan UNEMES))
#
#  Akurasi geografi (dicek dari koordinat nyata, utara di atas):
#    Pantai Marina -6.948, 110.389 (barat laut, pantai utara)
#    Kota Lama / Blenduk -6.968, 110.427 (utara, timur Marina)
#    Stasiun Tawang -6.964, 110.429 (timur Blenduk, landmark saja)
#    Pelabuhan Tanjung Mas -6.954, 110.430 (timur laut, landmark saja)
#    Lawang Sewu -6.984, 110.411 (barat Simpang Lima, landmark saja)
#    Simpang Lima -6.990, 110.422 (tengah, selatan Kota Lama)
#    Unnes Gunungpati -7.050, 110.392 (selatan barat daya)
#    Undip Tembalang -7.056, 110.442 (selatan tenggara)
#  Kampus Unemes (fiksi) ditaruh di posisi Undip, tenggara bawah,
#  dan kos Nata di sekitarnya, karena kos mahasiswa memang
#  berkumpul di sekitar kampus selatan, bukan di dekat pantai.
#    3. Semua background lokasi sudah ada versi barunya
#       (kos, kampus, perpustakaan, aula, dll, di folder backgrounds/).
#    4. Dari cerita, panggil:  call peta_semarang
#       (ganti / lengkapi label navigasi_bebas yang lama kalau sudah siap)
#
#  Aturan main peta ini:
#    - Pindah lokasi makan bensin 5. Bensin habis = jalan kaki, stamina -10.
#    - Tiap aksi di lokasi makan 1 slot waktu (Pagi/Siang/Sore/Malam).
#      Slot dihitung oleh game/waktu_uang.rpy (maju_slot); aksi di sini
#      mengubah uang / bensin / stamina / stat lewat ospek_tracker,
#      lalu label aksi memanggil cek_peristiwa_harian.
#    - Uang disimpan di variabel `uang_nata` (rupiah). Kiriman orang tua,
#      kos, token listrik, dan kerja part-time ada di waktu_uang.rpy.
# ------------------------------------------------------------------------- #

default uang_nata = 300000
default bensin_nata = 100

image bg peta_semarang = "images/peta_semarang.png"
# TODO: background baru, sementara memakai background yang sudah ada.
image bg kos = "images/kos.jpg"
image bg warteg = "images/warteg.jpg"
image bg angkringan = "images/angkringan.jpg"
image bg simpang_lima = "images/simpang_lima.jpg"
image bg kota_lama = "images/kota_lama.jpg"
image bg pantai_marina = "images/pantai_marina.jpg"
image bg masjid = "images/masjid.jpg"
image bg laundry = "images/laundry.jpg"
image bg kampus = "images/kampus.jpg"
image bg perpustakaan_baru = "images/perpustakaan.jpg"
image bg aula = "images/aula.jpg"

init python:
    # x, y = posisi pin di layar 1920x1080 (gui.init 1920x1080).
    # Peta v16 16:9 full-bleed (2048x1152 -> layar 1920x1080, faktor
    # 0.9375). Pin diukur dari crop zoom v16 2026-11-16. v15 dan
    # sebelumnya 3:2 dengan black bar, ditolak Arya ("ga proporsional,
    # bikin kek Summertime Saga") -> v16 full-bleed ala STS.
    # v17 (label nama tempat dihapus dari gambar peta) DIBATALKAN
    # 2026-11-16 atas perintah Arya ("balikin yg lama deh"), peta
    # kembali ke v16 dengan label di dalam gambar.
    LOCATIONS_SEMARANG = {
        "kos_nata": {
            "name": "Kos Nata",
            "desc": "Kamar kos 3x3, kipas angin, dan tumpukan tugas.",
            "background": "bg kos",
            "x": 1331, "y": 1031,
            "characters": ["dimas", "bu_ratna", "kirana"],
            "actions": [
                ("Tidur siang (stamina +30)", {"uang": 0, "stamina": 30}),
                ("Belajar di kamar (akademik +5, stamina -10)", {"uang": 0, "stamina": -10, "academic_potential": 5}),
                ("Masak mie (Rp5.000, stamina +15)", {"uang": -5000, "stamina": 15}),
                ("Bayar kos (Rp600.000)", {"uang": -600000, "khusus": "bayar_kos"}),
                ("Beli token listrik (Rp50.000)", {"uang": -50000, "khusus": "token_listrik"}),
                ("Isi bensin di pom mini (Rp20.000, bensin +50)", {"uang": -20000, "bensin": 50}),
                ("Begadang belajar (Malam, akademik +8, stamina -5)", {"uang": 0, "stamina": -5, "academic_potential": 8, "khusus": "begadang", "slot": 3}),
            ],
        },
        "kampus_unemes": {
            "name": "Kampus Unemes",
            "desc": "Gedung kuliah, lab, dan kantin kampus.",
            "background": "bg kampus",
            "x": 1453, "y": 797,
            "characters": ["pak_budi", "joko", "rina", "sari"],
            "actions": [
                ("Ikut kuliah (akademik +8, stamina -10)", {"uang": 0, "stamina": -10, "academic_potential": 8}),
                ("Nongkrong di kantin (Rp10.000, sosial +3)", {"uang": -10000, "stamina": 5, "leadership": 3}),
            ],
        },
        "perpustakaan": {
            "name": "Perpustakaan",
            "desc": "Sunyi, ber-AC, tempat paling aman buat belajar.",
            "background": "bg perpustakaan_baru",
            "x": 281, "y": 844,
            "characters": ["rina", "joko"],
            "actions": [
                ("Belajar serius (akademik +10, stamina -10)", {"uang": 0, "stamina": -10, "academic_potential": 10}),
                ("Pinjam buku (gratis, akademik +3)", {"uang": 0, "academic_potential": 3}),
            ],
        },
        "warteg": {
            "name": "Warteg Bu Tini",
            "desc": "Nasi, sayur, dan lauk. Murah, kenyang, cepat.",
            "background": "bg warteg",
            "x": 1219, "y": 928,
            "characters": ["dimas", "kirana"],
            "actions": [
                ("Makan warteg (Rp10.000, stamina +20)", {"uang": -10000, "stamina": 20}),
                ("Makan + ngobrol (Rp12.000, stamina +15, sosial +2)", {"uang": -12000, "stamina": 15, "leadership": 2}),
            ],
        },
        "angkringan": {
            "name": "Angkringan / Burjo",
            "desc": "Nasi kucing, sate usus, wedang jahe. Buka sampai malam.",
            "background": "bg angkringan",
            "x": 1078, "y": 844,
            "characters": ["kirana", "yosep"],
            "actions": [
                ("Nongkrong malam (Rp8.000, stamina +10)", {"uang": -8000, "stamina": 10}),
                ("Traktir teman (Rp20.000, sosial +5)", {"uang": -20000, "stamina": 10, "leadership": 5}),
            ],
        },
        "simpang_lima": {
            "name": "Simpang Lima",
            "desc": "Lapangan kota, tempat jalan sore dan event kampus.",
            "background": "bg simpang_lima",
            "x": 984, "y": 530,
            "characters": ["kirana", "yosep"],
            "actions": [
                ("Jalan sore (gratis, stamina -5)", {"uang": 0, "stamina": -5}),
                ("Jajan kaki lima (Rp15.000, stamina +15)", {"uang": -15000, "stamina": 15}),
            ],
        },
        "kota_lama": {
            "name": "Kota Lama",
            "desc": "Gedung tua peninggalan Belanda, bagus buat foto.",
            "background": "bg kota_lama",
            "x": 1078, "y": 150,
            "characters": ["rina", "joko"],
            "actions": [
                ("Foto-foto (gratis, stamina -5)", {"uang": 0, "stamina": -5}),
                ("Kencan murah (Rp25.000, stamina +10, sosial +2)", {"uang": -25000, "stamina": 10, "leadership": 2}),
            ],
        },
        "masjid_kampus": {
            "name": "Masjid Kampus",
            "desc": "Tenang. Tempat kajian dan menenangkan diri.",
            "background": "bg masjid",
            "x": 1631, "y": 844,
            "characters": ["yosep", "rina"],
            "actions": [
                ("Ikut kajian (gratis, ibadah +6, stamina +10)", {"uang": 0, "stamina": 10, "religious_knowledge": 6}),
                ("Duduk tenang sejenak (gratis, ibadah +3, stamina +15)", {"uang": 0, "stamina": 15, "religious_knowledge": 3}),
            ],
        },
        "pantai_marina": {
            "name": "Pantai Marina",
            "desc": "Angin laut. Tempat healing kalau stres menumpuk.",
            "background": "bg pantai_marina",
            "x": 403, "y": 141,
            "characters": ["kirana"],
            "actions": [
                ("Duduk di pantai (bensin 10, stamina +20)", {"uang": 0, "stamina": 20, "bensin": -10}),
            ],
        },
        "laundry": {
            "name": "Laundry + Indomaret",
            "desc": "Urusan harian: baju bersih, pulsa, dan jajan.",
            "background": "bg laundry",
            "x": 250, "y": 984,
            "characters": ["dimas"],
            "actions": [
                ("Laundry 3 kg (Rp15.000)", {"uang": -15000, "stamina": 0}),
                ("Beli pulsa + jajan (Rp20.000, stamina +5)", {"uang": -20000, "stamina": 5}),
            ],
        },
    }

    def rupiah(nilai):
        """Format rupiah: 1500000 -> 'Rp1.500.000'."""
        return "Rp{:,}".format(nilai).replace(",", ".")

    def terapkan_aksi_semarang(aksi):
        """Terapkan efek satu aksi lokasi, lalu maju 1 slot waktu.

        Kembalikan status: "ok", "uang" (uang kurang), "bensin" (bensin
        kurang), "lelah" (stamina di bawah batas), "waktu" (slot tidak
        cocok), "sudah" (sudah lunas / sudah dibeli bulan ini).
        """
        global uang_nata, bensin_nata, kos_lunas, kos_telat_hari
        global listrik_bulan_ini, begadang_besok
        efek = aksi[1]
        if "slot" in efek and slot_waktu != efek["slot"]:
            return "waktu"
        if efek.get("stamina", 0) < 0 and ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
            return "lelah"
        if uang_nata + efek.get("uang", 0) < 0:
            return "uang"
        if bensin_nata + efek.get("bensin", 0) < 0:
            return "bensin"
        khusus = efek.get("khusus")
        if khusus == "bayar_kos" and kos_lunas:
            return "sudah"
        if khusus == "token_listrik" and listrik_bulan_ini:
            return "sudah"
        uang_nata += efek.get("uang", 0)
        bensin_nata = max(0, min(100, bensin_nata + efek.get("bensin", 0)))
        for stat in ("stamina", "academic_potential", "leadership", "religious_knowledge"):
            if stat in efek:
                ospek_tracker.update_stat(stat, efek[stat])
        if khusus == "bayar_kos":
            kos_lunas = True
            kos_telat_hari = 0
        elif khusus == "token_listrik":
            listrik_bulan_ini = True
        elif khusus == "begadang":
            begadang_besok = True
        maju_slot()
        return "ok"

    def pindah_ke_lokasi_semarang(kunci):
        """Pindah lokasi: bensin -5, atau jalan kaki kalau bensin habis."""
        global bensin_nata
        if kunci not in LOCATIONS_SEMARANG:
            raise ValueError("Lokasi {} tidak ditemukan".format(kunci))
        if bensin_nata >= 5:
            bensin_nata -= 5
        else:
            ospek_tracker.update_stat("stamina", -10)
            renpy.say(None, "Bensin habis, kamu jalan kaki. Stamina -10.")
        loc = LOCATIONS_SEMARANG[kunci]
        renpy.scene()
        renpy.show(loc["background"])


screen peta_semarang():
    add "images/peta_semarang.png" xsize 1920 ysize 1080
    text "PETA SEMARANG" xalign 0.5 yalign 0.03 size 30 color "#ffffff" outlines [(2, "#000000", 0, 0)]
    text "Hari [hari_nata] ([nama_slot()])   |   Uang: [rupiah(uang_nata)]   |   Bensin: [bensin_nata]   |   Stamina: [ospek_tracker.stamina]%" xalign 0.5 yalign 0.09 size 20 color "#ffffff" outlines [(2, "#000000", 0, 0)]
    for _kunci, _lok in LOCATIONS_SEMARANG.items():
        textbutton _lok["name"]:
            xpos _lok["x"] ypos _lok["y"]
            xanchor 0.5 yanchor 0.5
            background "#00000099"
            hover_background "#000000cc"
            padding (14, 6)
            text_outlines [(2, "#000000", 0, 0)]
            action Return(_kunci)
    textbutton "Tutup peta":
        xalign 0.97 yalign 0.03
        action Return(None)


label peta_semarang:
    call screen peta_semarang
    $ _pilih = _return
    if _pilih is None:
        return
    $ pindah_ke_lokasi_semarang(_pilih)
    $ _lok = LOCATIONS_SEMARANG[_pilih]
    $ renpy.say(None, _lok["desc"])
    $ renpy.say(None, "Apa yang kamu lakukan di {}?".format(_lok["name"]))
    menu:
        "Lihat aksi":
            call aksi_lokasi_semarang(_pilih)
        "Kerja part-time":
            call kerja_part_time
            jump peta_semarang
        "Ngobrol dengan karakter di sini":
            call pilih_karakter_semarang(_pilih)
        "Buka peta lagi":
            jump peta_semarang
        "Kembali ke cerita":
            return


label aksi_lokasi_semarang(kunci):
    $ _lok = LOCATIONS_SEMARANG[kunci]
    $ _pilihan = [(a[0], a) for a in _lok["actions"]]
    $ _pilihan.append(("Kembali", None))
    $ _aksi = renpy.display_menu(_pilihan)
    if _aksi is not None:
        $ _status = terapkan_aksi_semarang(_aksi)
        if _status == "ok":
            $ renpy.say(None, "Kamu: {}.".format(_aksi[0]))
            call cek_peristiwa_harian
        elif _status == "uang":
            $ renpy.say(None, "Uangmu tidak cukup untuk itu.")
        elif _status == "bensin":
            $ renpy.say(None, "Bensinmu tidak cukup untuk itu.")
        elif _status == "lelah":
            $ renpy.say(None, "Kamu terlalu lelah. Istirahat dulu, tidur siang di kos itu gratis.")
        elif _status == "waktu":
            $ renpy.say(None, "Itu hanya bisa dilakukan di slot Malam.")
        elif _status == "sudah":
            $ renpy.say(None, "Itu sudah beres bulan ini.")
    return
