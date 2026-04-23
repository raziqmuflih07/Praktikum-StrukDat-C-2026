class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")


def tambahKendaraan(head, plat):
    currentNode = head
    while currentNode.next:
      currentNode=currentNode.next
  
    currentNode.next = plat

def hapusKendaraan(head,hapusplat):
   if head == hapusplat:
      return head.next
   
   currentNode = head
   while currentNode.next and currentNode.next != hapusplat:
    currentNode = currentNode.next

   if currentNode.next is None:
    return head

   currentNode.next = currentNode.next.next

   return head

node1 = Node("B 2921 WEJ")
node2 = Node("SD 9863 IWUE")
node3 = Node("WE 2377 NMD")
node4 = Node("SW 2323 EY")
node5 = Node("WJ 3209 EIU")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("antrean awal:")
traverseAndPrint(node1)

newNode = Node("qw 2839 ei")
tambahKendaraan(node1, newNode)

print("\nsesudah ditambah:")
traverseAndPrint(node1)

print("sebelum dihapus:")
traverseAndPrint(node1)

node1 = hapusKendaraan(node1, node4)

print("\nsetelah dihapus:")
traverseAndPrint(node1)