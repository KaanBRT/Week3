sayi = int(input("Enter a number to calcuulate its cubick root: "))
hata_payi = 0.1
arttiris = 0.01
tahmin = 0
while tahmin**3 < abs(sayi) - hata_payi:
    tahmin = tahmin + arttiris
    if tahmin == abs(sayi):
        break
if sayi < 0:
    print(f"{-1*tahmin} is cubick root of {sayi}")
else:
    print(f"{tahmin} is cubick root of {sayi}")