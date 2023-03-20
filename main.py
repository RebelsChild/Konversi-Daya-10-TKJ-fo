import logic, os

while True:
    print("""                  ____      _          _        ____ _     _ _     _ 
                 |  _ \ ___| |__   ___| |___   / ___| |__ (_) | __| |
                 | |_) / _ \ '_ \ / _ \ / __| | |   | '_ \| | |/ _` |
                 |  _ <  __/ |_) |  __/ \__ \ | |___| | | | | | (_| |
Code created by  |_| \_\___|_.__/ \___|_|___/  \____|_| |_|_|_|\__,_| 
                                                   
1. Integer
2. Float""")

    pilihan = int(input("Pilih: "))
    
    os.system("clear")
    
    def tampilan():
        print("Tools konversi daya (Materi Ibu Asyah)")
        print("""
        1. Watt ke mWatt
        2. mWatt ke Watt
        3. Watt ke dBW
        4. dBW ke Watt
        5. mWatt ke dBm
        6. dBm ke mWatt
        7. dBWatt ke dBm
        8. dBm ke dBWatt
        """)
    
    if pilihan == 1:
        tampilan()
        inputan = int(input("Pilih nomor: "))
    
        if inputan == 1:
                angka = int(input("Watt (int): "))
                logic.Watt_to_mWatt(angka)
    
        elif inputan == 2:
            angka = int(input("mWatt (int): "))
            logic.mWatt_to_Watt(angka)
    
        elif inputan == 3:
            x = input("Watt: ")
            logic.Watt_to_dBW(x)
    
        elif inputan == 4:
            x = int(input("dBW: "))
            logic.dBW_to_Watt(x)
    
        elif inputan == 5:
            x = input("mWatt: ")
            logic.mWatt_to_dBm(x)
    
        elif inputan == 6:
            x = int(input("dBm: "))
            logic.dBm_to_mWatt(x)
    
        elif inputan == 7:
            x = int(input("dBW: "))
            logic.dBW_to_dBm(x)
    
        elif inputan == 8:
            x = int(input("dBm: "))
            logic.dBm_to_dBW(x)
    
        else:
            print("Keyword salah silahkank coba lagi")
    
        print("Kode berhasil di jalankan")
    
    elif pilihan == 2:
        tampilan()
        inputan = int(input("Pilih nomor: "))
    
        if inputan == 1:
            angka = float(input("Watt (float): "))
            logic.Watt_to_mWatt(angka)
    
        elif inputan == 2:
            angka = float(input("mWatt (float): "))
            logic.mWatt_to_Watt(angka)
    
        elif inputan == 3:
            x = input("Watt: ")
            logic.Watt_to_dBW(x)
    
        elif inputan == 4:
            x = float(input("dBW: "))
            logic.dBW_to_Watt(x)
    
        elif inputan == 5:
            x = input("mWatt: ")
            logic.mWatt_to_dBm(x)
    
        elif inputan == 6:
            x = float(input("dBm: "))
            logic.dBm_to_mWatt(x)
    
        elif inputan == 7:
            x = float(input("dBW: "))
            logic.dBW_to_dBm(x)
    
        elif inputan == 8:
            x = float(input("dBm: "))
            logic.dBm_to_dBW(x)
    
        else:
            print("Keyword salah silahkank coba lagi")
    
        print("Kode berhasil di jalankan")