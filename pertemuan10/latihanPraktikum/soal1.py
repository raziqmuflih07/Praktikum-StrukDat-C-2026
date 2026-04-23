class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
        
    def push(self, url):
        # Tulis kode di sini (Petunjuk: gunakan append)
        self.items.append(url)

    def pop(self):
        # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
        if self.is_empty():
            return "url kosong"
        return self.items.pop()
    
    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
        if self.is_empty():
            return "url kosong"
        return self.items[-1]
    
    def is_empty(self):
        # Tulis kode di sini
        return len(self.items) == 0
    
    def size(self):
        # Tulis kode di sini (Petunjuk: gunakan len())
        return len(self.items)
    

dataurl = StackList()


dataurl.push("https://www.w3schools.com/python/default.asp")
dataurl.push("https://www.w3schools.com/python/python_intro.asp")
dataurl.push("https://www.w3schools.com/python/python_dsa_stacks.asp")

print("list URL : ", dataurl.items)
print("URL yg dihapus : ",dataurl.pop())
print("list URL setelah dihapus : ",dataurl.items)   
print("list URL peek : ", dataurl.peek())
print("apakah list URL kosong : ",dataurl.is_empty())
print("size list :",dataurl.size())