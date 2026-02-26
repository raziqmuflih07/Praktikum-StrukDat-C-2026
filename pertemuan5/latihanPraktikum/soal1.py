stok_barang = [15,40,30,10,25]

stok_barang[stok_barang.index(10)] = 50
print(stok_barang)
stok_barang.append(5)
stok_barang.sort(reverse=True)

jumlahTotal= sum(stok_barang)

print(jumlahTotal)

print("stok aman" if jumlahTotal/len(stok_barang) > 20 else "waspada")
