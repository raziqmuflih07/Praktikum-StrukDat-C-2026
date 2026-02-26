ukm_coding = {"Andi","Budi","Caca","Deni"}
ukm_robotik = {"Caca","Deni","Euis","Fafa"}

only_ukm_coding= ukm_coding - ukm_robotik
mahasiswa_unik = ukm_robotik | ukm_coding

print(only_ukm_coding)
print(mahasiswa_unik)
print("Andi" in ukm_robotik)
