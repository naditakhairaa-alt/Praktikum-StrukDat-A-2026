class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

#insert manual
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

pohon = BinaryTree()

#skenario pengujian
pohon.insert_root("A") 
pohon.insert_left(pohon.root, "B")
pohon.insert_left(pohon.root.left, "D")
pohon.insert_right(pohon.root.left, "E")
pohon.insert_right(pohon.root, "C")
pohon.insert_right(pohon.root.right, "F")

#mengecek gudang utama sebelum cabang-cabangnya
def traverse_preorder(node):
    if node is None:
        return
    print(node.data, end=" - ")
    traverse_preorder(node.left)
    traverse_preorder(node.right)

#mengecek dari jalur kiri, lalu pusat, baru ke kanan
def traverse_inorder(node):
    if node is None:
        return
    traverse_inorder(node.left)
    print(node.data, end=" - ")
    traverse_inorder(node.right)

#mengecek semua cabang terlebih dahulu sebelum kembali ke gudang pusat
def traverse_postorder(node):
    if node is None:
        return
    traverse_postorder(node.left)
    traverse_postorder(node.right)
    print(node.data, end=" - ")

#menampilkan daftar gudang yang merupakan leaf node
def get_leaf_nodes(node):
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.data]
    
    return get_leaf_nodes(node.left) + get_leaf_nodes(node.right)
    pass

#tampilan 
print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

print("\nHASIL AUDIT:")
print("1. Pre-Order  : ", end="")
traverse_preorder(pohon.root)
print("\n2. In-Order   : ", end="")
traverse_inorder(pohon.root)
print("\n3. Post-Order : ", end="")
traverse_postorder(pohon.root)

print("\n")
print(f"[DATA] Gudang Ujung (Leaf Nodes): {get_leaf_nodes(pohon.root)}")
print("======================================")
print("Audit Selesai!")