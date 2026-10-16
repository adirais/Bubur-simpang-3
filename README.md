# BST OS

Aplikasi operasional Bubur Simpang Tiga: kasir, prep harian, closing kas & checklist, absensi selfie, stok bahan, order & pembelian bahan, keuangan, dan analitik.

**Alamat:** https://adirais.github.io/Bubur-simpang-3/

Staf masuk dengan **username + PIN 6 angka**. Data tersimpan di Supabase (proyek `bubur-simpang-3`, Singapura) dan dijaga per peran langsung di database.

## Cara kerja

| Bagian | Di mana |
|---|---|
| Halaman web (file di repo ini) | GitHub Pages, branch `main`, folder root |
| Data, login, foto absensi | Supabase `bubur-simpang-3` |
| Fungsi server `admin-staff` (akun staf) | Supabase Edge Functions — kodenya di `supabase/functions/` |

Setiap perubahan yang di-commit ke `main` tayang otomatis dalam 1–2 menit. Aplikasi yang sedang terbuka akan menampilkan tombol "Muat ulang" saat ada versi baru.

## Pertama kali

Buka alamat web → isi **Buat akun Owner** (nama, username, PIN). Form ini hanya muncul selama belum ada akun sama sekali.

## Siapa bisa apa

| Peran | Akses |
|---|---|
| Owner / Manager | Semua menu, termasuk Keuangan, Analitik, Pengaturan, stock opname, setujui order, batalkan transaksi |
| Kasir | Kasir, Prep, Closing kas & checklist, Absensi, Stok & waste, Order bahan |
| Dapur | Prep, Checklist, Absensi, Stok & waste, Order & Pembelian bahan |

Akun Owner hanya bisa diatur oleh Owner. Staf yang dinonaktifkan langsung kehilangan akses.

## Menambah staf

Pengaturan → Staf → Tambah staf: nama, username, peran, PIN 6 angka. Beri tahu PIN langsung ke staf. Di HP/tablet staf: buka alamat web → **Add to Home Screen** (iPhone: tombol Share; Android: menu ⋮).

## Alur harian

1. **Absen masuk** (selfie) → **checklist opening**
2. **Catat prep** per menu → bahan baku terpotong otomatis sesuai resep
3. **Kasir** (tunai / QRIS) → porsi tersedia berkurang
4. **Tutup prep**: waste & porsi yang disimpan (menjadi "sisa kemarin" besok)
5. **Closing kas**: hitung laci, cek mutasi QRIS, setoran → selisih tercatat
6. **Checklist closing** → **absen pulang**

Stok di bawah minimum muncul sebagai **saran order** (jumlah = par − stok). Order: dibuat → disetujui & dipesan (Owner/Manager, salin pesan WA ke supplier) → **terima barang** dengan harga di nota → tercatat sebagai pembelian (lunas atau utang) dan stok bertambah.

## Perawatan

- **Cadangan mingguan:** Pengaturan → Cadangan → Unduh cadangan. Jangan unggah file cadangan ke repo ini — repo ini publik.
- **Paket gratis Supabase** dijeda bila tidak dipakai sekitar seminggu; pemakaian harian mencegahnya. Jika terjeda: dashboard Supabase → Restore.

## Isi repo

```
index.html              aplikasi (hasil build dari src/)
src/index.src.html      sumber aplikasi; logo disisipkan oleh src/build.py
config.js               alamat Supabase + anon key (boleh publik; data dijaga login + RLS)
manifest.webmanifest    mode aplikasi di HP/tablet
sw.js                   service worker minimal (tanpa cache)
assets/                 logo BST (SVG & PNG HD) dan ikon aplikasi
supabase/functions/     fungsi server admin-staff (arsip; sudah terpasang)
```
