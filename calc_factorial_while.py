sayi = int(input("Enter a number to calculate its factorial: "))
faktorial = 1
while sayi > 0:
    faktorial = faktorial * sayi
    sayi = sayi - 1
print(faktorial)