#string dalam Python dikelilingi oleh tanda kutip tunggal (') atau tanda kutip ganda (")
print("Hai")
print('Hai')

#string dalam string
print("She's so crazy")
print("She has 'something' she can not share")
print('My name is "David"')

#menetapkan string ke variabel
a = "Hai"
print(a)

#multiline string
a = """Aku berjalan mengikuti bayang-bayangku 
sendiri yang memanjang di depan. Aku dan matahari 
tidak bertengkar tentang siapa di antara kami 
yang telah menciptakan bayang-bayang..." 
— Sapardi Djoko Damono."""
print(a)

#string adalah array
a = "Hai!"
print(a[3])

#perulangan melalui string
for x in "Algoritma":
      print(x)

#panjang string
a = "Halo Dunia!"
print(len(a))

#SLICING
#dapatkan karakter dari posisi 2 hingga posisi 5 (tidak termasuk):

b = "Hai Dunia!"
print(b[1:2])

#slice dari awal
b = "Hai Dunia!"
print(b[:3])

#slice hingga ujung
b = "Hai Dunia!"
print(b[2:])

#pengindeksan negatif
b = "Hai Dunia!"
print(b[-1:-2])

#MEMODIFIKASI STRING
#upper case
a = "Algoritma Pemrograman"
print(a.upper())

#lower case
a = "Struktur Data"
print(a.lower())

#hapus whitecase
a = " Belajar Python "
print(a.strip()) # returns "Hello, World!"

#replace string
a = "Bunga Raya"
print(a.replace("R", "J"))

#split string
a = "Bunga,Raya"
print(a.split(",")) # returns ['Bunga', ' Raya']

#PENGGABUNGAN STRING
#menggambungkan variabel adengan variabel b ke dalam variabel c
a = "Terima"
b = "kasih"
c = a + b
print(c)

#untuk menambahkan spasi di antara keduanya, tambahkan tanda titik dua ( " ":).
a = "Terima"
b = "kasih"
c = a + " " + b
print(c)

#FORMAT STRING
#F-String
age = 20
txt = f"Namaku Aisyah. Aku berumur {age}"
print(txt)

#placeholder dan modifier
price = 40000
txt = f"Harga minyak goreng saat ini adalah {price} rupiah" 
print(txt)

price = 40
txt = f"Harga minyak goreng saat ini adalah {price:.3f} rupiah" #pengubah dapat disertakan dengan menambahkan ":" dan diikuti format yang sah
print(txt)

txt = f"Harga minyak goreng baik dua kali lipat yaitu sebesar {20000 * 2} rupiah " #pengubah dapat berisi kode Python seperti operasi matematika
print(txt)