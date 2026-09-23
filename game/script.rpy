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
    }

    CHARACTER_DIALOGUES = {
        "andi": [
            "Semangat, Nata! Ospek itu tempat kita tumbuh bersama.",
            "Kalau ada tugas kelompok, aku siap bantu kapan saja.",
            "Jangan lupa istirahat, kesehatan juga bagian dari ibadah.",
        ],
        "momogi": [
            "Aku jauh dari rumah, tapi di sini aku belajar mandiri.",
            "Kita perantau harus saling menguatkan, ya!",
            "Cita-citaku besar, dan ospek ini langkah pertamanya.",
        ],
        "rina": [
            "Menjaga kesehatan tubuh dan jiwa itu seimbang, Nata.",
            "Aku ikut kegiatan kemanusiaan, mau ikut suatu hari?",
            "Senyum itu sedekah, jadi jangan pelit senyum!",
        ],
        "joko": [
            "Disiplin adalah kunci. Tanpa itu, ilmu sulit bermanfaat.",
            "Aku tegas bukan karena benci, tapi karena sayang.",
            "Nilai keagamaan harus jadi fondasi, bukan hiasan.",
        ],
        "pak_budi": [
            "Kepemimpinan adalah amanah, bukan sekadar jabatan.",
            "Teruslah belajar, karena ilmu itu cahaya.",
            "Jaga akhlak, maka ilmumu akan berkah.",
        ],
    }

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

        def add_conflict(self, conflict_description):
            if conflict_description not in self.conflicts:
                self.conflicts.append(conflict_description)

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
            """Tentukan ending berdasarkan poin, hubungan, dan stat.

            Ambang dikalibrasi agar tiap cabang bisa dicapai dalam 7 hari:
            - jalur "poin"  : fokus kompetisi/seminar  -> poin tinggi, rel rendah
            - jalur "sosial": fokus diskusi/bantu teman -> rel tinggi
            """
            pts = self.ospek_points
            rel_total = self.total_relationship_score()

            if pts >= 18 and rel_total >= 14:
                return (
                    "ENDING: SAHABAT SEPANJANG MASA",
                    "Kamu menjadi mahasiswa teladan sekaligus sahabat sejati bagi teman-teman ospekmu.",
                )
            if pts >= 18:
                return (
                    "ENDING: MAHASISWA INSPIRATIF",
                    "Prestasimu menonjol, meski kamu masih perlu lebih dekat dengan teman-teman.",
                )
            if rel_total >= 14:
                return (
                    "ENDING: SAHABAT SEJATI",
                    "Kamu mungkin bukan yang paling menonjol, tetapi persahabatanmu sangat kuat.",
                )
            if pts >= 12:
                return (
                    "ENDING: MAHASISWA BERPRESTASI",
                    "Kamu aktif dan berprestasi selama ospek. Terus pertahankan!",
                )
            if pts >= 6:
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

# ------------------------------------------------------------------------- #
#  Gambar karakter
# ------------------------------------------------------------------------- #
image nata = "images/characters/nata.png"
image andi = "images/characters/andi.png"
image momogi = "images/characters/momogi.png"
image pak_budi = "images/characters/pak_budi.png"
image rina = "images/characters/rina.png"
image joko = "images/characters/joko.png"

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

    "[ Hari [day] dari [ospek_tracker.total_ospek_days] ]"

    if ospek_tracker.stamina < ospek_tracker.LOW_STAMINA:
        show pak_budi at center
        p "Kamu terlihat lelah, Nata. Sebaiknya istirahat dulu hari ini agar tidak tumbang."
        hide pak_budi

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
        scene bg lecture_room with dissolve
        "[_text]"
        hide screen hud
        $ renpy.say(None, "Poin ospek: +[_act[points]]")
        show screen hud
    else:
        "Tenagamu tidak cukup untuk kegiatan itu. Kamu memilih beristirahat."

    # ---------------- Event khusus per hari ---------------- #
    if day == 3:
        call kuis_aik
    elif day == 5:
        call tantangan_tim

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
    "Pencapaian yang kamu raih: [_ach_count] dari 10."
    if _ach_count:
        $ renpy.say(None, "Tekan tombol Pencapaian ★ pada HUD untuk melihat detailnya.")

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
        for _lk, _lv in LOCATIONS.items():
            for _cid in _lv["available_characters"]:
                if _cid == "nata":
                    continue
                _all.append(("{}  —  {}".format(CHARACTER_INFO[_cid]["name"], _lv["name"]), _cid))
        _all.append(("Kembali", None))
        _cid = renpy.display_menu(_all)
    if _cid is not None:
        $ show_character(_cid, "center")
        $ interact(_cid)
        hide andi
        hide momogi
        hide rina
        hide joko
        hide pak_budi
    return
