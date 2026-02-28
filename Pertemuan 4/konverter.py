#file konverter.py yang berisi fungsi konversi mata uang

import kurs
#dari mata uang asing ke IDR
def USD_ke_IDR(jumlah_awal):
    jumlah_akhir = jumlah_awal * kurs.kurs["USD"]
    return jumlah_akhir

def EUR_ke_IDR(jumlah_awal):
    jumlah_akhir = jumlah_awal * kurs.kurs["EUR"]
    return jumlah_akhir

def SGD_ke_IDR(jumlah_awal):
    jumlah_akhir = jumlah_awal * kurs.kurs["SGD"]
    return jumlah_akhir

def JPY_ke_IDR(jumlah_awal):
    jumlah_akhir = jumlah_awal * kurs.kurs["JPY"]
    return jumlah_akhir

#ubah IDR ke mata uang asing
def IDR_ke_USD(jumlah_awal):
    jumlah_akhir = jumlah_awal / kurs.kurs["USD"]
    return jumlah_akhir

def IDR_ke_EUR(jumlah_awal):
    jumlah_akhir = jumlah_awal / kurs.kurs["EUR"]
    return jumlah_akhir

def IDR_ke_SGD(jumlah_awal):
    jumlah_akhir = jumlah_awal / kurs.kurs["SGD"]
    return jumlah_akhir

def IDR_ke_JPY(jumlah_awal):
    jumlah_akhir = jumlah_awal / kurs.kurs["JPY"]
    return jumlah_akhir