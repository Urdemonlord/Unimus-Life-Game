# Import Libraries
init python:
    import random

    class OspekProgressTracker:
        def __init__(self):
            self.ospek_points = 0
            self.friend_relationship = {
                "Andi": 0,
                "Momogi": 0,
                "Rina": 0,
                "Joko": 0,
                "Pak Budi": 0,
            }
            self.current_major = None
            self.quiz_score = 0

        def update_relationship(self, character, points):
            """Update relationship with a character"""
            if character in self.friend_relationship:
                self.friend_relationship[character] = min(
                    max(self.friend_relationship[character] + points, 0), 10
                )

        def add_ospek_points(self, points):
            """Add points to ospek progress"""
            self.ospek_points += points

        def set_major(self, major):
            """Set the player's chosen major"""
            self.current_major = major

    def get_relationship_status(score):
        """Convert score to status"""
        if score >= 8:
            return "Sangat Dekat"
        elif score >= 5:
            return "Dekat"
        elif score >= 3:
            return "Cukup Kenal"
        else:
            return "Tidak Kenal"

# Initialize global tracker
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

    p "Selamat datang, mahasiswa baru! Ospek kali ini akan berbeda dari tahun-tahun sebelumnya."

    # Character Introductions
    scene bg ospek_hall with dissolve
    show andi at left
    show momogi at right

    a "Hai, aku Andi dari Teknik Informatika."
    l "Aku Momogi dari Manajemen. Kamu mau masuk jurusan apa?"

    menu:
        "Teknik Informatika":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.set_major("Teknik Informatika")
            $ ospek_tracker.update_relationship("Andi", 2)
            show nata at center
            e "Teknik Informatika adalah pilihanku!"
            a "Keren! Kita bisa saling membantu nanti."

        "Manajemen":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.set_major("Manajemen")
            $ ospek_tracker.update_relationship("Momogi", 2)
            show nata at center
            e "Aku memilih Manajemen."
            l "Bagus! Kita akan banyak belajar bersama."

        "Kesehatan":
            $ ospek_tracker.add_ospek_points(1)
            $ ospek_tracker.set_major("Kesehatan")
            show nata at center
            show rina at left
            r "Selamat datang di prodi Kesehatan!"
            $ ospek_tracker.update_relationship("Rina", 1)

    # Team Building Challenge
    scene bg student_center with dissolve
    play music challenge_theme fadein 2.0 loop
    show pak_budi at center
    show joko at right

    p "Sekarang, kalian akan menghadapi tantangan kerja tim yang menguji kemampuan kolaborasi dan kepemimpinan."
    j "Siap menghadapi apapun, Pak!"

    menu:
        "Ambil inisiatif memimpin tim":
            $ ospek_tracker.add_ospek_points(3)
            $ ospek_tracker.update_relationship("Joko", 1)
            $ ospek_tracker.update_relationship("Pak Budi", 2)
            show nata at left
            e "Saya akan mengkoordinasi tim kita secara efektif."
            p "Kepemimpinan yang baik, Nata! Kerjasama tim adalah kunci sukses di perguruan tinggi."

        "Fokus pada peran supportif":
            $ ospek_tracker.add_ospek_points(2)
            $ ospek_tracker.update_relationship("Andi", 1)
            $ ospek_tracker.update_relationship("Momogi", 1)
            show nata at left
            e "Mari kita kerjakan tugas ini bersama-sama, saling mendukung."
            j "Kerja tim yang solid! Setiap kontribusi penting."

    # Quiz Section with New Music
    scene bg lecture_room with dissolve
    play music quiz_theme fadein 2.0 loop
    show pak_budi at center

    p "Sekarang, tes pengetahuan dasar tentang Unimus! Ini bukan sekadar ujian, tetapi kesempatan untuk mengenal almamater kalian lebih dalam."

    $ answer = renpy.input("Tahun berapa Unimus didirikan?").strip()
    if answer == "1999":
        $ ospek_tracker.quiz_score += 1
        $ ospek_tracker.add_ospek_points(1)
        show nata at right
        e "Tahun 1999, kan? Saya sudah membaca sejarahnya!"
        p "Tepat sekali! Unimus sudah berkontribusi dalam pendidikan selama puluhan tahun."
    else:
        show nata at right
        e "Hmm... sepertinya saya masih perlu belajar lebih banyak."

    # End Scene with Outro Music
    scene bg ospek_hall with dissolve
    stop music fadeout 2.0
    play music end_theme fadein 2.0 loop

    show pak_budi at center

    if ospek_tracker.ospek_points >= 8:
        p "Luar biasa! Anda menunjukkan potensi yang sangat baik. Semangat dan keingintahuan adalah modal utama seorang mahasiswa."
    elif ospek_tracker.ospek_points >= 5:
        p "Cukup baik. Terus kembangkan potensi dan rasa ingin tahu Anda."
    else:
        p "Anda masih perlu banyak belajar dan beradaptasi. Jangan menyerah."

    # Relationship Summary
    "Hubungan Pertemanan:"
    python:
        for character, value in ospek_tracker.friend_relationship.items():
            if value > 0:
                status = get_relationship_status(value)
                renpy.say(None, f"{character}: {status} (Skor: {value})")

    stop music fadeout 2.0
    "Ospek Unimus: Babak Pertama Selesai."

    return
