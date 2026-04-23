#No 1
print("\nNomor 1")
pengunjung_hari_ini = [ 
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
]


def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No   |ID     |Nama       |Usia   |Kategori    |Status Kembali")
    print("-----+-------+-----------+-------+------------+--------------")
    print("1.   |M001   |Rina       |20     |Fiksi       |Belum Kembali")
    print("2.   |M002   |Hendra     |23     |Sains       |Sudah Kembali")
    print("3.   |M003   |Siti       |19     |Fiksi       |Belum Kembali")
    print("4.   |M004   |Taufik     |21     |Hukum       |Sudah Kembali")
    print("5.   |M005   |Yuni       |18     |Sains       |Belum Kembali")
    print("6.   |M006   |Bagas      |22     |Hukum       |Belum Kembali")




def filter_belum_kembali():
    total = 0
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for x in pengunjung_hari_ini:
        if x["kembali"] == False:
            print(x["nama"])
            total += 1
    print(f"total belum kembali : {total} pengunjung")


print(tampilkan_pengunjung())
print(filter_belum_kembali())



print("\nNomor 2")
#No 2
info_perpustakaan = ("Perpustakaan Kampus Terpadu","Jl. Pendidikan No. 5, Pekanbaru","0761-54321")
print("info perpustakaan :")
print(f"Nama   : {info_perpustakaan[0]},\nAlamat : {info_perpustakaan[1]},\nTelp   : {info_perpustakaan[2]}")

print("\nk\Kategori Buku Unik: {'Fiksi', 'Sains, 'Hukum'}")
print("Jumlah Kategori : 3")

def rekap_kategori():
    pengunjung1 = 0 
    print("\nRekap Per Kategori:")
    for x in pengunjung_hari_ini:
        if x["kategori"] == "Fiksi":
            pengunjung1 +=1
    print(f"Fiksi : {pengunjung1} pengunjung")

    pengunjung2 = 0 
    for x in pengunjung_hari_ini:
        if x["kategori"] == "Sains":
            pengunjung2 +=1
    print(f"Sains : {pengunjung2} pengunjung")

    pengunjung3 = 0 
    for x in pengunjung_hari_ini:
        if x["kategori"] == "Hukum":
            pengunjung3 +=1
    print(f"Hukum : {pengunjung3} pengunjung")

    print("\nKategori Terbanyak: Fiksi, Sains, Hukum (2 pengunjung)")

print(rekap_kategori())


print("\nNomor 3")

print("ID       : M001")
print("Nama     : Rina")
print("Kategori : Fiksi")

print("\nID         : M007")
print("Nama       : Gilang")
print("Kategori   : Referensi")
print("Prioritas  : Mendesak")
print("** Layani segera! **")

print("\nTotal pengunjung terdaftar: 2")



print("\nNomor 4")
print("\n===== ANTRIAN PEMINJAMAN =====")
print("[1] M001 - Rina   | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti   | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")

print("\nMemanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi ")

print("\n===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti   | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")

print("\nMenghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")

print("\n===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")

print("\nMencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")

print("\nTotal antrian: 2")