import os, time
from konversi import daya

def print_screen():
        print("""
                  ____      _          _        ____ _     _ _     _
                 |  _ \ ___| |__   ___| |___   / ___| |__ (_) | __| |
                 | |_) / _ \ '_ \ / _ \ / __| | |   | '_ \| | |/ _` |
                 |  _ <  __/ |_) |  __/ \__ \ | |___| | | | | | (_| |
Code created by  |_| \_\___|_.__/ \___|_|___/  \____|_| |_|_|_|\__,_|

1. Integer
2. Float
3. Exit""")

def tampilan():
    print("Tools konversi daya (Materi kelas 10 TKJ)")
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print_screen()
    try:
        pilihan = int(input("Pilih: "))

        if pilihan == 1:
            tampilan()
            inputan = int(input("Pilih nomor: "))

            if inputan == 1:
                    angka = int(input("Watt (int): "))
                    daya.Watt_to_mWatt(angka)

            elif inputan == 2:
                angka = int(input("mWatt (int): "))
                daya.mWatt_to_Watt(angka)

            elif inputan == 3:
                x = input("Watt: ")
                daya.Watt_to_dBW(x)

            elif inputan == 4:
                x = int(input("dBW: "))
                daya.dBW_to_Watt(x)

            elif inputan == 5:
                x = input("mWatt: ")
                daya.mWatt_to_dBm(x)

            elif inputan == 6:
                x = int(input("dBm: "))
                daya.dBm_to_mWatt(x)

            elif inputan == 7:
                x = int(input("dBW: "))
                daya.dBW_to_dBm(x)

            elif inputan == 8:
                x = int(input("dBm: "))
                daya.dBm_to_dBW(x)

            else:
                print("Keyword salah silahkan coba lagi")

            continue_v = str(input("Lanjut? [Y/n]: "))
            if continue_v == "N" or continue_v == "n":
                break

            print("Kode berhasil di jalankan")

        elif pilihan == 2:
            tampilan()
            inputan = int(input("Pilih nomor: "))

            if inputan == 1:
                angka = float(input("Watt (float): "))
                daya.Watt_to_mWatt(angka)

            elif inputan == 2:
                angka = float(input("mWatt (float): "))
                daya.mWatt_to_Watt(angka)

            elif inputan == 3:
                x = input("Watt: ")
                daya.Watt_to_dBW(x)

            elif inputan == 4:
                x = float(input("dBW: "))
                daya.dBW_to_Watt(x)

            elif inputan == 5:
                x = input("mWatt: ")
                daya.mWatt_to_dBm(x)

            elif inputan == 6:
                x = float(input("dBm: "))
                daya.dBm_to_mWatt(x)

            elif inputan == 7:
                x = float(input("dBW: "))
                daya.dBW_to_dBm(x)

            elif inputan == 8:
                x = float(input("dBm: "))
                daya.dBm_to_dBW(x)

            else:
                print("Keyword salah silahkan coba lagi")

            continue_v = str(input("Lanjut? [Y/n]: "))
            if continue_v == "N" or continue_v == "n":
                break

            print("Kode berhasil di jalankan")

        elif pilihan == 3:
            break

    except ValueError:
        print("Input tidak valid silahkan ulangi")
        time.sleep(4)
        clear_screen()
        continue
