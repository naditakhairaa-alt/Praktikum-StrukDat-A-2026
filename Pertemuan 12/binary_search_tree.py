class TreeNode:
    def __init__ (self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    #insert manual
    def insert(self, id_buku, judul):
        def _insert(node, id_buku, judul):
            if node is None:
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                return TreeNode(id_buku, judul)
            
            if id_buku < node.id:
                node.left = _insert(node.left, id_buku, judul)
            elif id_buku > node.id:
                node.right = _insert(node.right, id_buku, judul)
            return node
        self.root = _insert(self.root, id_buku, judul)

    #cari berdasarkan id
    def search(self, id_buku):
        def _search(node, id_buku):
            if node is None:
                return None
            if id_buku == node.id:
                return node
            elif id_buku < node.id:
                return _search(node.left, id_buku)
            else:
                return _search(node.right, id_buku)
            
        return _search(self.root, id_buku)

    #menemukan id terkecil
    def get_min(self):
        node = self.root
        while node and node.left is not None:
                node = node.left
        return node

    #menemukan id terbesar
    def get_max(self):
        node = self.root
        while node and node.right is not None:
            node = node.right
        return node
    
    #menghitung tinggi tree yang terbentuk
    def height_tree(self, node):
        if node is None:
            return -1
        return 1 + max (self.height_tree(node.left), self.height_tree(node.right))

#menampikan koleksi buku dengan urut dari id terkecil ke terbesar
def traverse_inorder(node, nomor=[1]):
    if node is not None:
        traverse_inorder(node.left, nomor)

        print(f"{nomor[0]}. {node.id} - {node.judul}")
        nomor[0] += 1

        traverse_inorder(node.right, nomor)


bst = BST()
#tampilan
print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Informasi")

print("\n[INFO] Koleksi Buku (In-Order Travesal): ")
traverse_inorder(bst.root)

searching1 = 60
hasil_searching1 = bst.search(searching1)
print(f"\n[SEARCH] Mencari {searching1}... Ditemukan! Judul: {hasil_searching1.judul}")

searching2 = 100
hasil_searching2 = bst.search(searching2)
if hasil_searching2:
    print(f"[SEARCH] Mencari {searching2}... Ditemukan! Judul: {hasil_searching2.judul}")
else:
     print(f"[SEARCH] Mencari ID {searching2}... Data Tidak Ditemukan.")


minimal = bst.get_min()
maximal = bst.get_max()
tinggi_tree = bst.height_tree(bst.root)
print(f"\n[STATISTIK] ID Terkecil: {minimal.id} ")
print(f"[STATISTIK] ID Terbesar: {maximal.id}")
print(f"[INFO] Tinggi (Height) Tree: {tinggi_tree} ")

print("=========================================")
print("Simulasi Selesai!")