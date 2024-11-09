while True:

    print("""
\n---PILIH PROGRAM---
   1. Penjumlahan
   2. Pengurangan
   3. Perkalian
   4. Pembagian""")
    list_soal=input("Masukan pilihan program (1-4) : ")

    if list_soal=='1':
        print("\n~ANDA PILIH PENJUMLAHAN~")
        angka1=float(input("Masukan angka pertama : "))
        angka2=float(input("Masukan angka kedua   : "))
        angka3=float(input("Masukan angka ketiga  : "))
        angka4=float(input("Masukan angka keempat : "))
        angka5=float(input("Masukan angka kelima  : "))
        hasil=angka1+angka2+angka3+angka4+angka5
        print(f"total hasil {hasil}")
    
    elif list_soal=='2':
        print("\n~ANDA PILIH PENGURANGAN~")
        angka1=float(input("Masukan angka pertama : "))
        angka2=float(input("Masukan angka kedua   : "))
        angka3=float(input("Masukan angka ketiga  : "))
        angka4=float(input("Masukan angka keempat : "))
        angka5=float(input("Masukan angka kelima  : "))
        hasil=angka1-angka2-angka3-angka4-angka5
        print(f"total hasil {hasil}")
    
    elif list_soal=='3':
        print("\n~ANDA PILIH PERKALIAN~")
        angka1=float(input("Masukan angka pertama : "))
        angka2=float(input("Masukan angka kedua   : "))
        angka3=float(input("Masukan angka ketiga  : "))
        angka4=float(input("Masukan angka keempat : "))
        angka5=float(input("Masukan angka kelima  : "))
        hasil=angka1*angka2*angka3*angka4*angka5
        print(f"total hasil {hasil}")
    
    elif list_soal=='4':
        print("\n~ANDA PILIH PEMBAGIAN~")
        angka1=float(input("Masukan angka pertama : "))
        angka2=float(input("Masukan angka kedua   : "))
        angka3=float(input("Masukan angka ketiga  : "))
        angka4=float(input("Masukan angka keempat : "))
        angka5=float(input("Masukan angka kelima  : "))
        hasil=angka1/angka2/angka3/angka4/angka5
        print(f"total hasil {hasil}")
        
    else:
        print("data tidak valid")
        
    list_soal=input("lanjut berhitung (y/n)")
    if list_soal=='n':
        break