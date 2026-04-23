class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

def tampil_antrian(head):
    currentNOde=head
    while currentNOde:
        print(currentNOde.data,end= " ==> ")
        currentNOde = currentNOde.next
    print("Null")

def sisipkan_vvip(head,card_baru,card_target):
    if card_target == 1:
        card_baru.next = head
        return card_baru
        
    CurrentNode = head
    for _ in range(card_target - 2):
        if CurrentNode.next is None:
            break
        CurrentNode = CurrentNode.next

    card_baru.next = CurrentNode.next
    CurrentNode.next = card_baru
    return head
    
node1 = Node(1) 
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next =node3
node3.next = node4

print("antrian asli : ")
tampil_antrian(node1)

card_baru= Node(0)
node1 = sisipkan_vvip(node1, card_baru,2)

print("antrian sesudah vip : ")
tampil_antrian(node1)

