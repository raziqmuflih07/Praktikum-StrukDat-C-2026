class node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None

    def insert(self, id_buku,judul):
        if self.root is None:
            self.root = node(id_buku,judul)
        else:
            self.insertRecursive(self.root, id_buku, judul)
        print(f"[INSERT] berhasil memasukkan: ID {id_buku} - {judul}")


    def insertRecursive(self, current, id_buku, judul):
        if id_buku < current.id_buku:
            if current.left is None:
                current.left = node(id_buku, judul)
            else:
                self.insertRecursive(current.left, id_buku, judul)
        elif id_buku > current.id_buku:
            if current.right is None:
                current.right = node(id_buku, judul)
            else:
                self.insertRecursive(current.right, id_buku, judul)

    def search(self, id_buku):
        return self.searchRecursive(self.root, id_buku)
    
    def searchRecursive(self, current, id_buku):
        if current is None:
            return None
        if id_buku == current.id_buku:
            return current
        if id_buku < current.id_buku:
            return self.searchRecursive(current.left, id_buku)
        return self.searchRecursive(current.right, id_buku)
    
    def traversal_inorder(self):
        self.counter = 1
        self.inorder_recursive(self.root)

    def inorder_recursive(self, current):
        if current:
            self.inorder_recursive(current.left)
            print(f"{self.counter}. {current.id_buku} - {current.judul}")
            self.counter += 1
            self.inorder_recursive(current.right)

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.id_buku
    
    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.id_buku
    
    def height(self):
        return self.height_recursive(self.root)
    
    def height_recursive(self, current):
        if current is None:
            return -1 
        left_h = self.height_recursive(current.left)
        right_h = self.height_recursive(current.right)
        return 1 + max(left_h, right_h)


print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG' ")
print("=" * 50)

katalog = bst()

data_buku = [
    (50, "Dasar Pemrograman"), (30, "Struktur Data"),
    (70, "Kecerdasan Buatan"), (20, "Matematika Diskrit"),
    (40, "Basis Data"), (60, "Jaringan Komputer"),
    (80, "Sistem Operasi")
    ]

for id_b, judul_b in data_buku:
    katalog.insert(id_b, judul_b)


print("\n[INFO] koleksi buku (in-order traversal):")
katalog.traversal_inorder()

print("\n")
for cari_id in [60, 100]:
    hasil = katalog.search(cari_id)
    if hasil :
        print(f"[SEARCH] mencari ID {cari_id} ... Ditemukan! judul: {hasil.judul}")
    else:
        print(f"[SEARCH] mencari ID {cari_id} ... data tidak ditemukan.")


print(f"\n[STATISTIK] ID Terkecil: {katalog.get_min()}")
print(f"[STATISTIK] ID Terbesar: {katalog.get_max()}")

print(f"[INFO] tinggi (height) Tree : {katalog.height()}")
print("=" *50)
print("simulasi selesai!")
