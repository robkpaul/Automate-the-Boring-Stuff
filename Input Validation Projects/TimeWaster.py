import pyinputplus as pyip

response = 'yes'
while response.lower() == 'yes':
    response = pyip.inputYesNo(prompt='Do you want to know how to waste an idiot\'s time?')
print("That's too bad...")