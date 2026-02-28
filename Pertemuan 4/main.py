import kurs
import konverter 
import tabulate

#tampilan tabel
print("=== KONVERTER MATA UANG ===")

data = []
for k, v in kurs.kurs.items():
    data.append([k, f"{v:.0f}" .replace(",", ".")])

print(tabulate.tabulate(data, headers=["Kode", "Kurs"], tablefmt="pretty"))

#input user
mata_uang_awal = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
hasil_konversi = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input ("Jumlah: "))

#ubah ke IDR
jumlah_IDR = 0
if mata_uang_awal.upper() == "USD":
    jumlah_IDR = konverter.USD_ke_IDR(jumlah)
elif mata_uang_awal.upper() == "EUR":
    jumlah_IDR = konverter.EUR_ke_IDR(jumlah)
elif mata_uang_awal.upper() == "SGD":
    jumlah_IDR = konverter.SGD_ke_IDR(jumlah)
elif mata_uang_awal.upper() == "JPY":
    jumlah_IDR = konverter.JPY_ke_IDR(jumlah)
elif mata_uang_awal.upper() == "IDR" :
    jumlah_IDR = jumlah
else:
    print("Mata uang tidak ditemukan!")


#ubah ke mata uang asing
jumlah_konversi = 0
if hasil_konversi.upper() == "USD":
    jumlah_konversi = konverter.IDR_ke_USD(jumlah)
elif hasil_konversi.upper() == "EUR":
    jumlah_konversi = konverter.IDR_ke_EUR(jumlah)
elif hasil_konversi.upper() == "SGD":
    jumlah_konversi = konverter.IDR_ke_SGD(jumlah)
elif hasil_konversi.upper() == "JPY":
    jumlah_konversi = konverter.IDR_ke_JPY(jumlah)
elif hasil_konversi.upper() == "IDR" :
    jumlah_konversi = jumlah_IDR
else :
    print("Mata uang tidak ditemukan!")

#tampilan output
if jumlah_IDR != 0 and jumlah_konversi != 0:
    if mata_uang_awal == "IDR":
        print (f"Rp {jumlah:,.0f}" .replace(",", ".") + f" = {jumlah_konversi:.2f} {hasil_konversi}")
    elif hasil_konversi == "IDR":
        print (f"{jumlah:.2f} {mata_uang_awal}" + f" = Rp {jumlah_konversi:,.0f}".replace(",", "."))
    else:
        print(f"{jumlah:.2f} {mata_uang_awal} = {jumlah_konversi:.2f} {hasil_konversi}")