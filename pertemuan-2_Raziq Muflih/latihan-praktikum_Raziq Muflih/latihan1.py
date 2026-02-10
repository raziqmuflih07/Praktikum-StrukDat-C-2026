stok = [15, 50, 30, 25, 40]

stok.append(100)
print(stok)

stok.insert(2, 75)
print(stok)

stok.sort(reverse=True)
print(stok)

jumlah = 0

for x in stok:
    jumlah += x

rata2=jumlah / len(stok)

print('jumlah rata-ratanya',rata2)

