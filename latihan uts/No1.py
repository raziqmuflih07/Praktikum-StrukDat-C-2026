buah = [
    {"nama": "Apel", "harga": 25000},
    {"nama": "Jeruk", "harga": 15000},
    {"nama": "Mangga", "harga": 18000},
    {"nama" : "Naga", "harga" : 30000}
]

murah = [x for x in buah if x["harga"] < 20000]

mahal = [x for x in buah if x["harga"] > 20000]

print(murah)
print(mahal)