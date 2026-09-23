################################################################################
##  UNIMUS LIFE GAME
##  Visual Novel Ospek Universitas Muhammadiyah Semarang
##
##  script.rpy — alur cerita utama + sistem ospek 7 hari
################################################################################

init python:
    import random

    # --------------------------------------------------------------------- #
    #  Data karakter
    # --------------------------------------------------------------------- #
    #  "rel" = kunci pada ospek_tracker.friend_relationship (None utk pemain)
    CHARACTER_INFO = {
        "nata":     {"image": "nata",     "name": "Nata",     "rel": None},
        "andi":     {"image": "andi",     "name": "Andi",     "rel": "Andi"},
        "momogi":   {"image": "momogi",   "name": "Momogi",   "rel": "Momogi"},
        "rina":     {"image": "rina",     "name": "Rina",     "rel": "Rina"},
        "joko":     {"image": "joko",     "name": "Joko",     "rel": "Joko"},
        "pak_budi": {"image": "pak_budi", "name": "Pak Budi", "rel": "Pak Budi"},
        # --- karakter baru ---
        "sari":     {"image": "sari",     "name": "Sari",     "rel": "Sari"},
        "dimas":    {"image": "dimas",    "name": "Dimas",    "rel": "Dimas"},
        "bu_ratna": {"image": "bu_ratna", "name": "Bu Ratna", "rel": "Bu Ratna"},
    }

    CHARACTER_DIALOGUES = {
        "andi": [
            "Semangat, Nata! Ospek itu tempat kita tumbuh bersama.",
            "Kalau ada tugas kelompok, aku siap bantu kapan saja.",
            "Jangan lupa istirahat, kesehatan juga bagian dari ibadah.",
            "Aku ikut organisasi kampus, di sana kita belajar memimpin.",
            "Kita ini satu angkatan, jadi harus saling mengangkat, ya!",
        ],
        "momogi": [
            "Aku jauh dari rumah, tapi di sini aku belajar mandiri.",
            "Kita perantau harus saling menguatkan, ya!",
            "Cita-citaku besar, dan ospek ini langkah pertamanya.",
            "Kangen rumah itu wajar, yang penting jangan menyerah.",
            "Aku ingin membanggakan orang tua di kampung.",
        ],
        "rina": [
            "Menjaga kesehatan tubuh dan jiwa itu seimbang, Nata.",
            "Aku ikut kegiatan kemanusiaan, mau ikut suatu hari?",
            "Senyum itu sedekah, jadi jangan pelit senyum!",
            "Kalau lelah, istirahatlah. Tubuh ini juga amanah.",
            "Aku suka belajar tentang gizi dan kesehatan masyarakat.",
        ],
        "joko": [
            "Disiplin adalah kunci. Tanpa itu, ilmu sulit bermanfaat.",
            "Aku tegas bukan karena benci, tapi karena sayang.",
            "Nilai keagamaan harus jadi fondasi, bukan hiasan.",
            "Senior itu tugasnya membimbing, bukan menakuti.",
            "Jangan takut salah, takutlah kalau tidak mau belajar.",
        ],
        "pak_budi": [
            "Kepemimpinan adalah amanah, bukan sekadar jabatan.",
            "Teruslah belajar, karena ilmu itu cahaya.",
            "Jaga akhlak, maka ilmumu akan berkah.",
            "Ospek bukan ajang balas dendam, tapi ajang pembentukan diri.",
            "Pemimpin yang baik itu mendengar sebelum memutuskan.",
        ],
        "sari": [
            "Hai! Aku Sari, mahasiswa tingkat atas. Ada yang bisa dibantu?",
            "Ikut UKM itu penting, Nata. Bisa menambah pengalaman.",
            "Dulu aku juga gugup saat ospek. Nanti pasti terbiasa.",
            "Jangan sungkan bertanya ke senior, kami siap membantu.",
        ],
        "dimas": [
            "Aku Dimas, teman sekamarmu. Kalau butuh apa-apa, bilang saja.",
            "Bangun pagi itu berat, tapi kita bisa saling membangunkan!",
            "Kita sekamar, jadi kita satu tim. Kompak, ya!",
            "Aku suka begadang belajar, kamu jangan ikut-ikutan, nanti ngantuk di ospek.",
        ],
        "bu_ratna": [
            "Selamat datang, Nata. Saya Bu Ratna, dosen pembimbing.",
            "Belajar itu tidak mengenal usia, teruslah bertanya.",
            "Akademik dan akhlak harus sejalan, itu pesan saya.",
            "Jangan ragu datang ke ruang saya kalau ada kesulitan.",
        ],
    }

    # --------------------------------------------------------------------- #
    #  Event acak harian
    # --------------------------------------------------------------------- #
    #  Setiap tiba hari baru, satu event acak dijalankan (bisa "none").
    #  Jenis:
    #    "rel"  -> ubah kedekatan karakter (kunci "char", "amount")
    #    "stat" -> ubah statistik        (kunci "stat", "amount")
    #    "points" -> tambah poin ospek   (kunci "amount")
    #    "scene"  -> tampilkan narasi + karakter + efek
    # --------------------------------------------------------------------- #
    RANDOM_EVENTS = [
        {
            "id": "sapa_pagi",
            "scene": "bg kampus_depan",
            "speaker": "andi", "position": "center",
            "line": "Nata! Ayo jalan bareng ke aula, jangan sampai telat lagi.",
            "narration": "Andi menyapamu dengan semangat di depan kampus.",
            "rel": {"char": "Andi", "amount": 1},
        },
        {
            "id": "buku_tertinggal",
            "scene": "bg perpustakaan",
            "speaker": "momogi", "position": "center",
            "line": "Aku pinjamkan catatanku, Nata. Belajar bareng yuk!",
            "narration": "Momogi berbagi catatan di perpustakaan.",
            "stat": {"stat": "academic_potential", "amount": 4},
        },
        {
            "id": "jemur_pagi",
            "scene": "bg kampus_depan",
            "speaker": "dimas", "position": "center",
            "line": "Udah sarapan? Aku bawain gorengan nih, kita makan bareng.",
            "narration": "Dimas mengajakmu sarapan bersama.",
            "stat": {"stat": "stamina", "amount": 8},
        },
        {
            "id": "tegur_senior",
            "scene": "bg ospek_hall",
            "speaker": "sari", "position": "center",
            "line": "Hari ini barisanmu paling rapi. Bagus, pertahankan!",
            "narration": "Kak Sari memberi pujian atas kedisiplinanmu.",
            "stat": {"stat": "discipline", "amount": 5},
        },
        {
            "id": "kajian_singkat",
            "scene": "bg masjid",
            "speaker": "joko", "position": "center",
            "line": "Sebelum mulai, mari kita renungkan sejenak ayat hari ini.",
            "narration": "Joko mengajakmu kajian singkat di masjid kampus.",
            "rel": {"char": "Joko", "amount": 1},
            "stat": {"stat": "religious_knowledge", "amount": 6},
        },
        {
            "id": "tips_dosen",
            "scene": "bg ruang_seminar",
            "speaker": "bu_ratna", "position": "center",
            "line": "Nata, saya lihat kamu rajin. Ini tips belajar yang bisa kamu coba.",
            "narration": "Bu Ratna memberi nasihat belajar.",
            "stat": {"stat": "academic_potential", "amount": 6},
        },
        {
            "id": "bantu_bawa",
            "scene": "bg kantin",
            "speaker": "rina", "position": "center",
            "line": "Tumben, kamu mau bantu aku bawa perlengkapan? Terima kasih!",
            "narration": "Kamu membantu Rina membawa perlengkapan kegiatan.",
            "rel": {"char": "Rina", "amount": 1},
        },
        {
            "id": "tugas_tambahan",
            "scene": "bg lecture_room",
            "speaker": "pak_budi", "position": "center",
            "line": "Karena kamu proaktif, saya beri kamu tugas kecil. Bisa?",
            "narration": "Pak Budi memberimu tugas tambahan kepercayaan.",
            "points": {"amount": 2},
        },
        {
            "id": "kantin_rame",
            "scene": "bg kantin",
            "speaker": "momogi", "position": "center",
            "line": "Kantin penuh! Sini, aku sudah pesankan tempat untuk kita.",
            "narration": "Kamu makan siang bersama teman-teman di kantin.",
            "rel": {"char": "Momogi", "amount": 1},
        },
        {
            "id": "olahraga_pagi",
            "scene": "bg kampus_depan",
            "speaker": "andi", "position": "center",
            "line": "Ayo jogging dulu sebelum ospek, biar badan segar!",
            "narration": "Kamu berolahraga pagi bersama Andi.",
            "stat": {"stat": "stamina", "amount": 6},
            "rel": {"char": "Andi", "amount": 1},
        },
    ]

    # --------------------------------------------------------------------- #
    #  Sistem konflik antar-teman
    # --------------------------------------------------------------------- #
    #  Setiap opsi: "rel" = {nama: delta}, "points" = poin, "stat" = {stat: delta}
    #  "resolved" = True berarti konflik terselesaikan dengan baik.
    CONFLICTS = {
        "tugas_tidak_adil": {
            "title": "Pembagian Tugas Tidak Adil",
            "scene": "bg pusat_mahasiswa",
            "intro": "Tugas kelompok menumpuk padamu, sementara Andi dan Joko terlihat santai.",
            "speaker": "andi",
            "line": "Santai saja, Nata. Kan kamu yang paling bisa.",
            "options": [
                {
                    "text": "Bicara baik-baik dan bagi tugas ulang",
                    "reply": "Kamu benar, aku kurang peka. Ayo kita bagi ulang!",
                    "rel": {"Andi": 2, "Joko": 1}, "points": 2,
                    "stat": {"leadership": 5}, "resolved": True,
                    "outcome": "Kamu menyelesaikan konflik dengan komunikasi terbuka.",
                },
                {
                    "text": "Diam saja dan kerjakan semuanya sendiri",
                    "reply": "Ya sudah, kalau kamu memang mau begitu.",
                    "rel": {"Andi": -1}, "points": 1,
                    "stat": {"stamina": -10}, "resolved": False,
                    "outcome": "Tugas selesai, tapi kamu kelelahan dan menyimpan kesal.",
                },
                {
                    "text": "Marah dan meninggalkan ruangan",
                    "reply": "Nata, kenapa kamu jadi begitu?",
                    "rel": {"Andi": -2, "Joko": -1}, "points": 0,
                    "stat": {}, "resolved": False,
                    "outcome": "Kamu pergi dengan marah. Hubungan jadi renggang.",
                },
            ],
        },
        "salah_paham": {
            "title": "Salah Paham dengan Rina",
            "scene": "bg kantin",
            "intro": "Kamu mendengar Rina membicarakanmu, padahal ia sedang membantumu.",
            "speaker": "rina",
            "line": "Aku tadi bilang ke Bu Ratna kalau kamu butuh bantuan...",
            "options": [
                {
                    "text": "Tanya langsung apa maksudnya",
                    "reply": "Oh, kamu salah dengar! Aku justru membelamu di depan dosen.",
                    "rel": {"Rina": 2}, "points": 2,
                    "stat": {"discipline": 3}, "resolved": True,
                    "outcome": "Kamu memilih klarifikasi dulu daripada berprasangka.",
                },
                {
                    "text": "Menjauh tanpa bertanya",
                    "reply": "Nata? Kenapa kamu diam saja?",
                    "rel": {"Rina": -1}, "points": 0,
                    "stat": {}, "resolved": False,
                    "outcome": "Salah paham itu tidak pernah terselesaikan.",
                },
            ],
        },
        "ejekan_senior": {
            "title": "Candaan yang Terlalu Jauh",
            "scene": "bg ospek_hall",
            "intro": "Seorang peserta lain mengejek cara kamu berpenampilan di depan banyak orang.",
            "speaker": "dimas",
            "line": "Nata, jangan didiemin. Kalau kamu mau, aku temani bicara.",
            "options": [
                {
                    "text": "Tegur dengan sopan dan tenang",
                    "reply": "Maaf, aku memang keterlaluan. Tidak akan kuulangi.",
                    "rel": {"Dimas": 1, "Sari": 1}, "points": 2,
                    "stat": {"leadership": 4, "discipline": 3}, "resolved": True,
                    "outcome": "Kamu menegur tanpa kehilangan adab. Kamu dihormati karena itu.",
                },
                {
                    "text": "Balas dengan ejekan juga",
                    "reply": "Sudah, sudah! Kalian ini peserta ospek, bukan preman!",
                    "rel": {"Sari": -1, "Dimas": -1}, "points": 0,
                    "stat": {}, "resolved": False,
                    "outcome": "Keributan kecil terjadi dan Kak Sari harus melerai.",
                },
                {
                    "text": "Diamkan saja dan biarkan lewat",
                    "reply": "Sudah, jangan dipikirin. Tapi lain kali lapor, ya.",
                    "rel": {"Dimas": 1}, "points": 1,
                    "stat": {"discipline": 2}, "resolved": False,
                    "outcome": "Kamu memilih sabar. Perasaanmu tidak enak, tapi situasi aman.",
                },
            ],
        },
        "iri_prestasi": {
            "title": "Kecemburuan atas Prestasimu",
            "scene": "bg ruang_seminar",
            "intro": "Joko terlihat kesal karena kamu dipuji Pak Budi di depan kelas.",
            "speaker": "joko",
            "line": "Enak ya, selalu dapat pujian. Kamu pasti disayang dosen.",
            "options": [
                {
                    "text": "Akui kerja keras Joko juga",
                    "reply": "Terima kasih, Nata. Aku memang sedang merasa tidak cukup baik.",
                    "rel": {"Joko": 2, "Pak Budi": 1}, "points": 2,
                    "stat": {"leadership": 3}, "resolved": True,
                    "outcome": "Kamu merendahkan hati dan mengangkat temanmu sendiri.",
                },
                {
                    "text": "Membanggakan diri sendiri",
                    "reply": "Ya, karena aku memang berusaha lebih keras.",
                    "rel": {"Joko": -2}, "points": 0,
                    "stat": {}, "resolved": False,
                    "outcome": "Joko menjauh. Persaingan yang tidak sehat mulai tumbuh.",
                },
            ],
        },
    }

    # --------------------------------------------------------------------- #
    #  Mini-game
    # --------------------------------------------------------------------- #
    #  1) Yel-yel: susun kata acak menjadi yel-yel yang benar.
    YELL_PHRASES = [
        "OSPEK UNIMUS SEMANGAT TERUS",
        "TAWAUN KUNCI KEBERHASILAN KITA",
        "DISIPLIN ILMU AMAL BERSAMA",
    ]

    #  2) Teka-teki logika Islami (jawaban berupa angka, dihitung).
    RIDDLES = [
        {
            "question": "Dalam sehari, berapa kali kita menunaikan salat fardu?",
            "answer": 5,
            "hint": "Subuh, Zuhur, Asar, Magrib, Isya.",
            "explain": "Salat fardu ada 5 waktu dalam sehari.",
        },
        {
            "question": "Berapa jumlah rakaat salat Magrib?",
            "answer": 3,
            "hint": "Lebih sedikit dari Zuhur.",
            "explain": "Salat Magrib berjumlah 3 rakaat.",
        },
        {
            "question": "Berapa jumlah rukun Islam?",
            "answer": 5,
            "hint": "Sama dengan jumlah salat fardu.",
            "explain": "Rukun Islam ada 5: syahadat, salat, zakat, puasa, haji.",
        },
    ]

    #  3) Tebak ayat/hadits: pilih lanjutan yang benar.
    AYAT_QUESTIONS = [
        {
            "q": "Lanjutan dari \"Fa inna ma'al usri...\" adalah?",
            "options": ["Yusra", "Sabra", "Amra", "Khair"],
            "answer": 0,
            "explain": "\"Fa inna ma'al usri yusra\" — sesungguhnya bersama kesulitan ada kemudahan (QS. Al-Insyirah: 6).",
        },
        {
            "q": "\"Innamal a'malu binniyat\" artinya?",
            "options": [
                "Sesungguhnya amal itu tergantung niatnya",
                "Sesungguhnya sabar itu indah",
                "Sesungguhnya ilmu itu cahaya",
                "Sesungguhnya sedekah itu berkah",
            ],
            "answer": 0,
            "explain": "Hadis riwayat Bukhari-Muslim: setiap amal tergantung niatnya.",
        },
        {
            "q": "\"Man jadda wa jada\" artinya?",
            "options": [
                "Barang siapa bersungguh-sungguh, ia akan berhasil",
                "Barang siapa bersabar, ia akan mulia",
                "Barang siapa belajar, ia akan pintar",
                "Barang siapa bersedekah, ia akan kaya",
            ],
            "answer": 0,
            "explain": "Pepatah: siapa bersungguh-sungguh pasti akan berhasil.",
        },
    ]

    # --------------------------------------------------------------------- #
    #  Data peserta lain (untuk papan skor / ranking)
    # --------------------------------------------------------------------- #
    #  Skor tetap supaya pemain bisa membandingkan posisinya.
    #  Dikalibrasi terhadap rata-rata skor pemain (~50) agar persaingan ketat.
    OTHER_PARTICIPANTS = [
        {"name": "Rizky",  "base": 62},
        {"name": "Salma",  "base": 55},
        {"name": "Fajar",  "base": 47},
        {"name": "Nabila", "base": 39},
        {"name": "Hendra", "base": 30},
        {"name": "Tiara",  "base": 21},
    ]

    POSITION_XALIGN = {"left": 0.0, "center": 0.5, "right": 1.0}

    def show_character(char_id, position="center"):
        """Tampilkan gambar karakter di layar.

        Menggantikan fungsi lama yang dipanggil tetapi tidak pernah
        didefinisikan (penyebab error pada label navigasi_bebas).
        """
        info = CHARACTER_INFO.get(char_id)
        if not info:
            return
        xalign = POSITION_XALIGN.get(position, 0.5)
        renpy.show(info["image"], at_list=[Transform(xalign=xalign, yalign=1.0)])

    def interact(char_id, topic="obrolan santai"):
        """Obrolan bebas dengan karakter (dipakai di mode jelajah bebas)."""
        info = CHARACTER_INFO.get(char_id)
        if not info:
            return
        lines = CHARACTER_DIALOGUES.get(char_id, ["..."])
        renpy.say(info["name"], random.choice(lines))

    # --------------------------------------------------------------------- #
    #  Aktivitas harian (sistem hari + stamina)
    # --------------------------------------------------------------------- #
    #  cost   = stamina yang berkurang
    #  points = poin ospek
    #  effects= kenaikan stat
    #  rel    = kenaikan kedekatan dengan karakter tertentu
    ACTIVITIES = {
        "seminar": {
            "label": "Mengikuti seminar kepemimpinan",
            "cost": 25,
            "points": 2,
            "effects": {"leadership": 5, "religious_knowledge": 10},
            "rel": {"Pak Budi": 1},
            "result": "Kamu menyimak materi kepemimpinan dengan saksama dan mencatat banyak hal baru.",
        },
        "kompetisi": {
            "label": "Ikut lomba akademik",
            "cost": 35,
            "points": 3,
            "effects": {"academic_potential": 10, "discipline": 5},
            "rel": {"Joko": 1},
            "result": "Kamu berjuang keras dalam lomba dan mendapat pengalaman berharga.",
        },
        "diskusi_keagamaan": {
            "label": "Diskusi keagamaan (AIK)",
            "cost": 20,
            "points": 2,
            "effects": {"religious_knowledge": 15, "leadership": 3},
            "rel": {"Pak Budi": 1, "Rina": 1},
            "result": "Diskusi berjalan hangat; pemahamanmu tentang nilai Islam bertambah.",
        },
        "olahraga": {
            "label": "Olahraga bersama",
            "cost": 20,
            "points": 1,
            "effects": {"discipline": 6},
            "rel": {"Andi": 1},
            "result": "Tubuhmu segar dan semangatmu kembali setelah berolahraga.",
        },
        "bantu_teman": {
            "label": "Membantu teman yang kesulitan",
            "cost": 15,
            "points": 1,
            "effects": {"leadership": 2},
            "rel": {"Momogi": 1, "Rina": 1},
            "result": "Kamu menolong teman yang kesulitan — nilai ta'awun yang nyata.",
        },
        "istirahat": {
            "label": "Istirahat di asrama",
            "cost": 0,
            "points": 0,
            "effects": {"stamina": 30},
            "rel": {},
            "result": "Kamu memulihkan tenaga untuk hari-hari berikutnya.",
        },
    }

    # --------------------------------------------------------------------- #
    #  Bank soal kuis AIK (Al-Islam & Kemuhammadiyahan)
    # --------------------------------------------------------------------- #
    QUIZ_QUESTIONS = [
        {
            "q": "Apa arti dari 'fastabiqul khairat'?",
            "options": [
                "Berlomba-lomba dalam kebaikan",
                "Berbuat baik kepada sesama",
                "Menuntut ilmu agama",
                "Menjaga persaudaraan",
            ],
            "answer": 0,
            "explain": "'Fastabiqul khairat' berarti berlomba-lomba dalam kebaikan (QS. Al-Baqarah: 148).",
        },
        {
            "q": "Siapa pendiri Muhammadiyah?",
            "options": [
                "K.H. Ahmad Dahlan",
                "K.H. Hasyim Asy'ari",
                "Buya Hamka",
                "K.H. Wahid Hasyim",
            ],
            "answer": 0,
            "explain": "Muhammadiyah didirikan oleh K.H. Ahmad Dahlan pada 18 November 1912 di Yogyakarta.",
        },
        {
            "q": "Apa makna 'ta'awun' dalam ajaran Islam?",
            "options": [
                "Saling tolong-menolong dalam kebaikan",
                "Bersaing dalam hal dunia",
                "Menahan diri dari makan",
                "Menuntut balas",
            ],
            "answer": 0,
            "explain": "'Ta'awun' berarti saling tolong-menolong dalam kebaikan dan takwa (QS. Al-Ma'idah: 2).",
        },
        {
            "q": "Amal usaha Muhammadiyah di bidang pendidikan disebut...",
            "options": [
                "Perguruan Muhammadiyah",
                "Pondok Pesantren",
                "Majelis Tarjih",
                "Baitul Mal",
            ],
            "answer": 0,
            "explain": "Muhammadiyah membangun banyak sekolah dan perguruan tinggi sebagai amal usaha pendidikan.",
        },
        {
            "q": "Sifat amanah dalam kepemimpinan berarti...",
            "options": [
                "Dapat dipercaya dan bertanggung jawab",
                "Berani mengambil untung",
                "Selalu menang sendiri",
                "Menghindari tugas",
            ],
            "answer": 0,
            "explain": "Amanah berarti dapat dipercaya; pemimpin bertanggung jawab atas apa yang dipimpinnya.",
        },
    ]

    # --------------------------------------------------------------------- #
    #  Label ramah-pemain untuk pencapaian (achievements)
    # --------------------------------------------------------------------- #
    ACHIEVEMENT_INFO = {
        "master_leadership":          ("Jiwa Pemimpin", "Stat kepemimpinan mencapai 90."),
        "master_discipline":          ("Disiplin Tinggi", "Stat kedisiplinan mencapai 90."),
        "master_religious_knowledge": ("Paham AIK", "Pengetahuan Al-Islam & Kemuhammadiyahan mencapai 90."),
        "master_academic_potential":  ("Cendekia Muda", "Potensi akademik mencapai 90."),
        "quiz_perfect":               ("Ahli AIK", "Menjawab benar semua soal kuis AIK."),
        "Andi_close_friend":          ("Sahabat Andi", "Kedekatan dengan Andi mencapai 8."),
        "Momogi_close_friend":        ("Sahabat Momogi", "Kedekatan dengan Momogi mencapai 8."),
        "Rina_close_friend":          ("Sahabat Rina", "Kedekatan dengan Rina mencapai 8."),
        "Joko_close_friend":          ("Sahabat Joko", "Kedekatan dengan Joko mencapai 8."),
        "Pak Budi_close_friend":      ("Dekat dengan Pak Budi", "Kedekatan dengan Pak Budi mencapai 8."),
        "Sari_close_friend":          ("Dekat dengan Kak Sari", "Kedekatan dengan Sari mencapai 8."),
        "Dimas_close_friend":         ("Sahabat Sekamar", "Kedekatan dengan Dimas mencapai 8."),
        "Bu Ratna_close_friend":      ("Dibimbing Bu Ratna", "Kedekatan dengan Bu Ratna mencapai 8."),
        "jalur_informatika":          ("Calon Programmer", "Menyelesaikan tantangan jalur Teknik Informatika."),
        "jalur_manajemen":            ("Calon Pemimpin", "Menyelesaikan tantangan jalur Manajemen."),
        "jalur_kesehatan":            ("Calon Tenaga Kesehatan", "Menyelesaikan tantangan jalur Kesehatan."),
        "minigame_sempurna":          ("Juara Mini-game", "Mendapat skor sempurna di semua mini-game."),
        "pendamai":                   ("Pendamai", "Menyelesaikan semua konflik dengan damai."),
        "peringkat_1":                ("Juara Umum Ospek", "Meraih peringkat 1 pada papan skor akhir."),
        "peringkat_3":                ("Papan Atas", "Meraih peringkat 3 besar pada papan skor akhir."),
    }

    # --------------------------------------------------------------------- #
    #  Tracker progres ospek
    # --------------------------------------------------------------------- #
    class OspekProgressTracker:
        """Menyimpan seluruh progres ospek: poin, hubungan, stat, hari."""

        MAX_STAT = 100
        NIGHT_RECOVERY = 15   # pemulihan stamina otomatis tiap malam
        LOW_STAMINA = 20      # di bawah ini hanya boleh istirahat

        def __init__(self):
            self.ospek_points = 0
            self.friend_relationship = {
                "Andi":     {"score": 0, "background": "Aktivis mahasiswa dengan semangat tinggi"},
                "Momogi":   {"score": 0, "background": "Mahasiswa perantauan dengan cita-cita besar"},
                "Rina":     {"score": 0, "background": "Aktivis kesehatan dan kemanusiaan"},
                "Joko":     {"score": 0, "background": "Senior tegas dengan nilai keagamaan kuat"},
                "Pak Budi": {"score": 0, "background": "Pembimbing spiritual dengan pengalaman luas"},
                "Sari":     {"score": 0, "background": "Kakak senior yang ramah dan suka membantu"},
                "Dimas":    {"score": 0, "background": "Teman sekamar yang ceria dan solid"},
                "Bu Ratna": {"score": 0, "background": "Dosen pembimbing yang bijaksana"},
            }

            self.stats = {
                "stamina": 100,
                "leadership": 0,
                "discipline": 0,
                "religious_knowledge": 0,
                "academic_potential": 0,
            }

            self.current_major = None
            self.quiz_score = 0
            self.quiz_total = 0
            self.achievements = []
            self.daily_schedule = []
            self.conflicts = []
            self.day_log = []          # catatan aktivitas tiap hari
            self.event_log = []        # id event acak yang pernah terjadi

            # --- gameplay baru ---
            self.conflict_log = []     # {id, choice, resolved}
            self.minigame_scores = {   # skor tiap mini-game
                "yel_yel": 0,
                "teka_teki": 0,
                "ayat": 0,
            }
            self.minigame_max = {
                "yel_yel": 3,
                "teka_teki": 3,
                "ayat": 3,
            }

            self.current_day = 1
            self.total_ospek_days = 7

        # ---------------------------------------------------------------- #
        #  Properti bantu (untuk HUD)
        # ---------------------------------------------------------------- #
        @property
        def stamina(self):
            return self.stats["stamina"]

        @property
        def is_finished(self):
            return self.current_day > self.total_ospek_days

        @property
        def days_left(self):
            return max(0, self.total_ospek_days - self.current_day + 1)

        # ---------------------------------------------------------------- #
        #  Validasi
        # ---------------------------------------------------------------- #
        def _validate_input(self, character=None, stat_name=None):
            if character and character not in self.friend_relationship:
                raise ValueError("Unknown character: {}".format(character))
            if stat_name and stat_name not in self.stats:
                raise ValueError("Unknown stat: {}".format(stat_name))

        # ---------------------------------------------------------------- #
        #  Hubungan & stat
        # ---------------------------------------------------------------- #
        def update_relationship(self, character, points):
            self._validate_input(character=character)
            current = self.friend_relationship[character]["score"]
            new_score = max(0, min(current + points, 10))
            self.friend_relationship[character]["score"] = new_score
            self._check_relationship_milestone(character, new_score)

        def _check_relationship_milestone(self, character, score):
            if score >= 8:
                self.add_achievement("{}_close_friend".format(character))

        def add_ospek_points(self, points):
            self.ospek_points += points

        def set_major(self, major):
            self.current_major = major

        def update_stat(self, stat_name, points):
            self._validate_input(stat_name=stat_name)
            current = self.stats[stat_name]
            new_value = max(0, min(current + points, self.MAX_STAT))
            self.stats[stat_name] = new_value
            self._check_stat_achievement(stat_name)

        def _check_stat_achievement(self, stat_name):
            # 'stamina' tidak dihitung: nilainya sudah 100 sejak awal.
            if stat_name == "stamina":
                return
            if self.stats[stat_name] >= 90:
                self.add_achievement("master_{}".format(stat_name))

        def add_achievement(self, key):
            """Tambahkan pencapaian (sekali saja)."""
            if key not in self.achievements:
                self.achievements.append(key)

        def achievement_list(self):
            """Daftar (judul, keterangan) pencapaian yang sudah didapat."""
            result = []
            for key in self.achievements:
                info = ACHIEVEMENT_INFO.get(key)
                if info:
                    result.append(info)
                else:
                    result.append((key.replace("_", " ").title(), ""))
            return result

        def achievement_max(self):
            """Jumlah maksimum pencapaian yang mungkin diraih.

            Sebagian pencapaian dibuat otomatis ("{nama}_close_friend",
            "master_{stat}") dan sebagian sudah terdaftar di ACHIEVEMENT_INFO.
            Ambil gabungannya supaya tidak terhitung dua kali.
            """
            mungkin = set(ACHIEVEMENT_INFO)
            mungkin |= {"{}_close_friend".format(c) for c in self.friend_relationship}
            mungkin |= {"master_{}".format(s) for s in self.stats if s != "stamina"}
            return len(mungkin)

        def add_conflict(self, conflict_description):
            if conflict_description not in self.conflicts:
                self.conflicts.append(conflict_description)

        # ---------------------------------------------------------------- #
        #  Konflik antar-teman
        # ---------------------------------------------------------------- #
        def resolve_conflict(self, conflict_id, option_index):
            """Terapkan pilihan pemain pada sebuah konflik."""
            conflict = CONFLICTS[conflict_id]
            if not (0 <= option_index < len(conflict["options"])):
                raise ValueError("Opsi konflik tidak valid: {}".format(option_index))
            option = conflict["options"][option_index]

            for char, delta in option.get("rel", {}).items():
                self.update_relationship(char, delta)
            for stat, delta in option.get("stat", {}).items():
                self.update_stat(stat, delta)
            self.add_ospek_points(option.get("points", 0))

            resolved = option.get("resolved", False)
            self.conflict_log.append({
                "id": conflict_id,
                "title": conflict["title"],
                "choice": option["text"],
                "resolved": resolved,
            })
            self.add_conflict(conflict["title"])
            return resolved

        def conflicts_resolved(self):
            return sum(1 for c in self.conflict_log if c["resolved"])

        def conflicts_total(self):
            return len(self.conflict_log)

        # ---------------------------------------------------------------- #
        #  Mini-game
        # ---------------------------------------------------------------- #
        def add_minigame_score(self, game, points):
            """Tambah skor mini-game + poin ospek sepadan.

            Skor dibatasi pada nilai maksimum tiap mini-game supaya tidak bisa
            melampaui 100% bila mini-game diulang (mis. saat uji/debug).
            """
            if game not in self.minigame_scores:
                return
            maks = self.minigame_max.get(game, 0)
            sebelum = self.minigame_scores[game]
            sesudah = min(sebelum + points, maks)
            self.minigame_scores[game] = sesudah
            # Poin ospek hanya untuk kenaikan nyata (tidak bisa di-farm).
            self.add_ospek_points(max(0, sesudah - sebelum))

        def minigame_total(self):
            return sum(self.minigame_scores.values())

        def minigame_max_total(self):
            return sum(self.minigame_max.values())

        def finish_minigames(self):
            """Beri pencapaian bila semua mini-game sempurna."""
            if all(self.minigame_scores[g] >= self.minigame_max[g]
                   for g in self.minigame_scores):
                self.add_achievement("minigame_sempurna")

        # ---------------------------------------------------------------- #
        #  Nilai & ranking
        # ---------------------------------------------------------------- #
        def category_scores(self):
            """Nilai per kategori (0-100) untuk rapor ospek."""
            rel = self.total_relationship_score()
            rel_max = 10 * len(self.friend_relationship)
            cats = {
                "Poin Ospek": min(100, self.ospek_points * 4),
                "Kedekatan": int(round(rel / rel_max * 100)) if rel_max else 0,
                "Kuis AIK": int(round(self.quiz_score / self.quiz_total * 100)) if self.quiz_total else 0,
                "Mini-game": int(round(self.minigame_total() / self.minigame_max_total() * 100)) if self.minigame_max_total() else 0,
                "Konflik": int(round(self.conflicts_resolved() / self.conflicts_total() * 100)) if self.conflicts_total() else 100,
            }
            # Semua kategori wajib berada di rentang 0-100.
            return {k: max(0, min(100, v)) for k, v in cats.items()}

        def overall_score(self):
            """Skor akhir 0-100 dari rata-rata kategori."""
            cats = self.category_scores()
            if not cats:
                return 0
            return int(round(sum(cats.values()) / len(cats)))

        def leaderboard(self):
            """Daftar (nama, skor, is_player) terurut menurun."""
            rows = [(p["name"], p["base"], False) for p in OTHER_PARTICIPANTS]
            rows.append(("Nata (kamu)", self.overall_score(), True))
            rows.sort(key=lambda r: -r[1])
            return rows

        def player_rank(self):
            """(peringkat, total peserta) untuk pemain."""
            rows = self.leaderboard()
            for i, (name, score, is_player) in enumerate(rows):
                if is_player:
                    return (i + 1, len(rows))
            return (len(rows), len(rows))

        # ---------------------------------------------------------------- #
        #  Sistem hari + stamina
        # ---------------------------------------------------------------- #
        def available_activities(self):
            """Daftar aktivitas yang boleh dipilih hari ini.

            Hanya kegiatan yang staminanya cukup yang ditawarkan, supaya
            pemain tidak membuang satu hari untuk kegiatan yang gagal.
            'istirahat' selalu tersedia.
            """
            stamina = self.stats["stamina"]
            if stamina < self.LOW_STAMINA:
                return ["istirahat"]
            choices = [
                key for key, act in ACTIVITIES.items()
                if key != "istirahat" and act["cost"] <= stamina
            ]
            choices.append("istirahat")
            return choices

        def do_activity(self, key):
            """Jalankan aktivitas harian. Kembalikan dict hasil."""
            if key not in ACTIVITIES:
                raise ValueError("Unknown activity: {}".format(key))
            act = ACTIVITIES[key]

            if act["cost"] > self.stats["stamina"]:
                return {"ok": False, "reason": "stamina", "activity": act}

            if act["cost"]:
                self.update_stat("stamina", -act["cost"])
            for stat, value in act["effects"].items():
                self.update_stat(stat, value)
            for char, value in act.get("rel", {}).items():
                self.update_relationship(char, value)
            self.add_ospek_points(act["points"])

            self.daily_schedule.append(key)
            self.day_log.append({"day": self.current_day, "activity": key})
            return {"ok": True, "activity": act}

        def end_day(self):
            """Tutup hari: pemulihan malam + naikkan hari."""
            self.update_stat("stamina", self.NIGHT_RECOVERY)
            self.current_day += 1

        def day_summary(self, day):
            """Ringkasan aktivitas pada satu hari tertentu (untuk catatan harian)."""
            entries = [e for e in self.day_log if e["day"] == day]
            if not entries:
                return "Tidak ada kegiatan tercatat."
            key = entries[-1]["activity"]
            act = ACTIVITIES.get(key)
            if not act:
                return "Tidak ada kegiatan tercatat."
            return "{}  (Poin +{})".format(act["label"], act["points"])

        def schedule_summary(self):
            """Daftar (hari, ringkasan) seluruh kegiatan selama ospek."""
            rows = []
            for day in range(1, self.total_ospek_days + 1):
                if any(e["day"] == day for e in self.day_log):
                    rows.append((day, self.day_summary(day)))
            return rows

        def closest_friend(self):
            """(nama, skor) teman dengan kedekatan tertinggi; None jika semua 0."""
            name, data = self.best_friend()
            if data["score"] <= 0:
                return None
            return (name, data["score"])

        def apply_random_event(self, event):
            """Terapkan efek satu event acak (dict dari RANDOM_EVENTS)."""
            if not event:
                return
            rel = event.get("rel")
            if rel:
                self.update_relationship(rel["char"], rel["amount"])
            stat = event.get("stat")
            if stat:
                self.update_stat(stat["stat"], stat["amount"])
            points = event.get("points")
            if points:
                self.add_ospek_points(points["amount"])
            self.event_log.append(event.get("id", "event"))

        # ---------------------------------------------------------------- #
        #  Kuis
        # ---------------------------------------------------------------- #
        def answer_quiz(self, correct):
            self.quiz_total += 1
            if correct:
                self.quiz_score += 1
                self.add_ospek_points(1)
                self.update_stat("religious_knowledge", 5)
            return self.quiz_score

        def finish_quiz(self):
            """Dipanggil setelah seluruh soal kuis dijawab."""
            if self.quiz_total and self.quiz_score == self.quiz_total:
                self.add_achievement("quiz_perfect")

        # ---------------------------------------------------------------- #
        #  Evaluasi akhir & ending
        # ---------------------------------------------------------------- #
        def total_relationship_score(self):
            return sum(r["score"] for r in self.friend_relationship.values())

        def best_friend(self):
            return max(self.friend_relationship.items(), key=lambda kv: kv[1]["score"])

        def calculate_final_grade(self):
            total_score = (
                self.ospek_points * 3.0
                + self.total_relationship_score() * 1.5
                + sum(v for k, v in self.stats.items() if k != "stamina") * 0.4
            )
            grade_mapping = [
                (60, "Mahasiswa Inspiratif"),
                (40, "Mahasiswa Berprestasi"),
                (20, "Mahasiswa Potensial"),
            ]
            for threshold, grade in grade_mapping:
                if total_score >= threshold:
                    return grade
            return "Perlu Pengembangan Diri"

        def get_ending(self):
            """Tentukan ending berdasarkan poin, hubungan, stat, dan konflik.

            Ambang dikalibrasi agar tiap cabang bisa dicapai dalam 7 hari:
            - jalur "poin"  : fokus kompetisi/seminar/mini-game -> poin tinggi
            - jalur "sosial": fokus diskusi/bantu teman -> rel tinggi
            """
            pts = self.ospek_points
            rel_total = self.total_relationship_score()
            c_total = self.conflicts_total()
            c_resolved = self.conflicts_resolved()

            # Konflik yang gagal diselesaikan semuanya menutup ending terbaik.
            konflik_buruk = c_total >= 2 and c_resolved == 0

            if pts >= 24 and rel_total >= 14 and not konflik_buruk:
                return (
                    "ENDING: SAHABAT SEPANJANG MASA",
                    "Kamu menjadi mahasiswa teladan sekaligus sahabat sejati bagi teman-teman ospekmu.",
                )
            if konflik_buruk and rel_total < 14:
                return (
                    "ENDING: JALAN SENDIRI",
                    "Kamu unggul dalam kegiatan, tetapi banyak hubungan yang renggang karena konflik tak terselesaikan.",
                )
            if pts >= 24:
                return (
                    "ENDING: MAHASISWA INSPIRATIF",
                    "Prestasimu menonjol, meski kamu masih perlu lebih dekat dengan teman-teman.",
                )
            if rel_total >= 14:
                return (
                    "ENDING: SAHABAT SEJATI",
                    "Kamu mungkin bukan yang paling menonjol, tetapi persahabatanmu sangat kuat.",
                )
            if pts >= 19:
                return (
                    "ENDING: MAHASISWA BERPRESTASI",
                    "Kamu aktif dan berprestasi selama ospek. Terus pertahankan!",
                )
            if pts >= 12:
                return (
                    "ENDING: MAHASISWA POTENSIAL",
                    "Kamu menunjukkan potensi yang baik. Masih banyak ruang untuk tumbuh.",
                )
            return (
                "ENDING: PERLU PENGEMBANGAN DIRI",
                "Ospek ini menjadi awal belajar. Jangan berhenti berusaha memperbaiki diri.",
            )

        @staticmethod
        def get_relationship_status(score):
            status_mapping = [
                (8, "Sahabat Sejati"),
                (5, "Teman Dekat"),
                (3, "Kenalan Baik"),
                (0, "Baru Kenal"),
            ]
            for threshold, status in status_mapping:
                if score >= threshold:
                    return status
            return "Baru Kenal"


# Global tracker
default ospek_tracker = OspekProgressTracker()


# ------------------------------------------------------------------------- #
#  Karakter
# ------------------------------------------------------------------------- #
define e = Character("Nata", who_color="#3498db")
define a = Character("Andi", who_color="#2ecc71")
define l = Character("Momogi", who_color="#e74c3c")
define p = Character("Pak Budi", who_color="#f39c12")
define r = Character("Rina", who_color="#9b59b6")
define j = Character("Joko", who_color="#1abc9c")
# --- karakter baru ---
define s = Character("Sari", who_color="#e67e22")
define d = Character("Dimas", who_color="#16a085")
define br = Character("Bu Ratna", who_color="#8e44ad")

# ------------------------------------------------------------------------- #
#  Gambar karakter
# ------------------------------------------------------------------------- #
image nata = "images/characters/nata.png"
image andi = "images/characters/andi.png"
image momogi = "images/characters/momogi.png"
image pak_budi = "images/characters/pak_budi.png"
image rina = "images/characters/rina.png"
image joko = "images/characters/joko.png"
# --- karakter baru ---
image sari = "images/characters/sari.png"
image dimas = "images/characters/dimas.png"
image bu_ratna = "images/characters/bu_ratna.png"

# ------------------------------------------------------------------------- #
#  Background & audio
# ------------------------------------------------------------------------- #
image bg welcome = "images/campus_entrance.jpg"
image bg ospek_hall = "images/ospek_main_hall.jpg"
image bg lecture_room = "images/lecture_room.jpg"
image bg student_center = "images/student_center.jpg"
image bg welcome_night = "images/welcome_night.jpg"

image bg kampus_depan = "images/campus_entrance.jpg"
image bg aula_ospek = "images/ospek_main_hall.jpg"
image bg ruang_kuliah = "images/lecture_room.jpg"
image bg pusat_mahasiswa = "images/student_center.jpg"

# --- background baru (placeholder, silakan ganti dengan foto asli) ---
image bg kantin = "images/kantin.jpg"
image bg perpustakaan = "images/perpustakaan.jpg"
image bg masjid = "images/masjid.jpg"
image bg lab_komputer = "images/lab_komputer.jpg"
image bg ruang_seminar = "images/ruang_seminar.jpg"
image bg lab_kesehatan = "images/lab_kesehatan.jpg"

define audio.ospek_theme = "audio/ospek_welcome.mp3"
define audio.challenge_theme = "audio/challenge_theme.mp3"
define audio.quiz_theme = "audio/quiz_theme.mp3"
define audio.end_theme = "audio/end_theme.mp3"


# ------------------------------------------------------------------------- #
#  HUD (hari / stamina / poin)
# ------------------------------------------------------------------------- #
screen hud():
    zorder 100
    frame:
        align (0.0, 0.0)
        xoffset 15
        yoffset 15
        padding (18, 12)
        background "#000000aa"
        vbox:
            spacing 3
            text "Hari [ospek_tracker.current_day]/[ospek_tracker.total_ospek_days]" size 22 color "#ffffff"
            text "Stamina: [ospek_tracker.stamina]%" size 22 color "#ffffff"
            text "Poin Ospek: [ospek_tracker.ospek_points]" size 22 color "#ffffff"
            null height 4
            textbutton "Pencapaian ★" action Show("achievements")
            textbutton "Papan Skor 🏆" action Show("leaderboard")


# ------------------------------------------------------------------------- #
#  Layar Pencapaian (achievements)
# ------------------------------------------------------------------------- #
screen achievements():
    modal True
    zorder 200

    add "#000000cc"

    frame:
        align (0.5, 0.5)
        xpadding 40
        ypadding 30
        xmaximum 900
        background "#1b1b1bf2"

        vbox:
            spacing 14

            text "PENCAPAIAN" size 40 color "#f1c40f" xalign 0.5

            $ _ach = ospek_tracker.achievement_list()

            if _ach:
                for _title, _desc in _ach:
                    hbox:
                        spacing 12
                        text "★" size 26 color "#f1c40f" yalign 0.0
                        vbox:
                            spacing 2
                            text _title size 26 color "#ffffff"
                            if _desc:
                                text _desc size 20 color "#bbbbbb"
            else:
                text "Belum ada pencapaian. Teruslah berusaha!" size 24 color "#bbbbbb" xalign 0.5

            null height 6

            textbutton "Tutup" action Hide("achievements") xalign 0.5


# ------------------------------------------------------------------------- #
#  Cerita
# ------------------------------------------------------------------------- #
label start:
    $ ospek_tracker = OspekProgressTracker()

    scene bg welcome with dissolve
    play music ospek_theme fadein 2.0 loop

    "Pagi yang cerah di Universitas Muhammadiyah Semarang (Unimus)."

    show nata at center
    e "Deg-degan rasanya. Ini pertama kalinya aku masuk kampus setelah berbulan-bulan mempersiapkan diri. Aku berharap bisa menjalani ospek dengan baik."

    scene bg ospek_hall with fade
    show pak_budi at center
    p "Selamat datang di Universitas Muhammadiyah Semarang. Ospek ini tidak hanya tentang belajar akademik, tapi juga memperkenalkanmu pada nilai-nilai Islam yang akan membimbing hidupmu."

    show andi at left
    show momogi at right
    a "Ospek di Unimus memang penuh tantangan, Nata. Tapi, kita akan belajar banyak di sini."
    l "Kita akan menghadapi berbagai tantangan yang tidak hanya menguji pengetahuan, tapi juga karakter kita."
    hide momogi
    show rina at right
    r "Semuanya akan lebih mudah jika kita saling mendukung. Jangan ragu untuk berbagi dan belajar bersama."
    hide rina
    hide andi

    # ------------------------------------------------------------------ #
    #  Pemilihan jurusan
    # ------------------------------------------------------------------ #
    show pak_budi at center
    p "Nata, jurusan apa yang kamu pilih?"

    menu:
        "Teknik Informatika":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.set_major("Teknik Informatika")
            $ ospek_tracker.update_relationship("Andi", 2)
            show nata at left
            show andi at right
            e "Teknik Informatika adalah pilihanku!"
            a "Keren! Semoga kita bisa berkontribusi lewat teknologi yang mendukung nilai-nilai Islam."
            hide andi
            hide nata

        "Manajemen":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.set_major("Manajemen")
            $ ospek_tracker.update_relationship("Momogi", 2)
            show nata at left
            show momogi at right
            e "Aku memilih Manajemen."
            l "Bagus! Kita akan belajar bagaimana menjadi pemimpin yang amanah."
            hide momogi
            hide nata

        "Kesehatan":
            $ ospek_tracker.add_ospek_points(1)
            $ ospek_tracker.set_major("Kesehatan")
            $ ospek_tracker.update_relationship("Rina", 1)
            show nata at left
            show rina at right
            e "Aku memilih Kesehatan."
            r "Selamat datang di prodi Kesehatan! Islam juga mengajarkan pentingnya menjaga kesehatan tubuh dan jiwa."
            hide rina
            hide nata

    show pak_budi at center
    p "Baiklah. Ospek berlangsung selama 7 hari. Aturlah tenagamu dengan bijak — setiap hari kamu hanya bisa melakukan satu kegiatan utama."
    hide pak_budi

    # Sapaan singkat bernuansa jurusan
    if ospek_tracker.current_major == "Teknik Informatika":
        show andi at center
        a "Sebagai anak Informatika, kita akan banyak berkutat di lab komputer. Siap?"
        hide andi
    elif ospek_tracker.current_major == "Manajemen":
        show momogi at center
        l "Anak Manajemen harus siap memimpin. Kita akan banyak berlatih presentasi!"
        hide momogi
    elif ospek_tracker.current_major == "Kesehatan":
        show rina at center
        r "Anak Kesehatan akan belajar banyak di lab. Ilmu kita untuk menolong sesama."
        hide rina

    jump day_loop


# ------------------------------------------------------------------------- #
#  Loop harian
# ------------------------------------------------------------------------- #
label day_loop:
    if ospek_tracker.is_finished:
        jump final_evaluation

    $ day = ospek_tracker.current_day

    scene bg ospek_hall with dissolve
    show screen hud

    # Perhatian: JANGAN menulis "[ Hari [day] ... ]" — kurung siku bersarang
    # membuat Ren'Py mengevaluasi seluruh isinya sebagai ekspresi Python dan
    # gagal dengan SyntaxError. Gunakan satu tingkat kurung saja.
    "Hari [day] dari [ospek_tracker.total_ospek_days]"

    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show pak_budi at center
        p "Kamu terlihat lelah, Nata. Sebaiknya istirahat dulu hari ini agar tidak tumbang."
        hide pak_budi

    # Event acak (tidak pada hari event utama 3 & 5)
    if day != 3 and day != 5:
        call random_event
        show screen hud

    menu:
        "Pilih kegiatan hari ini":
            jump day_activity

        "Jelajah kampus & bicara dengan teman":
            call navigasi_bebas
            jump day_loop


label day_activity:
    python:
        while True:
            _items = []
            for _key in ospek_tracker.available_activities():
                _act = ACTIVITIES[_key]
                if _act["cost"]:
                    _items.append(("{}  (Stamina -{})".format(_act["label"], _act["cost"]), _key))
                else:
                    _items.append((_act["label"], _key))
            _items.append(("Lihat catatan harian", "__log__"))
            _chosen = renpy.display_menu(_items)
            if _chosen != "__log__":
                break
            _rows = ospek_tracker.schedule_summary()
            if _rows:
                for _d, _txt in _rows:
                    renpy.say(None, "Hari {}: {}".format(_d, _txt))
            else:
                renpy.say(None, "Belum ada kegiatan tercatat.")

    $ _result = ospek_tracker.do_activity(_chosen)

    if _result["ok"]:
        $ _act = _result["activity"]
        $ _text = _act["result"]
        $ _gain = _act["points"]
        scene bg lecture_room with dissolve
        "[_text]"
        hide screen hud
        $ renpy.say(None, "Poin ospek: +{}".format(_gain))
        show screen hud
    else:
        "Tenagamu tidak cukup untuk kegiatan itu. Kamu memilih beristirahat."

    # ---------------- Event khusus per hari ---------------- #
    if day == 3:
        call kuis_aik
    elif day == 4:
        call jalur_jurusan
    elif day == 5:
        call tantangan_tim
    elif day == 6:
        call konflik_antar_teman
        call minigame_session
    elif day == 7:
        call konflik_antar_teman

    $ ospek_tracker.end_day()

    hide screen hud
    if ospek_tracker.is_finished:
        jump final_evaluation

    "Malam pun tiba. Kamu beristirahat untuk menyambut hari berikutnya."
    jump day_loop


# ------------------------------------------------------------------------- #
#  Event: kuis AIK (multi-soal)
# ------------------------------------------------------------------------- #
label kuis_aik:
    scene bg lecture_room with dissolve
    play music quiz_theme fadein 2.0 loop
    show pak_budi at center
    p "Hari ini kita uji pemahamanmu tentang Al-Islam dan Kemuhammadiyahan. Jawablah dengan tenang."

    python:
        for _qi, _q in enumerate(QUIZ_QUESTIONS):
            renpy.say("Pak Budi", "Soal {} dari {}.\n{}".format(_qi + 1, len(QUIZ_QUESTIONS), _q["q"]))
            _pick = renpy.display_menu([(opt, _i) for _i, opt in enumerate(_q["options"])])
            _correct = (_pick == _q["answer"])
            ospek_tracker.answer_quiz(_correct)
            if _correct:
                renpy.say(None, "Benar! " + _q["explain"])
            else:
                renpy.say(None, "Belum tepat. " + _q["explain"])
        ospek_tracker.finish_quiz()

    p "Skor kuis kamu: [ospek_tracker.quiz_score]/[ospek_tracker.quiz_total]. Ilmu itu cahaya — teruslah belajar."
    hide pak_budi
    return


# ------------------------------------------------------------------------- #
#  Event: tantangan kerja tim
# ------------------------------------------------------------------------- #
label tantangan_tim:
    scene bg student_center with dissolve
    play music challenge_theme fadein 2.0 loop
    show pak_budi at center
    show joko at right
    p "Saatnya tantangan kerja tim! Di sini kita menguji nilai ta'awun (saling tolong-menolong) dan kepemimpinan. Pilihlah dengan bijak!"
    hide pak_budi

    menu:
        "Ambil inisiatif memimpin tim":
            $ ospek_tracker.add_ospek_points(3)
            $ ospek_tracker.update_relationship("Joko", 1)
            $ ospek_tracker.update_relationship("Pak Budi", 2)
            show nata at left
            e "Saya akan memimpin tim ini dan mengatur strategi agar tugas ini selesai dengan baik."
            j "Kepemimpinan itu amanah. Bagus sekali, terus tingkatkan!"

        "Fokus pada peran supportif":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.update_relationship("Andi", 1)
            $ ospek_tracker.update_relationship("Momogi", 1)
            show nata at left
            e "Saya akan mendukung teman-teman dalam menyelesaikan tugas ini."
            j "Kerja tim yang solid! Setiap kontribusi itu bernilai."

        "Mengalah dan mengalahkan ego":
            $ ospek_tracker.add_ospek_points(1)
            $ ospek_tracker.update_relationship("Rina", 2)
            $ ospek_tracker.update_relationship("Joko", 1)
            show nata at left
            e "Saya akan mendengarkan pendapat teman-teman dulu sebelum memutuskan."
            j "Sikap rendah hati itu kekuatan, bukan kelemahan. Bagus."

    hide joko
    hide nata
    return


# ------------------------------------------------------------------------- #
#  Event acak harian
# ------------------------------------------------------------------------- #
label random_event:
    python:
        _ev = random.choice(RANDOM_EVENTS)
        ospek_tracker.apply_random_event(_ev)
    $ _ev_scene = _ev["scene"]
    $ _ev_speaker = CHARACTER_INFO[_ev["speaker"]]["name"]
    $ _ev_line = _ev["line"]
    $ _ev_narr = _ev["narration"]
    scene expression _ev_scene with dissolve
    "[_ev_narr]"
    $ show_character(_ev["speaker"], "center")
    "[_ev_speaker] \"[_ev_line]\""
    python:
        for _k in ("sari", "dimas", "bu_ratna", "andi", "momogi", "rina", "joko", "pak_budi"):
            renpy.hide(CHARACTER_INFO[_k]["image"])
    return


# ------------------------------------------------------------------------- #
#  Jalur cerita per jurusan (event eksklusif hari ke-4)
# ------------------------------------------------------------------------- #
label jalur_jurusan:
    if ospek_tracker.current_major == "Teknik Informatika":
        call jalur_informatika
    elif ospek_tracker.current_major == "Manajemen":
        call jalur_manajemen
    elif ospek_tracker.current_major == "Kesehatan":
        call jalur_kesehatan
    return


label jalur_informatika:
    scene bg lab_komputer with dissolve
    play music challenge_theme fadein 2.0 loop
    show andi at center
    a "Nata, di lab ini kita belajar membuat aplikasi sederhana. Mau coba?"
    e "Tentu! Aku penasaran bagaimana teknologi bisa membantu banyak orang."
    python:
        ospek_tracker.update_relationship("Andi", 2)
        ospek_tracker.update_stat("academic_potential", 8)
        ospek_tracker.add_ospek_points(3)
        ospek_tracker.add_achievement("jalur_informatika")
    a "Kode yang baik itu bukan yang pintar, tapi yang mudah dipahami orang lain."
    "Kamu menghabiskan hari itu dengan menyusun program pertamamu. Rasanya melelahkan tapi menyenangkan."
    hide andi
    return


label jalur_manajemen:
    scene bg ruang_seminar with dissolve
    play music challenge_theme fadein 2.0 loop
    show momogi at center
    l "Nata, kita diminta memimpin rapat kecil. Berani mencoba?"
    e "Ayo! Aku ingin belajar bagaimana mengatur tim dengan baik."
    python:
        ospek_tracker.update_relationship("Momogi", 2)
        ospek_tracker.update_stat("leadership", 8)
        ospek_tracker.add_ospek_points(3)
        ospek_tracker.add_achievement("jalur_manajemen")
    l "Pemimpin yang baik itu mendengar dulu, baru memutuskan. Kamu sudah melakukannya!"
    "Kamu memimpin rapat dengan tenang, mendengar setiap pendapat, lalu mengambil kesimpulan."
    hide momogi
    return


label jalur_kesehatan:
    scene bg lab_kesehatan with dissolve
    play music challenge_theme fadein 2.0 loop
    show rina at center
    r "Nata, di lab ini kita belajar pertolongan pertama. Ini penting untuk menolong sesama."
    e "Aku siap. Ilmu ini pasti berguna, bukan hanya untuk diriku sendiri."
    python:
        ospek_tracker.update_relationship("Rina", 2)
        ospek_tracker.update_stat("discipline", 8)
        ospek_tracker.add_ospek_points(3)
        ospek_tracker.add_achievement("jalur_kesehatan")
    r "Menjaga kesehatan itu bagian dari menjaga amanah dari Allah. Kamu sudah paham."
    "Kamu berlatih pertolongan pertama dengan sungguh-sungguh. Rasanya bermanfaat."
    hide rina
    return


# ------------------------------------------------------------------------- #
#  Konflik antar-teman
# ------------------------------------------------------------------------- #
label konflik_antar_teman:
    python:
        _candidates = [cid for cid in CONFLICTS if cid not in ospek_tracker.conflicts]
        _cid = random.choice(_candidates) if _candidates else random.choice(list(CONFLICTS))
        _conf = CONFLICTS[_cid]
    $ _c_scene = _conf["scene"]
    $ _c_intro = _conf["intro"]
    scene expression _c_scene with dissolve
    "[_c_intro]"
    $ show_character(_conf["speaker"], "center")
    $ _c_speaker = CHARACTER_INFO[_conf["speaker"]]["name"]
    $ _c_line = _conf["line"]
    "[_c_speaker] \"[_c_line]\""

    python:
        _opts = [(o["text"], _i) for _i, o in enumerate(_conf["options"])]
        _pick = renpy.display_menu(_opts)
        _chosen = _conf["options"][_pick]
        _resolved = ospek_tracker.resolve_conflict(_cid, _pick)

    $ _c_reply = _chosen["reply"]
    $ _c_outcome = _chosen["outcome"]
    "[_c_speaker] \"[_c_reply]\""
    hide andi
    hide momogi
    hide rina
    hide joko
    hide pak_budi
    hide sari
    hide dimas
    hide bu_ratna
    "[_c_outcome]"
    if _resolved:
        "Kamu merasa lega — hubungan kalian justru semakin kuat."
    else:
        "Ada beban yang tersisa di hati. Mungkin lain kali bisa lebih baik."
    return


# ------------------------------------------------------------------------- #
#  Mini-game 1: susun yel-yel
# ------------------------------------------------------------------------- #
label mini_yel_yel:
    scene bg ospek_hall with dissolve
    play music challenge_theme fadein 2.0 loop
    show pak_budi at center
    p "Saatnya lomba yel-yel! Susun kata-kata berikut menjadi yel-yel yang benar."
    hide pak_budi

    python:
        _phrase = random.choice(YELL_PHRASES)
        _words = _phrase.split()
        _shuffled = _words[:]
        random.shuffle(_shuffled)
        while len(_shuffled) > 1 and _shuffled == _words:
            random.shuffle(_shuffled)

    $ renpy.say(None, "Kata acak: {}".format(" ".join(_shuffled)))

    python:
        _answer = renpy.input("Susun menjadi yel-yel (huruf kapital):").strip().upper()
        _answer = " ".join(_answer.split())
        _correct = (_answer == _phrase)
        if _correct:
            ospek_tracker.add_minigame_score("yel_yel", 3)
            ospek_tracker.update_stat("leadership", 5)
        else:
            ospek_tracker.add_minigame_score("yel_yel", 1)
            ospek_tracker.update_stat("leadership", 2)

    if _correct:
        "Tepat sekali! Seluruh peserta mengikuti yel-yelmu dengan semangat."
        p "Bagus! Yel-yel itu membangkitkan semangat seluruh angkatan."
    else:
        $ renpy.say(None, "Yel-yel yang benar: {}".format(_phrase))
        p "Hampir! Yang penting semangatnya tetap terjaga."
    hide pak_budi
    return


# ------------------------------------------------------------------------- #
#  Mini-game 2: teka-teki logika Islami
# ------------------------------------------------------------------------- #
label mini_teka_teki:
    scene bg masjid with dissolve
    play music quiz_theme fadein 2.0 loop
    show joko at center
    j "Sebelum istirahat, coba jawab teka-teki singkat ini. Isi dengan angka."
    hide joko

    python:
        _rid = random.choice(RIDDLES)
        renpy.say(None, _rid["question"])
        _raw = renpy.input("Jawabanmu (angka):").strip()
        try:
            _num = int(_raw)
        except ValueError:
            _num = -1
        if _num == _rid["answer"]:
            ospek_tracker.add_minigame_score("teka_teki", 3)
            ospek_tracker.update_stat("religious_knowledge", 6)
            renpy.say(None, "Benar! " + _rid["explain"])
        else:
            ospek_tracker.add_minigame_score("teka_teki", 0)
            renpy.say(None, "Belum tepat. Petunjuk: " + _rid["hint"])
            renpy.say(None, "Jawaban: {} — {}".format(_rid["answer"], _rid["explain"]))
    return


# ------------------------------------------------------------------------- #
#  Mini-game 3: tebak lanjutan ayat / hadis
# ------------------------------------------------------------------------- #
label mini_ayat:
    scene bg masjid with dissolve
    play music quiz_theme fadein 2.0 loop
    show bu_ratna at center
    br "Sekarang kita uji hafalan dan pemahamanmu. Pilih jawaban yang benar."
    hide bu_ratna

    python:
        _q = random.choice(AYAT_QUESTIONS)
        renpy.say("Bu Ratna", _q["q"])
        _pick = renpy.display_menu([(o, _i) for _i, o in enumerate(_q["options"])])
        if _pick == _q["answer"]:
            ospek_tracker.add_minigame_score("ayat", 3)
            ospek_tracker.update_stat("religious_knowledge", 6)
            renpy.say(None, "Benar! " + _q["explain"])
        else:
            ospek_tracker.add_minigame_score("ayat", 0)
            renpy.say(None, "Belum tepat. " + _q["explain"])
    return


# ------------------------------------------------------------------------- #
#  Mini-game gabungan (dipakai sebagai kegiatan hari ke-6)
# ------------------------------------------------------------------------- #
label minigame_session:
    call mini_yel_yel
    call mini_teka_teki
    call mini_ayat
    python:
        ospek_tracker.finish_minigames()
    "Kamu menutup sesi permainan dengan pengalaman yang menyenangkan."
    return


# ------------------------------------------------------------------------- #
#  Papan skor (leaderboard)
# ------------------------------------------------------------------------- #
screen leaderboard():
    modal True
    zorder 200

    add "#000000cc"

    frame:
        align (0.5, 0.5)
        xpadding 40
        ypadding 30
        xmaximum 900
        background "#1b1b1bf2"

        vbox:
            spacing 12

            text "PAPAN SKOR OSPEK" size 40 color "#f1c40f" xalign 0.5

            $ _rows = ospek_tracker.leaderboard()
            $ _rank, _total = ospek_tracker.player_rank()

            for _i, (_name, _score, _is_player) in enumerate(_rows):
                hbox:
                    spacing 14
                    text "[_i + 1]." size 26 color ("#f1c40f" if _is_player else "#ffffff") xsize 60
                    text _name size 26 color ("#f1c40f" if _is_player else "#ffffff")
                    text "[_score]" size 26 color ("#f1c40f" if _is_player else "#bbbbbb") xalign 1.0

            null height 6
            text "Peringkatmu: [_rank] dari [_total]" size 26 color "#2ecc71" xalign 0.5

            null height 4
            text "Nilai per kategori:" size 24 color "#ffffff"
            $ _cats = ospek_tracker.category_scores()
            for _cname, _cval in _cats.items():
                hbox:
                    spacing 10
                    text _cname size 22 color "#dddddd" xsize 260
                    text "[_cval]/100" size 22 color "#dddddd"

            null height 6
            textbutton "Tutup" action Hide("leaderboard") xalign 0.5


# ------------------------------------------------------------------------- #
#  Evaluasi akhir
# ------------------------------------------------------------------------- #
label final_evaluation:
    scene bg ospek_hall with dissolve
    stop music fadeout 2.0
    play music end_theme fadein 2.0 loop
    show pak_budi at center

    $ _grade = ospek_tracker.calculate_final_grade()
    p "Ospek telah usai. Nilai akhir kamu: [_grade]."

    "Berikut ringkasan perjalananmu selama 7 hari:"
    $ _poin = ospek_tracker.ospek_points
    $ _kuis = "{}/{}".format(ospek_tracker.quiz_score, ospek_tracker.quiz_total)
    $ _rel = ospek_tracker.total_relationship_score()
    "Poin ospek: [_poin]  |  Skor kuis AIK: [_kuis]  |  Total kedekatan: [_rel]"

    "Catatan kegiatan harianmu:"
    python:
        for _d, _txt in ospek_tracker.schedule_summary():
            renpy.say(None, "Hari {}: {}".format(_d, _txt))

    python:
        _best = ospek_tracker.closest_friend()
        if _best:
            _best_name, _best_score = _best
        else:
            _best_name, _best_score = None, 0
    if _best_name:
        "Teman yang paling dekat denganmu adalah [_best_name] (kedekatan [_best_score]/10)."
    else:
        "Kamu belum sempat dekat dengan siapa pun selama ospek ini."

    "Hubungan Pertemanan:"
    python:
        for _name, _val in ospek_tracker.friend_relationship.items():
            _status = ospek_tracker.get_relationship_status(_val["score"])
            renpy.say(None, "{}: {} (Skor: {})".format(_name, _status, _val["score"]))

    python:
        _ach_count = len(ospek_tracker.achievement_list())
        _ach_max = ospek_tracker.achievement_max()
    "Pencapaian yang kamu raih: [_ach_count] dari [_ach_max]."
    if _ach_count:
        $ renpy.say(None, "Tekan tombol Pencapaian ★ pada HUD untuk melihat detailnya.")

    # ---------------- Konflik ---------------- #
    python:
        _c_total = ospek_tracker.conflicts_total()
        _c_ok = ospek_tracker.conflicts_resolved()
    "Konflik antar-teman: [_c_ok] dari [_c_total] terselesaikan dengan damai."
    python:
        for _c in ospek_tracker.conflict_log:
            _mark = "✔" if _c["resolved"] else "✘"
            renpy.say(None, "{} {} — pilihanmu: {}".format(_mark, _c["title"], _c["choice"]))

    # ---------------- Mini-game ---------------- #
    python:
        _mg = ospek_tracker.minigame_scores
        _mg_txt = "Yel-yel {}/{}, Teka-teki {}/{}, Ayat {}/{}".format(
            _mg["yel_yel"], ospek_tracker.minigame_max["yel_yel"],
            _mg["teka_teki"], ospek_tracker.minigame_max["teka_teki"],
            _mg["ayat"], ospek_tracker.minigame_max["ayat"])
    "Skor mini-game: [_mg_txt]"

    # ---------------- Nilai & ranking ---------------- #
    python:
        _overall = ospek_tracker.overall_score()
        _rank, _total_p = ospek_tracker.player_rank()
        if _rank == 1:
            ospek_tracker.add_achievement("peringkat_1")
        if _rank <= 3:
            ospek_tracker.add_achievement("peringkat_3")
        if _c_total and _c_ok == _c_total:
            ospek_tracker.add_achievement("pendamai")

    "Nilai akhir ospek kamu: [_overall]/100"
    "Peringkat kamu: [_rank] dari [_total_p] peserta."
    $ renpy.say(None, "Tekan tombol Papan Skor 🏆 pada HUD untuk melihat rincian nilai per kategori.")

    python:
        _end_title, _end_desc = ospek_tracker.get_ending()

    show nata at center
    e "Terima kasih, semuanya. Aku belajar banyak di ospek ini dan akan terus berusaha menjadi lebih baik."

    p "Semoga perjalananmu di Unimus semakin membawa kebaikan. Teruskan perjuanganmu!"

    scene bg welcome_night with dissolve
    e "Ospek sudah selesai, tapi perjalanan aku di Unimus baru dimulai. Aku siap menghadapi tantangan yang lebih besar!"

    stop music fadeout 2.0

    "[_end_title]"
    "[_end_desc]"

    return


# ------------------------------------------------------------------------- #
#  Mode jelajah bebas (navigasi lokasi & karakter)
# ------------------------------------------------------------------------- #
init python:
    LOCATIONS = {
        "kampus_depan": {
            "name": "Depan Kampus",
            "background": "bg kampus_depan",
            "available_characters": ["nata", "andi", "momogi", "pak_budi"],
            "music": "audio/ospek_welcome.mp3",
        },
        "aula_ospek": {
            "name": "Aula Ospek",
            "background": "bg aula_ospek",
            "available_characters": ["pak_budi", "joko", "rina"],
            "music": "audio/ospek_welcome.mp3",
        },
        "ruang_kuliah": {
            "name": "Ruang Kuliah",
            "background": "bg ruang_kuliah",
            "available_characters": ["pak_budi", "andi", "rina"],
            "music": "audio/quiz_theme.mp3",
        },
        "pusat_mahasiswa": {
            "name": "Pusat Mahasiswa",
            "background": "bg pusat_mahasiswa",
            "available_characters": ["momogi", "joko", "andi"],
            "music": "audio/challenge_theme.mp3",
        },
        "kantin": {
            "name": "Kantin Kampus",
            "background": "bg kantin",
            "available_characters": ["dimas", "rina", "momogi"],
            "music": "audio/ospek_welcome.mp3",
        },
        "perpustakaan": {
            "name": "Perpustakaan",
            "background": "bg perpustakaan",
            "available_characters": ["momogi", "bu_ratna", "andi"],
            "music": "audio/quiz_theme.mp3",
        },
        "masjid": {
            "name": "Masjid Kampus",
            "background": "bg masjid",
            "available_characters": ["joko", "pak_budi", "rina"],
            "music": "audio/ospek_welcome.mp3",
        },
    }

    def pindah_lokasi(lokasi):
        """Pindah lokasi: ganti background dan musik."""
        if lokasi not in LOCATIONS:
            raise ValueError("Lokasi {} tidak ditemukan".format(lokasi))
        loc = LOCATIONS[lokasi]
        renpy.scene()
        renpy.show(loc["background"])
        renpy.music.play(loc["music"], fadeout=1.0, fadein=1.0)

    def pilih_karakter_di_lokasi(lokasi):
        """Daftar id karakter yang tersedia di lokasi tertentu."""
        if lokasi not in LOCATIONS:
            raise ValueError("Lokasi {} tidak ditemukan".format(lokasi))
        return LOCATIONS[lokasi]["available_characters"]


label navigasi_bebas:
    scene bg welcome with dissolve
    menu:
        "Pilih Lokasi":
            call pilih_lokasi
            jump navigasi_bebas

        "Pilih Karakter untuk Berbicara":
            call pilih_karakter
            jump navigasi_bebas

        "Kembali ke Cerita":
            return


label pilih_lokasi:
    python:
        _locs = [(v["name"], k) for k, v in LOCATIONS.items()]
        _locs.append(("Kembali", None))
        _pilih = renpy.display_menu(_locs)
    if _pilih is not None:
        $ pindah_lokasi(_pilih)
        $ renpy.say(None, "Kamu berpindah ke {}.".format(LOCATIONS[_pilih]["name"]))
    return


label pilih_karakter:
    python:
        _all = []
        _seen = set()
        for _lk, _lv in LOCATIONS.items():
            for _cid in _lv["available_characters"]:
                if _cid == "nata" or _cid in _seen:
                    continue
                _seen.add(_cid)
                _all.append(("{}  —  {}".format(CHARACTER_INFO[_cid]["name"], _lv["name"]), _cid))
        _all.append(("Kembali", None))
        _cid = renpy.display_menu(_all)
    if _cid is not None:
        $ show_character(_cid, "center")
        $ interact(_cid)
        python:
            for _k in ("andi", "momogi", "rina", "joko", "pak_budi", "sari", "dimas", "bu_ratna"):
                renpy.hide(CHARACTER_INFO[_k]["image"])
    return
