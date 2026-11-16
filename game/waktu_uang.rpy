# ------------------------------------------------------------------------- #
#  Sistem Waktu + Uang Kos (Unemes Life, adaptasi Summertime Saga)
# ------------------------------------------------------------------------- #
#  Cara pasang:
#    1. Salin file ini ke game/waktu_uang.rpy
#    2. Wajib bersama game/map_semarang.rpy (uang_nata, bensin_nata,
#       LOCATIONS_SEMARANG, terapkan_aksi_semarang) dan game/script.rpy
#       (ospek_tracker: stamina, leadership, discipline,
#       religious_knowledge, academic_potential, semua 0-100).
#
#  Aturan main:
#    - 4 slot per hari: Pagi, Siang, Sore, Malam. Tiap aksi makan 1 slot.
#      Habis slot Malam, hari berganti: tidur otomatis, stamina pulih
#      +15 (NIGHT_RECOVERY tracker), kecuali begadang atau listrik mati.
#    - Minggu 1 = minggu ospek (hari 1-7). Tiap 7 hari ada evaluasi mingguan.
#    - Kiriman orang tua Rp1.500.000 tiap awal bulan, kadang telat 0-2 hari.
#    - Kos Rp600.000 tiap tanggal 1. Bulan pertama sudah lunas (dibayar
#      orang tua), jadi utang pertama jatuh tanggal 1 bulan kedua.
#      Telat bayar tidak mengunci game: Bu Ratna menegur tiap pagi, dan
#      jumlah hari telat dicatat buat ending.
#    - Token listrik Rp50.000 per bulan. Kalau tanggal 15 belum beli,
#      kos gelap: stamina tidak pulih di malam hari sampai token dibeli.
#    - Kerja part-time bayar per slot, ada batas per minggu, ada syarat
#      slot dan stat. Kerja butuh stamina minimal 15.
#    - Uang habis bukan game over: tidur siang gratis (+30 stamina),
#      lalu kerja part-time (gratis, dibayar), lalu makan. Loop selalu
#      bisa ditutup tanpa utang ke siapa pun.
#
#  Pemetaan stat (dokumen desain -> tracker lama):
#    Akademik -> academic_potential, Sosial -> leadership,
#    Ibadah -> religious_knowledge, Stamina -> stamina.
# ------------------------------------------------------------------------- #

default hari_nata = 1
default slot_waktu = 0
default minggu_nata = 1
default tanggal_nata = 1
default kiriman_telat = 0
default kiriman_diterima = True
default kos_lunas = True
default kos_telat_hari = 0
default listrik_bulan_ini = True
default begadang_besok = False
default kerja_mingguan = {}
default laporan_malam = ""
default flag_kiriman = False
default flag_kos = False
default flag_evaluasi = False
default flag_uts = False
default flag_akhir = False

init python:
    SLOT_NAMA = ["Pagi", "Siang", "Sore", "Malam"]

    KIRIMAN_BULANAN = 1500000
    HARGA_KOS = 600000
    HARGA_TOKEN = 50000
    HARGA_BENSIN = 20000
    BENSIN_ISI = 50
    STAMINA_KERJA_MIN = 15

    # kunci: (nama, slot yang boleh, gaji, stamina, bensin, efek stat,
    #         batas per minggu, syarat (teks, fungsi cek))
    PEKERJAAN = {
        "warung_kopi": {
            "nama": "Jaga warung kopi",
            "slot": [2, 3],
            "gaji": 50000,
            "stamina": -10,
            "bensin": 0,
            "efek": {"leadership": 2},
            "batas": 3,
            "syarat_teks": "Sore atau Malam",
            "syarat": lambda: True,
        },
        "asisten_lab": {
            "nama": "Asisten lab",
            "slot": [1],
            "gaji": 75000,
            "stamina": -10,
            "bensin": 0,
            "efek": {"academic_potential": 3},
            "batas": 2,
            "syarat_teks": "Siang, Akademik 20+",
            "syarat": lambda: ospek_tracker.stats["academic_potential"] >= 20,
        },
        "freelance_desain": {
            "nama": "Freelance desain",
            "slot": [0, 1, 2, 3],
            "gaji": 100000,
            "stamina": -15,
            "bensin": 0,
            "efek": {},
            "batas": 1,
            "syarat_teks": "Akademik 30+",
            "syarat": lambda: ospek_tracker.stats["academic_potential"] >= 30,
        },
        "antar_makanan": {
            "nama": "Antar makanan",
            "slot": [2, 3],
            "gaji": 60000,
            "stamina": -10,
            "bensin": -10,
            "efek": {},
            "batas": 3,
            "syarat_teks": "Sore atau Malam, bensin 10+",
            "syarat": lambda: bensin_nata >= 10,
        },
    }

    def nama_slot():
        return SLOT_NAMA[slot_waktu]

    def maju_slot():
        """Maju 1 slot waktu. Kalau habis Malam, ganti hari.

        Mengatur flag buat label cek_peristiwa_harian, bukan narasi
        langsung, karena fungsi python tidak bisa menampilkan dialog.
        """
        global slot_waktu, hari_nata, minggu_nata, tanggal_nata
        global kiriman_telat, kiriman_diterima, kos_lunas, kos_telat_hari
        global listrik_bulan_ini, begadang_besok, kerja_mingguan
        global laporan_malam, flag_kiriman, flag_kos, flag_evaluasi
        global flag_uts, flag_akhir

        slot_waktu += 1
        if slot_waktu > 3:
            slot_waktu = 0
            hari_nata += 1
            tanggal_nata += 1
            minggu_baru = (hari_nata - 1) // 7 + 1
            if minggu_baru != minggu_nata:
                minggu_nata = minggu_baru
                kerja_mingguan = {}
            if tanggal_nata > 30:
                tanggal_nata = 1
                kiriman_telat = renpy.random.randint(0, 2)
                kiriman_diterima = False
                kos_lunas = False
                flag_kos = True
                listrik_bulan_ini = False
            if tanggal_nata == 1 + kiriman_telat and not kiriman_diterima:
                flag_kiriman = True
            if not kos_lunas:
                kos_telat_hari += 1
            if hari_nata % 7 == 0:
                flag_evaluasi = True
            # Quest utama (quest_utama.rpy): UTS minggu 8 (hari 50),
            # rapor akhir semester setelah hari 112 (hari 113).
            if hari_nata == 50:
                flag_uts = True
            if hari_nata == 113:
                flag_akhir = True
            # Tidur malam: pulih 15, kecuali begadang atau listrik mati.
            if begadang_besok:
                laporan_malam = "Kamu begadang semalam. Badan terasa berat, stamina tidak pulih."
                begadang_besok = False
            elif tanggal_nata >= 15 and not listrik_bulan_ini:
                laporan_malam = "Listrik kos mati semalam (token habis). Kamu tidur dalam gelap, stamina tidak pulih."
            else:
                ospek_tracker.update_stat("stamina", ospek_tracker.NIGHT_RECOVERY)
                laporan_malam = ""

    def bisa_kerja(kunci):
        """Kembalikan (boleh, alasan) buat satu pekerjaan."""
        job = PEKERJAAN[kunci]
        if slot_waktu not in job["slot"]:
            return (False, "Kerja ini hanya bisa di slot {}.".format(
                ", ".join(SLOT_NAMA[s] for s in job["slot"])))
        if ospek_tracker.stamina < STAMINA_KERJA_MIN:
            return (False, "Kamu terlalu lelah buat kerja. Istirahat dulu.")
        if kerja_mingguan.get(kunci, 0) >= job["batas"]:
            return (False, "Jatah {} minggu ini sudah habis.".format(job["nama"]))
        if not job["syarat"]():
            return (False, "Syarat belum terpenuhi: {}.".format(job["syarat_teks"]))
        return (True, "")

    def lakukan_kerja(kunci):
        """Terapkan gaji + efek satu pekerjaan, lalu maju 1 slot."""
        global uang_nata, bensin_nata, kerja_mingguan
        boleh, alasan = bisa_kerja(kunci)
        if not boleh:
            return (False, alasan)
        job = PEKERJAAN[kunci]
        uang_nata += job["gaji"]
        bensin_nata = max(0, min(100, bensin_nata + job["bensin"]))
        ospek_tracker.update_stat("stamina", job["stamina"])
        for stat, nilai in job["efek"].items():
            ospek_tracker.update_stat(stat, nilai)
        kerja_mingguan[kunci] = kerja_mingguan.get(kunci, 0) + 1
        maju_slot()
        return (True, "Kamu kerja sebagai {}. Gaji Rp{:,}.".format(
            job["nama"], job["gaji"]).replace(",", "."))

    def status_keuangan():
        """Satu baris ringkas buat HUD dan evaluasi mingguan."""
        uang_teks = "{:,}".format(uang_nata).replace(",", ".")
        return ("Hari {} ({}), minggu {}, tanggal {} | Uang Rp{} | Bensin {} | "
                "Stamina {}% | Akademik {} | Sosial {} | Ibadah {}".format(
                    hari_nata, SLOT_NAMA[slot_waktu], minggu_nata, tanggal_nata,
                    uang_teks, bensin_nata, ospek_tracker.stamina,
                    ospek_tracker.stats["academic_potential"],
                    ospek_tracker.stats["leadership"],
                    ospek_tracker.stats["religious_knowledge"]))


label cek_peristiwa_harian:
    # Dipanggil setelah tiap aksi: sampaikan apa yang terjadi semalam
    # (kiriman, kos jatuh tempo, evaluasi mingguan) sebelum lanjut.
    if laporan_malam:
        $ renpy.say(None, laporan_malam)
        $ laporan_malam = ""
    if flag_kiriman:
        $ flag_kiriman = False
        $ kiriman_diterima = True
        $ uang_nata += KIRIMAN_BULANAN
        if kiriman_telat > 0:
            $ renpy.say(None, "Kiriman orang tua datang, telat {} hari. Rp1.500.000 masuk. Uangmu sekarang Rp{:,}.".format(kiriman_telat, uang_nata).replace(",", "."))
        else:
            $ renpy.say(None, "Kiriman orang tua datang tepat waktu. Rp1.500.000 masuk. Uangmu sekarang Rp{:,}.".format(uang_nata).replace(",", "."))
    if flag_kos:
        $ flag_kos = False
        $ renpy.say(None, "Tanggal 1. Kos bulan ini Rp600.000, Bu Ratna sudah menagih dari pagi.")
        menu:
            "Bayar kos sekarang (Rp600.000)":
                if uang_nata >= HARGA_KOS:
                    $ uang_nata -= HARGA_KOS
                    $ kos_lunas = True
                    $ kos_telat_hari = 0
                    "Bu Ratna tersenyum. \"Bagus, tepat waktu.\""
                else:
                    "Uangmu tidak cukup. Bu Ratna menghela napas. \"Segera ya, Nak. Jangan sampai lewat tanggal 5.\""
            "Bayar nanti":
                "Kamu mengangguk. Bu Ratna mencatat di buku kecilnya."
    if flag_evaluasi:
        $ flag_evaluasi = False
        call evaluasi_mingguan
    if flag_uts:
        $ flag_uts = False
        call uts
    if flag_akhir:
        $ flag_akhir = False
        call akhir_semester
    return


label evaluasi_mingguan:
    "Sudah satu minggu. Kamu duduk di kos dan menghitung-hitung."
    $ renpy.say(None, status_keuangan())
    if kos_lunas:
        "Kos bulan ini aman."
    else:
        $ renpy.say(None, "Kos masih nunggak {} hari. Bu Ratna makin sering menanyakan.".format(kos_telat_hari))
    if ospek_tracker.stats["academic_potential"] >= 20:
        "Kuliahmu mulai terasa. Dosen sudah hafal namamu."
    if ospek_tracker.stats["leadership"] >= 10:
        "Teman-temanmu makin banyak. Ada yang mengajakmu ikut kepanitiaan."
    if ospek_tracker.stats["religious_knowledge"] >= 10:
        "Hati terasa lebih tenang. Kajian minggu ini menenangkanmu."
    "Minggu depan mulai lagi. Jatah kerja part-time minggu ini direset."
    return


label kerja_part_time:
    "Mencari kerja part-time. Sekali kerja makan 1 slot waktu."
    $ _pilihan = []
    python:
        for _kunci, _job in PEKERJAAN.items():
            _boleh, _alasan = bisa_kerja(_kunci)
            _teks = "{} (Rp{:,}, {})".format(_job["nama"], _job["gaji"], _job["syarat_teks"]).replace(",", ".")
            if not _boleh:
                _teks += " - " + _alasan
            _pilihan.append((_teks, _kunci))
        _pilihan.append(("Tidak jadi", None))
    $ _pilih = renpy.display_menu(_pilihan)
    if _pilih is not None:
        $ _ok, _pesan = lakukan_kerja(_pilih)
        $ renpy.say(None, _pesan)
        call cek_peristiwa_harian
    return
