sesuatu = ["A","B","C","A","A","B","A"]

unik = set(sesuatu)

frekuensi = {}
for x in sesuatu:
    frekuensi[x] = frekuensi.get(x,0) + 1

hitung_max = max(frekuensi.values())

pemenang = [x for x ,y in frekuensi.items() if y == hitung_max]

print(f"Laporan Frekuensi: {frekuensi}")
print(f"Kategori Paling Sering Muncul: {pemenang} (Muncul {hitung_max} kali)")
print(unik)