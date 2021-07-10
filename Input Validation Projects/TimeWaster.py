import pyinputplus as pyip

def isYesOrNo(arg):
    if(arg.lower() == 'yes' or arg.lower() == 'no'):
        return arg
    else:
        raise Exception('Please answer yes or no, not \'%s\'.' %(arg))

response = 'yes'
while response.lower() == 'yes':
    response = pyip.inputCustom(isYesOrNo, prompt="Do you wanna know how to waste an idiot's time?\n")
print("That's too bad...")