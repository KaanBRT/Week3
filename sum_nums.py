sayi = int(input("Enter a number: "))
toplam = 0
formula = sayi * (sayi + 1) / 2
while sayi > 0:
    toplam = toplam + sayi
    sayi = sayi - 1
print(toplam)
print(formula)
if toplam == formula:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")
