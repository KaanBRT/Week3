given_number = int(input("Enter a number tpo calculate square root: "))

if given_number < 0:
    print(f"Square root of negative numbers is not a real number. Did you want to say {-1*given_number}? ")
    cevap = input("Yes or No: ")
    if cevap == "Yes":
        given_number = -1* given_number
        for guess_number in range (1,given_number):
            if guess_number**2 == given_number:
             print (f"{guess_number} is square root of {given_number}")
            break
    else:
        for guess_number in range (1,given_number):
            print("booooooooooooooooo")
        if guess_number**2 != given_number:
            print("booooo")

for guess_number in range (1,given_number):
    if guess_number**2 == given_number:
        print (f"{guess_number} is square root of {given_number}")
        break
if guess_number**2 != given_number:
    print("booooo")



    