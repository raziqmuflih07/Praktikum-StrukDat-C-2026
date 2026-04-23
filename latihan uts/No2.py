pass
#gk ada contoh di w3

# 1. TUPLE: Digunakan untuk data yang tidak boleh diubah (Fixed)
# Contoh: Daftar kategori servis yang tersedia di toko
kategori_tetap = ("Hardware", "Software", "Maintenance")

# 2. LIST DATA: Data input yang berisi banyak duplikat
servis_hari_ini = ["Hardware", "Software", "Hardware", "Maintenance", "Hardware", "Software"]

# 3. SET: Digunakan untuk mendapatkan nilai unik dari koleksi data 
kategori_unik = set(servis_hari_ini) 

# 4. DICTIONARY: Menghitung frekuensi kemunculan 
frekuensi = {}
for k in servis_hari_ini:
    # Mengisi dictionary: {nama_kategori: jumlah_muncul}
    frekuensi[k] = frekuensi.get(k, 0) + 1 

# 5. MENCARI NILAI TERTINGGI (Modus) 
# Mencari angka kemunculan paling besar
max_hitung = max(frekuensi.values())

# Menentukan kategori mana yang punya jumlah = max_hitung
# (Bisa lebih dari satu nilai jika jumlahnya sama) 
pemenang = [key for key, val in frekuensi.items() if val == max_hitung]

# --- OUTPUT ---
print(f"Daftar Kategori Unik: {kategori_unik}")
print(f"Laporan Frekuensi: {frekuensi}")
print(f"Kategori Paling Sering Muncul: {pemenang} (Muncul {max_hitung} kali)")