thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

hewan = ("ikan", "ayam", "sapi")
print(hewan[1])

#negatif
hewan = ("ikan", "ayam", "sapi")
print(hewan[-1])

hewan = ("ikan", "ayam", "sapi", "kambing", "kelinci", "kucing", "harimau")
print(hewan[2:5])

hewan = ("ikan", "ayam", "sapi", "kambing", "kelinci", "kucing", "harimau")
print(hewan[-4:-1])

hewan = ("ikan", "ayam", "sapi")
if "sapi" in hewan:
  print("Yes, 'sapi' is in the hewan tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
