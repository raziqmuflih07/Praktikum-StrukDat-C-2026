class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def tampilkan_antrean(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sisipkan_vip(head, plat_baru, plat_target):
  if plat_target == 1:
    plat_baru.next = head
    return plat_baru

  currentNode = head
  for _ in range(plat_target - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  plat_baru.next = currentNode.next
  currentNode.next = plat_baru
  return head

node1 = Node("a 2382 yd")
node2 = Node("ks 3742 iw")
node3 = Node("wi 2920 owe")
node4 = Node("qp 23761 eqw")

node1.next = node2
node2.next = node3
node3.next = node4

print("antrean awal:")
tampilkan_antrean(node1)

plat_baru = Node("sd 2739 ei")
node1 = sisipkan_vip(node1, plat_baru, 2)

print("\nsetelah ditambah:")
tampilkan_antrean(node1)