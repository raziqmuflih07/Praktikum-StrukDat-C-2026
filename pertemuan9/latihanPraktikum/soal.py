# --- BAGIAN 1 & 2: DOUBLE LINKED LIST ---

class NodeDLL:
    def __init__(self, plat):
        self.plat = plat
        self.next = None 
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = NodeDLL(plat)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node 

    def hapus_kendaraan(self, plat):
        current = self.head
        while current:
            if current.plat == plat:
                if current.prev:
                    current.prev.next = current.next 
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev 
                else:
                    self.tail = current.prev 
                return
            current = current.next

    def tampilkan_maju(self):
        current = self.head 
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):
        current = self.tail 
        while current:
            print(current.plat)
            current = current.prev


# --- BAGIAN 3: CIRCULAR LINKED LIST ---

class NodeCLL:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_valet = None

    def tambah_petugas(self, nama):
        new_node = NodeCLL(nama) 
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = self.head 
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head 
        self.current_valet = self.head 

    def giliran_berikutnya(self, n):
        for i in range(1, n + 1):
            print(f"Giliran {i}: {self.current_valet.nama}") 
            self.current_valet = self.current_valet.next

# ==========================================
# MENJALANKAN TESTING SESUAI MODUL
# ==========================================

if __name__ == "__main__":
    print("=== SOAL 1: Double Linked List (Maju & Mundur) ===")
    parkir = DoubleLinkedList()
    parkir.tambah_kendaraan("B 1234 ABC") 
    parkir.tambah_kendaraan("D 5678 XYZ") 
    parkir.tambah_kendaraan("A 9999 TUV")
    
    print("[Maju]")
    parkir.tampilkan_maju() 
    print("[Mundur]")
    parkir.tampilkan_mundur() 
    print("-" * 30)

    print("=== SOAL 2: Hapus Kendaraan Tengah ===")
    parkir_hapus = DoubleLinkedList()
    parkir_hapus.tambah_kendaraan("B 1111 AA") 
    parkir_hapus.tambah_kendaraan("D 2222 BB") 
    parkir_hapus.tambah_kendaraan("A 3333 CC") 
    parkir_hapus.tambah_kendaraan("B 4444 DD")
    
    print("Sebelum:")
    parkir_hapus.tampilkan_maju() 
    parkir_hapus.hapus_kendaraan("A 3333 CC") 
    print("Sesudah:")
    parkir_hapus.tampilkan_maju() 
    print("-" * 30)

    print("=== SOAL 3: Circular Linked List (Valet) ===")
    valet = CircularLinkedList()
    valet.tambah_petugas("Andi") 
    valet.tambah_petugas("Budi") 
    valet.tambah_petugas("Citra")
    valet.tambah_petugas("Dewi")
    
    valet.giliran_berikutnya(6) 