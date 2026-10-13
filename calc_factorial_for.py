sayi = int(input("Enter a number to calculate its factorial: "))
faktorial = 1
for x in range(1, sayi + 1):
    faktorial = faktorial * x
print(faktorial)