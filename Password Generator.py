import random

print("Welcome to the Password Generator!")
while True:
    try:
        characterAmount = int(input("Enter the character amount: ").strip())
        if characterAmount <= 0:
            print("Try again: Enter a positive number.")
            continue
        break
    except ValueError:
        print("Try again: Please enter a valid number.")

while True:
    numbersCheck = input("Include numbers? (y/n): ").strip().lower()
    if numbersCheck in ['y', 'n']:
        break
    else:
        print("Try again: Please enter 'y' or 'n'.")

while True:
    symbolsCheck = input("Include symbols? (y/n): ").strip().lower()
    if symbolsCheck in ['y', 'n']:
        break
    else:
        print("Try again: Please enter 'y' or 'n'.")

if numbersCheck not in ['y', 'n'] or symbolsCheck not in ['y', 'n']:
    print("Invalid input for numbers or symbols. Please enter 'y' or 'n'.")
    exit()

password = []

for i in range(characterAmount):
    if numbersCheck == 'y' and symbolsCheck == 'y':
        password.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'))
    elif numbersCheck == 'y':
        password.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
    elif symbolsCheck == 'y':
        password.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'))
    else:
        password.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))

finalPassword = ''.join(password)
print(f"Your generated password is: {finalPassword}")