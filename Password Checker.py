password = input("Type in password: ").strip()

score = 0
lengthBoolean = False
containsUppercase = False
containsLowercase = False
containsNumbers = False
containsSymbols = False

if len(password) >= 8:
    lengthBoolean = True
    score += 1
if any(char.isupper() for char in password):
    containsUppercase = True
    score += 1
if any(char.islower() for char in password):
    containsLowercase = True
    score += 1
if any(char.isdigit() for char in password):
    containsNumbers = True
    score += 1
if any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
    containsSymbols = True
    score += 1

print("Strength Meter:", "★ " * score + "☆ " * (5 - score))
print(f"✔ Length >= 8: {lengthBoolean}")
print(f"✔ Contains uppercase: {containsUppercase}")
print(f"✔ Contains lowercase: {containsLowercase}")
print(f"✔ Contains numbers: {containsNumbers}")
print(f"✔ Contains symbols: {containsSymbols}")