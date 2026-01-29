#creating variabels
x = 5
y = "Kun"
print(x)
print(y)

z = 4       # z bertipe int
z = "Karina" # z sekarang berganti menjadi tipe str
print(z)

#casting
a = str(8)    # a akan menjadi '8'
b = int(9)    # b akan menjadi 9
c = float(10)  # c akan menjadi 10.0

#mendapatkan tipenya
m = 7
n = "Kevin"
print(type(m))
print(type(n))

#single atau double quotes?
o = "Martin"
# sama saja seperti
o = 'Martin'

#case-sensitive
q = 9
Q = "Winter"
#Q tidak akan menimpa q

#VARIABLES NAMES
myvar = "Jake"
my_var = "Jake"
_my_var = "Jay"
myVar = "Jay"
MYVAR = "Evan"
myvar2 = "Evan"

#nama variabel lebih dari satu kata
#camel case
myVariableName = "Sean"

#pascal case
MyVariableName = "Sean"

#snake case
my_variable_name = "Sean"

#MENETAPKAN BEBERAPA NILAI
#banyak nilai untuk banyak variabel
d, e, f = "Justin", "Kenny", "James"
print(d)
print(e)
print(f)

#satu nilai untuk beberapa variabel
h = i = j = "Seventeen"
print(h)
print(i)
print(j)

#output variables
p = "Always be there"
print(p)

r = "She"
s = "is"
t = "supercalifragilisticexpialidocious"
print(r, s, t)

u = "He "
v = "is "
w = "incredible"
print(u + v + w)

k =9
l = 1
print(k + l)

ab = 5
cd = "Carmen"
print(ab, cd)

#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "greatl"

def myfunc():
  x = "cool"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#the global keyword
def myfunc():
  global x
  x = "incredible"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "good"

myfunc()

print("Python is " + x)
