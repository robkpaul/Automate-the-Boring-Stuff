import re

regexes = {re.compile(r'\S{8,}'), re.compile(r'[a-z]+'), re.compile(r'[A-Z]+'), re.compile(r'\d+')}

password = input("Enter a Password: ")

passing = True
for reg in regexes:
    if passing:
        passing = bool(re.search(reg, password))
    else:
        break
if passing:
    print("Valid")
else:
    print("Invalid")