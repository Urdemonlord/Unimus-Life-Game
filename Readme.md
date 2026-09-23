# Unimus Life Game 🎮

Visual novel interaktif bertema **ospek (orientasi studi dan pengenalan kampus)**
di **Universitas Muhammadiyah Semarang (Unimus)**, dibangun dengan
[Ren'Py](https://www.renpy.org/).

Kamu berperan sebagai **Nata**, mahasiswa baru yang menjalani 7 hari ospek:
memilih jurusan, mengatur stamina, membangun pertemanan, mengikuti kuis
Al-Islam & Kemuhammadiyahan, dan menghadapi tantangan kerja tim. Setiap
keputusan menentukan nilai akhir dan ending yang kamu dapatkan.

## Fitur ✨

- **Sistem 7 hari + stamina** — setiap hari hanya bisa melakukan satu kegiatan
  utama; stamina habis memaksamu beristirahat.
- **5 kegiatan harian** — seminar, lomba akademik, diskusi keagamaan, olahraga,
  membantu teman, dan istirahat.
- **Event acak harian** — 10 kejadian tak terduga (sarapan bareng, kajian
  singkat, nasihat dosen, dll.) yang memberi efek berbeda tiap kali bermain.
- **Jalur cerita per jurusan** — event eksklusif di hari ke-4 untuk Teknik
  Informatika (lab komputer), Manajemen (rapat/seminar), dan Kesehatan
  (lab pertolongan pertama), plus dialog bernuansa jurusan.
- **Kuis AIK multi-soal** — 5 soal Al-Islam & Kemuhammadiyahan dengan
  pembahasan tiap jawaban.
- **Sistem hubungan** — skor kedekatan dengan **8 karakter** (Andi, Momogi,
  Rina, Joko, Pak Budi, Sari, Dimas, Bu Ratna) beserta status hubungan
  (Baru Kenal → Sahabat Sejati).
- **Statistik pemain** — leadership, discipline, religious_knowledge,
  academic_potential, stamina.
- **Sistem konflik antar-teman** — 4 konflik (pembagian tugas, salah paham,
  candaan berlebihan, kecemburuan prestasi) di hari 6 & 7. Tiap konflik punya
  3 cara penyelesaian dengan dampak berbeda pada kedekatan, statistik, dan
  poin. Konflik yang gagal diselesaikan menutup ending terbaik.
- **3 mini-game** — **susun yel-yel** (acak kata jadi yel-yel), **teka-teki
  logika Islami** (jawaban angka), dan **tebak lanjutan ayat/hadis** (pilihan
  ganda). Semua memberi poin ospek dan menaikkan statistik.
- **Sistem nilai & ranking** — rapor ospek dengan 5 kategori (Poin Ospek,
  Kedekatan, Kuis AIK, Mini-game, Konflik) dan skor akhir 0–100. Kamu
  dibandingkan dengan 6 peserta lain di **papan skor** (tombol **Papan Skor 🏆**
  di HUD). Bertanding ketat — juara umum tidak mudah diraih.
- **6 ending berbeda** — ditentukan oleh poin ospek, total kedekatan, stat, dan
  seberapa baik konflik diselesaikan. Setiap gaya bermain (akademik, sosial,
  pasif, seimbang) menghasilkan ending yang berbeda.
- **Pencapaian (achievements)** — 20 pencapaian, mis. "Ahli AIK" (kuis
  sempurna), "Jiwa Pemimpin" (leadership 90), "Calon Programmer" (jalur
  Informatika), "Juara Mini-game", "Pendamai", "Juara Umum Ospek", dan
  "Sahabat <nama>" (kedekatan 8). Bisa dibuka lewat tombol
  **Pencapaian ★** di HUD.
- **Catatan harian** — lihat rekap kegiatan tiap hari, baik saat bermain
  maupun di ringkasan akhir.
- **Sahabat terdekat** — di akhir ospek ditampilkan teman yang paling
  dekat denganmu.
- **HUD** — menampilkan hari, stamina, dan poin ospek selama permainan.
- **Mode jelajah bebas** — 7 lokasi kampus (depan kampus, aula, ruang kuliah,
  pusat mahasiswa, kantin, perpustakaan, masjid) dan mengobrol dengan karakter.
- **Antarmuka lintas platform** — desktop dan mobile (tata letak khusus ponsel).

## Persyaratan Sistem 💻

- **Ren'Py 8.0 atau lebih baru** (dikembangkan & diuji dengan Ren'Py 8.3)
- Windows, macOS, atau Linux
- Opsional: dukungan perangkat mobile

## Cara Menjalankan 🚀

### 1. Clone repositori

```bash
git clone https://github.com/Urdemonlord/Unimus-Life-Game.git
cd Unimus-Life-Game
```

### 2. Buka dengan Ren'Py Launcher

1. Unduh & pasang [Ren'Py SDK](https://www.renpy.org/latest.html) (8.0+).
2. Buka **Ren'Py Launcher**.
3. Klik **Preferences → Projects Directory**, arahkan ke folder induk
   `Unimus-Life-Game`.
4. Pilih proyek **Unimus-Life-Game** di daftar, lalu klik **Launch Project**.

## Struktur Proyek 📁

```
Unimus-Life-Game/
├── game/
│   ├── script.rpy      # alur cerita, sistem ospek, kuis, ending
│   ├── options.rpy     # konfigurasi dasar game
│   ├── screens.rpy     # layar antarmuka Ren'Py
│   ├── gui.rpy         # pengaturan tema GUI
│   ├── audio/          # musik tema
│   ├── images/         # background & sprite karakter
│   └── gui/            # aset antarmuka
├── LICENSE
└── Readme.md
```

## Cara Bermain 🕹️

- Setiap hari kamu memilih **satu kegiatan** dari menu (atau menjelajah kampus).
- Kegiatan menguras **stamina**; jika stamina < 20 kamu hanya bisa istirahat.
- **Event acak** bisa terjadi setiap pagi, kecuali hari 3, 5, 6 & 7.
- **Hari 3** kuis AIK · **Hari 4** event jalur jurusan · **Hari 5** tantangan tim.
- **Hari 6** konflik antar-teman + sesi mini-game (yel-yel, teka-teki, ayat).
- **Hari 7** konflik terakhir, lalu evaluasi akhir.
- Setelah **7 hari**, nilai akhir dan ending dihitung dari poin ospek, total
  kedekatan, statistik, dan hasil penyelesaian konflik.
- Buka **Pencapaian ★** dan **Papan Skor 🏆** kapan saja lewat tombol di HUD.

## Mengganti Aset Gambar 🎨

Semua background & sprite karakter baru saat ini adalah **placeholder buatan
otomatis** (gradasi warna + label). Silakan ganti dengan gambar/foto asli —
cukup timpa berkas dengan nama yang sama:

| Berkas | Ukuran disarankan | Keterangan |
|---|---|---|
| `game/images/kantin.jpg` | 1920×1080 | Kantin kampus |
| `game/images/perpustakaan.jpg` | 1920×1080 | Perpustakaan |
| `game/images/masjid.jpg` | 1920×1080 | Masjid kampus |
| `game/images/lab_komputer.jpg` | 1920×1080 | Lab komputer (jalur Informatika) |
| `game/images/ruang_seminar.jpg` | 1920×1080 | Ruang seminar (jalur Manajemen) |
| `game/images/lab_kesehatan.jpg` | 1920×1080 | Lab kesehatan (jalur Kesehatan) |
| `game/images/characters/sari.png` | 1024×1024 (PNG transparan) | Sari (kakak senior) |
| `game/images/characters/dimas.png` | 1024×1024 (PNG transparan) | Dimas (teman sekamar) |
| `game/images/characters/bu_ratna.png` | 1024×1024 (PNG transparan) | Bu Ratna (dosen) |

> Background: JPG 1920×1080. Karakter: PNG transparan 1024×1024, berdiri
> dengan posisi di bagian bawah gambar.

## Berkontribusi 🛠️

1. Fork repositori ini.
2. Buat branch fitur: `git checkout -b fitur/nama-fitur`.
3. Commit perubahan: `git commit -m "Tambah fitur ..."`.
4. Push branch dan buka **Pull Request**.

## Lisensi 📄

Proyek ini dilisensikan di bawah **MIT License** — lihat berkas
[LICENSE](LICENSE) untuk detail.

Copyright (c) 2024 Urdemonlord

## Kontak 📧

- GitHub: [Urdemonlord](https://github.com/Urdemonlord)
- Repositori: [Unimus-Life-Game](https://github.com/Urdemonlord/Unimus-Life-Game)
