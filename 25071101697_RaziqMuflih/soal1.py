def registrasi_gadget():
    merk = "redmi"
    tipe = "pro"
    harga = 3699000
    sn = "578125"

    if harga < 1000000:
        print("harga tidak valid,mohon masukkan harga yang sesuai")
        return None
    elif len(sn) <= 5 :
        print("serial number minimal harus 5 karakter,harap masukkan SN ulang")
        return None
    else :
        print("Tersedia")
        print(merk,tipe,harga,sn)

registrasi_gadget()

def program():
    inventaris = []
    for i in range(3):
       merk=input("masukkan merk= ")
       tipe=input("masukkan tipe= ")
       harga=input("masukkan harga= ")
       sn=input("masukkan serial number =" )

program()
print (program)