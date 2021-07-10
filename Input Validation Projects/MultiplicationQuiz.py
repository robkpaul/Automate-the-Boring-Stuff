import pyinputplus as pyip
import random, time

numberOfQuestions = pyip.inputNum(prompt="How many problems do you want to solve?")
numCorrect = 0

for i in range(0, numberOfQuestions):
    multiplicand1 = random.randint(0,9)
    multiplicand2 = random.randint(0,9)
    ans = multiplicand1*multiplicand2
    prompt = f"{i+1}: {multiplicand1} * {multiplicand2} ="
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (ans)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('You have to be faster!')
    except pyip.RetryLimitException:
        print('You ran out of tries.')
    else:
        print('Correct!')
        numCorrect += 1
print('Score: %s/%s' % (numCorrect, numberOfQuestions))
