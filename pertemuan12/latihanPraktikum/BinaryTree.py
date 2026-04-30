class node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = node('A')
        self.root.left = node('B')
        self.root.right = node('C')

        self.root.left.left = node('D')
        self.root.left.right = node('E')

        self.root.right.left = node('F')    
        
    def traverse_preorder(self,node, result = None):
        if result is None:
            result = []

        if node:
            result.append (node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)
        return result


    def traverse_Inorder(self, node, result = None):
        if result is None:
            result = []
        if node:
            self.traverse_Inorder(node.left, result)
            result.append (node.data)
            self.traverse_Inorder(node.right, result)
        return result
    
    def traverse_postorder(self, node, result = None):
        if result is None:
            result = []
        if node :
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append (node.data)
        return result
    
    def get_leaf_nodes(self, node, result = None):
        if result is None:
            result = []
            
        if node:
            if not node.left and not node.right:
                result.append(node.data)
            self.get_leaf_nodes(node.left, result)
            self.get_leaf_nodes(node.right, result)
        return result
    
print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI' ")
print("=" * 30)
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

Tree = BinaryTree()

Tree.insert_manual()
preorder = Tree.traverse_preorder(Tree.root)
inorder = Tree.traverse_Inorder(Tree.root)
postorder = Tree.traverse_postorder(Tree.root)

print("HASIL AUDIT:")
print(f'1. Pre-Order: {"-".join(preorder)}')
print(f"2. In-Order: {'-'.join(inorder)}")
print(f"3. Post-Order: {'-'.join(postorder)}")

leaf = Tree.get_leaf_nodes(Tree.root)
print(f"[DATA] Gudang Ujung (Leaf Nodes): {",".join(leaf)}")
print("=" * 30)
print('Audit Selesai!')