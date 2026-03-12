def ganjil_genap(plat):
    ganjil=[]
    genap=[]
    for i in plat:
        nomor = int (i.split(" ")[1])
        if nomor % 2 == 0 :
            genap.append(i)
        else:
            ganjil.append(i)
    return ganjil,genap
    
ganjil,genap = ganjil_genap(["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"])
print(ganjil)
print(genap)