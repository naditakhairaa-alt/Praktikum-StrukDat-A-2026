class Person:
  def __init__(self, nama, jenisKelamin, umur):
    self.nama = nama
    self.jenisaKelamin = jenisKelamin
    self.umur = umur

class Karyawan(Person):
  def __init__(self, nama, jenisKelamin, umur, gaji):
    super().__init__(nama, jenisKelamin, umur)
    self._gaji = gaji #protected property

  def get_gaji(self):
    return self._gaji
  
  def set_gaji(self, gajiBaru):
    self._gaji = gajiBaru

class Rekening():
  def __init__(self, noRekening, pin):
    self.noRekening = noRekening
    self.__pin = pin

  def get_pin(self):
    return self.__pin
  
  def set_pin(self, pin):
    if pin > 6:
      self.__pin = pin
    else:
      print("Pin harus di memiliki minimal 6 angka")

p1 = Karyawan("Nadit", "Female", 19, 88000000)
r1 = Rekening("87668", "8888")

print(r1.get_pin())
print(p1.nama)
print(p1.get_gaji())