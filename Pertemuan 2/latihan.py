#1.1
nilai = [75, 80, 65, 90, 85]
nilai.append(95)
print(nilai)

#1.2
nilai = [75, 80, 65, 90, 85]
nilai.remove(65)
print(nilai)

#1.3
nilai = [75, 80, 65, 90, 85]
nilai.sort()
print(nilai)

#1.4
nilai = [75, 80, 65, 90, 85]
print(max(nilai))
print(min(nilai))
print(len(nilai))

#1.5
nilai = [75, 80, 65, 90, 85, 95]
print(sum(nilai)/len(nilai))

#1.6
print(nilai)

#2.1
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print(dosen[1:-1])

#2.2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
for x in dosen:
    print(x)

#2.3
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
y = list(dosen)
y[3] = 14
x = tuple(y)

print(x)

#2.3
#tuple tidak dapat berubah ubah

#3.1
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
keahlian_AB = keahlian_A.union(keahlian_B)
print(keahlian_AB)

#3.2 
keahlian_A = frozenset({"Python", "Java", "SQL", "Git"})
print(keahlian_A)

#3.3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

keahlian_AB = keahlian_A | keahlian_B
print(keahlian_AB)

#3.4
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
print("Java" in keahlian_B)


