init python:
    import random

    class OspekProgressTracker:
        def __init__(self):
            self.ospek_points = 0
            self.friend_relationship = {
                "Andi": {"score": 0, "background": "Aktivis mahasiswa dengan semangat tinggi"},
                "Momogi": {"score": 0, "background": "Mahasiswa perantau dengan cita-cita besar"},
                "Rina": {"score": 0, "background": "Aktivis kesehatan dan kemanusiaan"},
                "Joko": {"score": 0, "background": "Senior tegas dengan nilai keagamaan kuat"},
                "Pak Budi": {"score": 0, "background": "Pembimbing spiritual dengan pengalaman luas"}
            }
            
            self.stats = {
                "stamina": 100,
                "leadership": 0,
                "discipline": 0,
                "religious_knowledge": 0,
                "academic_potential": 0
            }
            
            self.current_major = None
            self.quiz_score = 0
            self.achievements = []
            self.daily_schedule = []
            self.conflicts = []
            
            self.current_day = 1
            self.total_ospek_days = 7

        def _validate_input(self, character=None, stat_name=None):
            """Validate input parameters for various methods."""
            if character and character not in self.friend_relationship:
                raise ValueError(f"Unknown character: {character}")
            if stat_name and stat_name not in self.stats:
                raise ValueError(f"Unknown stat: {stat_name}")

        def update_relationship(self, character, points):
            """Update relationship score with validation and milestone checking."""
            self._validate_input(character)
            current_score = self.friend_relationship[character]["score"]
            new_score = max(0, min(current_score + points, 10))
            
            self.friend_relationship[character]["score"] = new_score
            self._check_relationship_milestone(character, new_score)

        def _check_relationship_milestone(self, character, score):
            """Check and add relationship milestones."""
            if score >= 8:
                milestone = f"{character}_close_friend"
                if milestone not in self.achievements:
                    self.achievements.append(milestone)

        def add_ospek_points(self, points):
            """Add points to overall ospek score."""
            self.ospek_points += points

        def set_major(self, major):
            """Set the student's chosen major."""
            self.current_major = major

        def update_stat(self, stat_name, points):
            """Update a specific stat with validation and achievement checking."""
            self._validate_input(stat_name=stat_name)
            current_value = self.stats[stat_name]
            new_value = max(0, min(current_value + points, 100))
            
            self.stats[stat_name] = new_value
            self._check_stat_achievement(stat_name)

        def _check_stat_achievement(self, stat_name):
            """Check and add stat-based achievements."""
            if self.stats[stat_name] >= 90:
                achievement = f"master_{stat_name}"
                if achievement not in self.achievements:
                    self.achievements.append(achievement)

        def add_conflict(self, conflict_description):
            """Add a unique conflict to the tracker."""
            if conflict_description not in self.conflicts:
                self.conflicts.append(conflict_description)

        def choose_daily_activity(self, activity):
            """Choose a daily activity with predefined effects."""
            activities = {
                "seminar": {"ospek_points": 2, "stamina": -20, "leadership": 5, "religious_knowledge": 10},
                "kompetisi": {"ospek_points": 3, "stamina": -30, "academic_potential": 10, "discipline": 5},
                "diskusi_keagamaan": {"ospek_points": 2, "religious_knowledge": 15, "leadership": 3},
                "istirahat": {"stamina": 30, "ospek_points": 0}
            }
            
            if activity not in activities:
                raise ValueError(f"Unknown activity: {activity}")

            activity_effects = activities[activity]
            
            for stat, value in activity_effects.items():
                if stat == "ospek_points":
                    self.add_ospek_points(value)
                else:
                    self.update_stat(stat, value)
            
            self.daily_schedule.append(activity)
            self.current_day += 1

        def generate_unique_challenge(self):
            """Generate a random challenge."""
            challenges = [
                "Susun Yel-Yel Kreatif",
                "Diskusikan Peran Muhammadiyah dalam Pendidikan",
                "Rancang Proyek Sosial Kampus",
                "Pecahkan Teka-Teki Logika Islami"
            ]
            return random.choice(challenges)

        def calculate_final_grade(self):
            """Calculate final grade based on multiple factors."""
            total_score = (
                self.ospek_points * 0.3 +
                sum(rel['score'] for rel in self.friend_relationship.values()) * 5 +
                sum(self.stats.values()) * 0.5
            )
            
            grade_mapping = [
                (90, "Mahasiswa Inspiratif"),
                (75, "Mahasiswa Berprestasi"),
                (60, "Mahasiswa Potensial")
            ]
            
            for threshold, grade in grade_mapping:
                if total_score >= threshold:
                    return grade
            
            return "Perlu Pengembangan Diri"

        @staticmethod
        def get_relationship_status(score):
            """Determine relationship status based on score."""
            status_mapping = [
                (8, "Sahabat Sejati"),
                (5, "Teman Dekat"),
                (3, "Kenalan Baik"),
                (0, "Baru Kenal")
            ]
            
            for threshold, status in status_mapping:
                if score >= threshold:
                    return status
            return "Baru Kenal"

# Global Tracker
default ospek_tracker = OspekProgressTracker()

# Character Definitions
define e = Character("Nata", who_color="#3498db")
define a = Character("Andi", who_color="#2ecc71")
define l = Character("Momogi", who_color="#e74c3c")
define p = Character("Pak Budi", who_color="#f39c12")
define r = Character("Rina", who_color="#9b59b6")
define j = Character("Joko", who_color="#1abc9c")

# Character Images
image nata = "images/characters/nata.png"
image andi = "images/characters/andi.png"
image momogi = "images/characters/momogi.png"
image pak_budi = "images/characters/pak_budi.png"
image rina = "images/characters/rina.png"
image joko = "images/characters/joko.png"

# Backgrounds and Audio
image bg welcome = "images/campus_entrance.jpg"
image bg ospek_hall = "images/ospek_main_hall.jpg"
image bg lecture_room = "images/lecture_room.jpg"
image bg student_center = "images/student_center.jpg"
define audio.ospek_theme = "audio/ospek_welcome.mp3"
define audio.challenge_theme = "audio/challenge_theme.mp3"
define audio.quiz_theme = "audio/quiz_theme.mp3"
define audio.end_theme = "audio/end_theme.mp3"

# Main Game Start
label start:
    # Opening Scene with Main Theme
    scene bg welcome with dissolve
    play music ospek_theme fadein 2.0 loop

    "Pagi yang cerah di Universitas Muhammadiyah Semarang (Unimus)."

    show nata at center
    e "Deg-degaran rasanya. Pertama kali masuk kampus setelah sekian lama mempersiapkan diri."

    # Introduction to Ospek
    scene bg ospek_hall with fade
    show pak_budi at center

    p "Selamat datang, mahasiswa baru! Di Unimus, kita tidak hanya belajar ilmu akademik tetapi juga nilai-nilai Islam yang menjadi pedoman hidup."

    # Dialog Refleksi Al-Islam dan Kemuhammadiyahan
    show andi at left
    show momogi at right

    a "Salah satu yang menarik di Unimus adalah program *Al-Islam dan Kemuhammadiyahan*. Kita belajar bagaimana menjadi individu yang bermanfaat bagi masyarakat."
    l "Betul, Andi. Kita juga diajarkan pentingnya *fastabiqul khairat* atau berlomba-lomba dalam kebaikan."

    # Pemilihan Jurusan
    menu:
        "Teknik Informatika":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.set_major("Teknik Informatika")
            $ ospek_tracker.update_relationship("Andi", 2)
            show nata at center
            e "Teknik Informatika adalah pilihanku!"
            a "Keren! Semoga kita bisa berkontribusi lewat teknologi yang mendukung nilai-nilai Islam."

        "Manajemen":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.set_major("Manajemen")
            $ ospek_tracker.update_relationship("Momogi", 2)
            show nata at center
            e "Aku memilih Manajemen."
            l "Bagus! Kita akan belajar bagaimana menjadi pemimpin yang amanah."

        "Kesehatan":
            $ ospek_tracker.add_ospek_points(1)
            $ ospek_tracker.set_major("Kesehatan")
            show nata at center
            show rina at left
            r "Selamat datang di prodi Kesehatan! Islam juga mengajarkan pentingnya menjaga kesehatan tubuh dan jiwa."
            $ ospek_tracker.update_relationship("Rina", 1)

    # Tantangan Kerja Tim
    scene bg student_center with dissolve
    play music challenge_theme fadein 2.0 loop
    show pak_budi at center
    show joko at right

    p "Sekarang, tantangan kerja tim! Tantangan ini akan menguji nilai *ta'awun* atau saling tolong menolong."

    menu:
        "Ambil inisiatif memimpin tim":
            $ ospek_tracker.add_ospek_points(3)
            $ ospek_tracker.update_relationship("Joko", 1)
            $ ospek_tracker.update_relationship("Pak Budi", 2)
            show nata at left
            e "Saya akan mengatur strategi agar tugas ini bisa selesai dengan baik."
            p "Kepemimpinan itu adalah amanah, Nata. Bagus sekali, terus tingkatkan!"

        "Fokus pada peran supportif":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.update_relationship("Andi", 1)
            $ ospek_tracker.update_relationship("Momogi", 1)
            show nata at left
            e "Saya akan membantu teman-teman menyelesaikan tugas ini."
            j "Kerja tim yang solid! Setiap kontribusi itu bernilai."

    # Kuis Pengetahuan AIK
    scene bg lecture_room with dissolve
    play music quiz_theme fadein 2.0 loop
    show pak_budi at center

    p "Sekarang, kita lanjutkan dengan kuis tentang nilai-nilai *Al-Islam dan Kemuhammadiyahan*."

    $ answer = renpy.input("Apa arti dari 'fastabiqul khairat'?").strip()
    if answer.lower() in ["berlomba dalam kebaikan", "berlomba-lomba dalam kebaikan"]:
        $ ospek_tracker.quiz_score += 1
        $ ospek_tracker.add_ospek_points(1)
        show nata at right
        e "Itu berarti berlomba-lomba dalam kebaikan, Pak."
        p "Bagus sekali! Semoga nilai ini menjadi pegangan dalam kehidupan kalian."
    else:
        show nata at right
        e "Hmm... Saya belum paham benar."
        p "Tidak apa-apa, ini saatnya untuk belajar lebih dalam."

    # Penutupan
    scene bg ospek_hall with dissolve
    stop music fadeout 2.0
    play music end_theme fadein 2.0 loop

    show pak_budi at center

    if ospek_tracker.ospek_points >= 8:
        p "Luar biasa! Anda menunjukkan potensi luar biasa. Nilai-nilai Islam terlihat dalam tindakan Anda."
    elif ospek_tracker.ospek_points >= 5:
        p "Cukup baik. Tetaplah semangat dalam belajar dan berbuat kebaikan."
    else:
        p "Anda masih perlu belajar lebih banyak. Jangan berhenti berusaha."

    # Ringkasan Hubungan
    "Hubungan Pertemanan:"
    python:
        for character, value in ospek_tracker.friend_relationship.items():
            score = value["score"]
            status = ospek_tracker.get_relationship_status(score)
            renpy.say(None, f"{character}: {status} (Skor: {score})")

    stop music fadeout 2.0
    "Ospek Unimus: Babak Pertama Selesai."

    return