import re
import pyperclip

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')#|\((\d{3})\) (\d{3}-\d{4})')

emailRegex = re.compile(r'\S{1,64}@\S{1,253}\.\S{1,4}')

clipboard = pyperclip.paste()

phoneNums = phoneNumRegex.findall(clipboard)
emails = emailRegex.findall(clipboard)

print(phoneNums, emails, sep="\n")