def Watt_to_mWatt(angka1:int):
    x = angka1 * 1000
    print(f"""p(mWatt) = p(Watt) x 1000
         = {angka1} x 1000
         = {x} mWatt
    """)

def Watt_to_mWatt1(angka1:float):
    x = angka1 * 1000
    print(f"""p(mWatt) = p(Watt) x 1000
         = {angka1} x 1000
         = {x} mWatt
    """)

def mWatt_to_Watt(angka1:int):
    x = angka1 / 1000
    print(f"""p(Watt) = p(mWatt) : 1000
         = {angka1} : 1000
         = {x} Watt
    """)

def mWatt_to_Watt1(angka1:float):
    x = angka1 * 1000
    print(f"""p(mWatt) = p(Watt) x 1000
         = {angka1} x 1000
         = {x} mWatt
    """)

def Watt_to_dBW(angka1):
    string_number = str(angka1)
    result = "".join(filter(lambda x: x == '0', string_number[string_number.index(angka1[0])+1:]))
    x = len(result)
    y = 10 * x
    print(f"""p(dBWatt) = 10 log p(Watt)
          = 10 log {angka1}
          = 10 x {x}
          = {y} dBWatt
    """)

def dBW_to_Watt(angka1):
    x = angka1 / 10
    y = 10 ** x
    print(f"""p(Watt) = 10^ (p(dBWatt / 10))
        = 10^({angka1}:10)
        = 10^{x}
        = {y} Watt
    """)

def mWatt_to_dBm(angka1):
    string_number = str(angka1)
    result = "".join(filter(lambda x: x == '0', string_number[string_number.index(angka1[0])+1:]))
    x = len(result)
    y = 10 * x
    print(f"""p(dBWatt) = 10 log p(Watt)
          = 10 log {angka1}
          = 10 x {x}
          = {y} dBWatt
    """)

def dBm_to_mWatt(angka1):
    x = angka1 / 10
    y = 10 ** x
    print(f"""p(Watt) = 10^ (p(dBWatt / 10))
        = 10^({angka1}:10)
        = 10^{x}
        = {y} Watt
    """)

def dBW_to_dBm(angka1):
    x = angka1 + 30
    print(f"""p(dBm) = p(dBWatt) + 30
       = {angka1} + 30
       = {x} dBm
    """)

def dBm_to_dBW(angka1):
    x = angka1 - 30
    print(f"""p(dBWatt) = p(dBm) - 30
       = {angka1} - 30
       = {x} dBWatt
    """)