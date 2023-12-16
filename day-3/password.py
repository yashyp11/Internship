import random;
print("Generate your password !")

char ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()<>,.?1234567890"
number = input('Amount of password to generate:-')
number= int(number)

length = input("Input the length of password:-")
length= int(length)

print("\n These are your passwords:-")
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print(passwords)