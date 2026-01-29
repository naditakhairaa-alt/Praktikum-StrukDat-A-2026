#Nilai Boolean
'''
Boolean hanya mengeluarkan nilai True (Benar) 
atau False (Salah) untuk membandingkan dua nilai
'''
print(20 >= 11)
print(13 == 12)
print(20 < 25)

#menjalankan suatu kondisi dengan pernyataan if
y = 555
z = 444

if z > y:
  print("z lebih besar dari y")
else:
  print("z lebih kecil dari y")

#mengevaluasi nilai dan variabel
print(bool("Batik"))
print(bool(20))

#evaluasi dua variabel
x = "Ayam"
y = 79

print(bool(x))
print(bool(y))

#sebagian besar nilai adalah benar
'''
Semua string adalah True, kecuali string kosong,
semua angka adalah True, kecuali 0,
semua list, tuple, set, dan dictionary adalah True, kecuali yang kosong.
'''
bool("ayce")
bool(2026)
bool(["sapi", "ikan", "ayam"])

#nilai salah
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#fungsi dapat mengembalikan nilai boolean
def akuPelaut() :
  return True

print(akuPelaut())

def akuPelaut() :
  return True

if akuPelaut(): #menjalankan kode berdasarkan jawaban boolean dari suatu fungsi
  print("YEY!")
else:
  print("YAH!")

x = 20.0
print(isinstance(x, float))