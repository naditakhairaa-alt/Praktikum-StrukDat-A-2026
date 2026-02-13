hewan = ["ikan", "ayam", "sapi"]
print(hewan)

#duplikat
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#panjang list
hewan = ["ikan", "ayam", "sapi", "kambing",]
print(len(hewan))

#tipe
mylist = ["contoh", "list", "type"]
print(type(mylist))

#LIST ACCESS
hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci"]
print(hewan[3])

#indeks negatif
hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci"]
print(hewan[-3])

#rentang akses
hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci", "kucing", "harimau"]
print(hewan[2:5])

hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci", "kucing", "harimau"]
print(hewan[:3])

#rentang akses negatif
hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci", "kucing", "harimau"]
print(hewan[-4:-1])

#periksa barang ada
hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci"]
if "kelinci" in hewan:
  print("Iya, kelinci ada di dalam list")

#CHANGE ITEMS LIST
#Change Item Value
barang = ["meja", "kursi", "lampu"]
barang[1] = "kasur"
print(barang)

barang = ["meja", "kursi", "lampu", "tv", "kipas", "lemari"]
barang[1:2] = ["charger", "handphone"]
print(barang)

#insert
barang = ["meja", "kursi", "lampu"]
barang.insert(2, "charger")
print(barang)

#tambahkanitem
hewan = ["ikan", "ayam", "sapi"]
hewan.append("paus")
print(hewan)

hewan = ["ikan", "ayam", "sapi"]
mamalia = ["paus", "gajah", "harimau"]
hewan.extend(mamalia)
print(hewan)

#remove
hewan = ["ikan", "ayam", "sapi"]
hewan.remove("ikan")
print(hewan)

hewan = ["ikan", "ayam", "sapi"]
hewan.pop(1)
print(hewan)

hewan = ["ikan", "ayam", "sapi"]
del hewan[0]
print(hewan)

hewan = ["ikan", "ayam", "sapi"]
del hewan #menghapus semua list

hewan = ["ikan", "ayam", "sapi"]
hewan.clear()
print(hewan)

#loop
hewan = ["ikan", "ayam", "sapi"]
for x in hewan:
  print(x)

hewan = ["ikan", "ayam", "sapi"]
for i in range(len(hewan)):
  print(hewan[i])

hewan = ["ikan", "ayam", "sapi"]
i = 0
while i < len(hewan):
  print(hewan[i])
  i = i + 1

#list comprehension
hewan = ["ikan", "ayam", "sapi", "kambing", "kelinci"]
binatang = [x for x in hewan if "i" in x]

print(binatang)

#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#reverse sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#menyalin
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#gabungkan
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)