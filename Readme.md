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
- **Kuis AIK multi-soal** — 5 soal Al-Islam & Kemuhammadiyahan dengan
  pembahasan tiap jawaban.
- **Sistem hubungan** — skor kedekatan dengan 5 karakter (Andi, Momogi, Rina,
  Joko, Pak Budi) beserta status hubungan (Baru Kenal → Sahabat Sejati).
- **Statistik pemain** — leadership, discipline, religious_knowledge,
  academic_potential, stamina.
- **Banyak ending** — ditentukan oleh poin ospek, total kedekatan, dan stat.
- **Pencapaian (achievements)** — 10 pencapaian, mis. "Ahli AIK" (kuis
  sempurna), "Jiwa Pemimpin" (leadership 90), dan "Sahabat <nama>"
  (kedekatan 8). Bisa dibuka lewat tombol **Pencapaian ★** di HUD.
- **Catatan harian** — lihat rekap kegiatan tiap hari, baik saat bermain
  maupun di ringkasan akhir.
- **Sahabat terdekat** — di akhir ospek ditampilkan teman yang paling
  dekat denganmu.
- **HUD** — menampilkan hari, stamina, dan poin ospek selama permainan.
- **Mode jelajah bebas** — pindah lokasi kampus dan mengobrol dengan karakter
  (tersedia sebagai pilihan setiap hari).
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

- Setiap hari kamu memilih **satu kegiatan** dari menu.
- Kegiatan menguras **stamina**; jika stamina < 20 kamu hanya bisa istirahat.
- **Hari 3** ada kuis AIK, **Hari 5** ada tantangan kerja tim.
- Setelah **7 hari**, nilai akhir dan ending dihitung dari poin ospek, total
  kedekatan, dan statistikmu.

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
