import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})|\((\d{3})\) (\d{3}-\d{4})')

response = input("What\'s your phone number?")

print(phoneNumRegex.search(response).groups()) 