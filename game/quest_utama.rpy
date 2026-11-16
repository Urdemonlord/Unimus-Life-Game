# ------------------------------------------------------------------------- #
#  Quest Utama Semester + UTS + Ending (Unemes Life)
# ------------------------------------------------------------------------- #
#  Cara pasang:
#    1. Salin file ini ke game/quest_utama.rpy
#    2. Wajib bersama game/waktu_uang.rpy (flag_uts / flag_akhir, hari_nata,
#       minggu_nata, kos_lunas, kos_telat_hari), game/rute_karakter.rpy
#       (kedekatan, tahap_rute, KARAKTER) dan game/script.rpy
#       (ospek_tracker: academic_potential).
#
#  Aturan main:
#    - Semester = 16 minggu (hari 1-112). Minggu 1 = minggu ospek.
#    - UTS: minggu 8 (hari 50). Dipicu otomatis lewat flag_uts dari
#      maju_slot() di waktu_uang.rpy, disampaikan lewat
#      cek_peristiwa_harian. Hasilnya dari stat Akademik, bukan kuis
#      interaktif (kuis mata kuliah dicatat sebagai mini-game berikutnya).
#      Nilai A/B/C/D. Nilai D = remedial, menutup ending terbaik.
#    - Rapor akhir semester: hari 113 (sehari setelah hari terakhir
#      semester). Dipicu otomatis lewat flag_akhir. IPK dihitung dari
#      Akademik (0-100 -> 0.00-4.00), sahabat terdekat dari kedekatan
#      tertinggi. Ending ditentukan dari IPK + kos + nilai UTS + rute
#      yang tamat. Rapor bukan hard stop: setelah rapor, pemain bisa
#      lanjut free-roam (game belum punya New Game+).
#
#  Ending (4):
#    - teladan ("Mahasiswa Teladan"): Akademik >= 80, kos lunas,
#      nilai UTS A/B, minimal 1 rute tamat.
#    - aman ("Semester Aman"): Akademik >= 50, kos lunas.
#    - lulus ("Lulus Pas-pasan"): Akademik >= 20, kos lunas.
#    - pulang ("Pulang Kampung"): kos nunggak (kos_lunas False) atau
#      Akademik < 20. Ending jelek: pulang kampung lebih awal.
# ------------------------------------------------------------------------- #

default uts_selesai = False
default nilai_uts = None
default ending_nama = None

init python:
    SEMESTER_MINGGU = 16
    UTS_HARI = 50
    AKHIR_HARI = 113

    def ipk_nata():
        """IPK 0.00-4.00 dari stat Akademik 0-100."""
        return round(ospek_tracker.stats["academic_potential"] * 4.0 / 100, 2)

    def sahabat_terdekat():
        """Kembalikan (kunci, nama, nilai) karakter dengan kedekatan
        tertinggi. Seri dimenangkan yang lebih dulu di daftar."""
        _terbaik = None
        _nilai = -1
        for _kunci in kedekatan:
            if kedekatan[_kunci] > _nilai:
                _nilai = kedekatan[_kunci]
                _terbaik = _kunci
        return (_terbaik, KARAKTER[_terbaik]["nama"], _nilai)

    def hitung_ending():
        """Kembalikan kunci ending: teladan / aman / lulus / pulang."""
        _akademik = ospek_tracker.stats["academic_potential"]
        if not kos_lunas or _akademik < 20:
            return "pulang"
        _tamat = any(tahap_rute[k] >= 5 for k in tahap_rute)
        if _akademik >= 80 and nilai_uts in ("A", "B") and _tamat:
            return "teladan"
        if _akademik >= 50:
            return "aman"
        return "lulus"


label uts:
    # Ujian Tengah Semester, minggu 8. Hasil dari stat Akademik.
    scene bg aula
    "Hari ini UTS. Aula penuh, semua menunduk ke soal masing-masing."
    "Soal pertama: teori. Kedua: hitungan. Ketiga: studi kasus. Kamu kerjakan satu-satu, pelan tapi pasti."
    $ _akademik = ospek_tracker.stats["academic_potential"]
    if _akademik >= 60:
        $ nilai_uts = "A"
        "Kamu keluar aula dengan senyum. Soalnya berat, tapi semua bisa dijawab. Nilaimu A."
    elif _akademik >= 40:
        $ nilai_uts = "B"
        "Kamu keluar aula dengan lega. Ada dua soal yang ragu-ragu, tapi sisanya lancar. Nilaimu B."
    elif _akademik >= 25:
        $ nilai_uts = "C"
        "Kamu keluar aula sambil menghela napas. Banyak soal yang ditebak. Nilaimu C, lulus pas-pasan."
    else:
        $ nilai_uts = "D"
        "Kamu keluar aula dengan muka pucat. Setengah soal tidak bisa dijawab. Nilaimu D, remedial. Semester ini harus lebih rajin."
    $ uts_selesai = True
    return


label akhir_semester:
    # Rapor akhir semester, hari 113. Ditentukan IPK + kos + UTS + rute.
    scene bg kampus
    "Semester selesai. Kamu duduk di depan globe Unemes dan membuka rapor akhir semester."
    $ _ipk = ipk_nata()
    $ _sahabat = sahabat_terdekat()
    $ ending_nama = hitung_ending()
    $ renpy.say(None, "IPK semester ini: {}. Uang sisa: Rp{:,}.".format(_ipk, uang_nata).replace(",", "."))
    $ renpy.say(None, "Sahabat terdekatmu: {} (kedekatan {}).".format(_sahabat[1], _sahabat[2]))
    if ending_nama == "teladan":
        "Mahasiswa Teladan. IPK tinggi, kos aman, UTS bagus, dan teman banyak. Orang tuamu bangga, kamu pulang kampung dengan kepala tegak."
    elif ending_nama == "aman":
        "Semester Aman. IPK cukup, kos aman. Tidak ada yang istimewa, tapi tidak ada yang berantakan. Semester depan bisa lebih baik."
    elif ending_nama == "lulus":
        "Lulus Pas-pasan. IPK mepet, tapi lulus. Kos aman, teman ada. Semester depan harus lebih rajin."
    else:
        "Pulang Kampung. Kos nunggak dan IPK anjlok. Orang tuamu menyuruhmu pulang lebih awal. Semester depan, coba lagi dari awal."
    return
