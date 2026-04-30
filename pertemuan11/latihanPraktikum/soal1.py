class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None   


class RS:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        self.length = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, nama, keluhan):
        pasien_baru = Node(nama, keluhan)
        self.count +=1
        if self.rear is None:
            self.front = self.rear = pasien_baru
        else:
            self.rear.next = pasien_baru
            self.rear = pasien_baru
        self.length +=1
        print(f"[daftar]{nama} terdaftar dengan keluhan: {keluhan} (No.antrian: {self.count})")

    def dequeue(self):
        if self.is_empty():
            return None
        
        temp = self.front
        self.front = self.front.next
        self.length -= 1
        self.count -= 1
        if self.front is None:
            self.rear = None

        return temp
    
    def peek(self):
        return self.front
    
    
    def size(self):
        return self.length
    
    def clear(self):
        self.front = None
        self.rear = None
        self.length = 0 
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def tampilkan_antrian(self):
        if self.is_empty():
            print("antrian kosong")
            return
        
        temp = self.front
        i = 1
        while temp:
            print(f"{i}. {temp.nama} -> {temp.keluhan}")
            temp = temp.next
            i += 1

    
print("=" *30)
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("=" *30)

antrian = RS()

status = "Ya, antrian masih kosong." if antrian.is_empty() else "Tidak"
print(f"\n[CEK] apakah antrian kosong? {status}")

antrian.enqueue("BUDI", "demam tinggi")
antrian.enqueue("ANI", "batuk pilek")
antrian.enqueue("CITRA", "sakit kepala")

print(f"\n[info] jumlah pasien menunggu : {antrian.size()} orang")

pasien_terdepan = antrian.peek()
if pasien_terdepan:
    print(f"\n[PEEK] pasien berikutnya: {pasien_terdepan.nama} - {pasien_terdepan.keluhan}")

panggil = antrian.dequeue()
if panggil:
    print(f"\n[PANGGIL] dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")

antrian.enqueue("DODI", "nyeri perut")

print("\n[ANTRIAN SAAT INI]")
antrian.tampilkan_antrian()

panggil = antrian.dequeue()
if panggil:
    print(f"\n[PANGGIL] Dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")

print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

antrian.clear()

status = "YA, antrian sudah kosong." if antrian.is_empty() else "TIDAK."
print(f"\n[CEK] Apakah antrian kosong? -> {status}")

print("=" * 30)
print("Simulasi Selesai!")
print("=" * 30)