#tipe data bawaan
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

#mendapatkan tipe datanya
x = 10
print(type(x))

#mengatur tipe datanya
x = "Halo Dunia!"	#str	
x = 20         	#int	
x = 20.5       	#float	
x = 1j	            #complex	
x = ["Geprek", "Mie", "Bakso"]	#list	
x = ("Ayam", "Sapi", "Ikan")	#tuple	
x = range(6)	#range	
x = {"nama" : "James", "Umur" : 20}	#dict	
x = {"Semangka", "Melon", "Apel"}	#set	
x = frozenset({"Semangka", "Melon", "Anggur"})	#frozenset	
x = True	#bool	
x = b"Hai"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

#menetapakan tipe data tertentu
x = str("Halo Dunia")	#str	
x = int(20)	#int	
x = float(20.5)    #float	
x = complex(1j)	#complex	
x = list(("Semangka", "Melon", "Anggur"))	#list	
x = tuple(("Semangka", "Melon", "Anggur"))	#tuple	
x = range(6)	#range	
x = dict(Nama="Kevin", age=20)	#dict	
x = set(("Semangka", "Melon", "Anggur"))	#set	
x = frozenset(("Geprek", "Mie", "Bakso"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
