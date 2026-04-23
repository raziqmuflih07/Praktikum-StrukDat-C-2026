class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        # Tulis kode di sini (Petunjuk: periksa apakah top bernilai None)
        return self.count == 0
    
    def push(self, url):
        # Tulis kode di sini
        # 1. Buat Node baru
        # 2. Hubungkan 'next' node baru ke 'top' saat ini
        # 3. Jadikan node baru sebagai 'top' yang baru
        # 4. Tambahkan nilai 'count'
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    
    def pop(self):
    # Tulis kode di sini
    # 1. Periksa is_empty()
    # 2. Simpan url dari 'top' saat ini
    # 3. Geser 'top' ke node berikutnya (top = top.next)
    # 4. Kurangi nilai 'count'
    # 5. Kembalikan url yang disimpan
        if self.is_empty():
            return "url kosong"
        hapus_node = self.top
        self.top = self.top.next
        self.count -= 1
        return hapus_node.url

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
        if self.is_empty():
            return "url kosong"
        return self.top.url

    def size(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai variabel 'count')
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()

dataurl = StackLinkedList()

dataurl.push("https://www.w3schools.com/python/python_dsa_stacks.asp")
dataurl.push("https://www.w3schools.com/python/default.asp")
dataurl.push("https://www.w3schools.com/python/python_intro.asp")

print("LinkedList: ", end="")
dataurl.traverseAndPrint()
print("Peek: ", dataurl.peek())
print("Pop: ", dataurl.pop())
print("LinkedList after Pop: ", end="")
dataurl.traverseAndPrint()
print("isEmpty: ", dataurl.is_empty())
print("Size: ", dataurl.size())