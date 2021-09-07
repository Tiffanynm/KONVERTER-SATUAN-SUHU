print("Anyeong!")
nama = "Tiffany Naila Maharani"
NIM = 210441100026
prodi = "Sistem Informasi"
print("Nama Saya: " + nama)
print("NIM: ", NIM)
print("Prodi: " + prodi)
print("\nKONVERTER SATUAN SUHU\n")

print("----Konversi Celcius----")

celcius = float(input("Masukkan nilai suhu dalam celcius: "))
fahrenheit = (9/5) * celcius + 32
reamur = (4/5) * celcius
kelvin = celcius + 273
#Konversi Celcius
print("Nilai Celcius : ", celcius, "C")
print("Nilai dalam Fahrenheit : ", fahrenheit, "F")
print("Nilai dalam Reamur : ", reamur, "R")
print("Nilai dalam Kelvin : ", kelvin, "K")

print("\n----Konversi Fahrenheit----")

fahrenheit = float(input("Masukkan nilai suhu dalam fahrenheit: "))
celcius = (5/9) * (fahrenheit - 32)
reamur = (4/9) * (fahrenheit - 32)
kelvin = (5/9) * (fahrenheit - 32) + 273
#Konversi Fahrenheit
print("Nilai Fahrenheit : ", fahrenheit, "F")
print("Nilai dalam Celcius : ", celcius, "C")
print("Nilai dalam Reamur : ", reamur, "R")
print("Nilai dalam Kelvin : ", kelvin, "K")

print("\n----Konversi Reamur----")

reamur = float(input("Masukkan nilai suhu dalam reamur: "))
celcius = (5/4) * reamur
fahrenheit = (9/4) * reamur + 32
kelvin = (5/4) * reamur + 273
#Konversi Reamur
print("Nilai Reamur : ", reamur, "R")
print("Nilai dalam Celcius : ", celcius, "C")
print("Nilai dalam Fahrenheit : ", fahrenheit, "F")
print("Nilai dalam Kelvin : ", kelvin, "K")

print("\n----Konversi Kelvin----")

kelvin = float(input("Masukkan nilai suhu dalam kelvin: "))
celcius = kelvin - 273
fahrenheit = (9/5) * (kelvin - 273) + 32
reamur = (4/5) * (kelvin - 273)
#Konversi Kelvin
print("Nilai Kelvin : ", kelvin, "K")
print("Nilai dalam Celcius : ", celcius, "C")
print("Nilai dalam Fahrenheit : ", fahrenheit, "F")
print("Nilai dalam Reamur ; ", reamur, "R")

print("\n----TERIMA KASIH ----")
