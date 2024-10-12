#PROJECT PERTAMA - KELAS TERBUKA -> REWRITE
import time
while True:
    print("Halo, ayo kita konversi suhunya")
    time.sleep(1)

    celcius = float(input("Masukan suhu dalam celcius: "))
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)

    #Celcius
    print("Suhu adalah: ", celcius, 'C')
    print("======")
    time.sleep(0.5)

    #Fahrenheit
    fahrenheit = ((9/5) * celcius) + 32 
    print('Fahrenheit: ', round(fahrenheit,1), 'F')

    #Reamur
    reamur = (4/5) * celcius
    print('Reamur: ', round(reamur,1), 'R')

    #Kelvin
    kelvin = celcius + 273.15
    print('Kelvin: ', kelvin, 'K')

    time.sleep(0.5)
    print('Udah beres nih bro..')
    time.sleep(0.5)

    ulang = input("mau konversi suhu lagi ga? (ketik 'y' untuk ya, 'n' untuk tidak): ")
    if ulang != 'y':
        print("Dadah!")
        print("Created by @yoalsb")
        break