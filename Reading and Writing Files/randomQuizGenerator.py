import random
from os import mkdir, path
from pathlib import Path
import pyinputplus as pyip

classSize = pyip.inputInt(prompt="How many tests do you need?")
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


try:
    mkdir('./quizzes')
except FileExistsError:
    print('./quizzes already exists, continuing...')

for quizNum in range(classSize):
    quizFile = open(Path('./quizzes') / ('quiz%s.txt' % str(quizNum+1)), 'w')
    quizFile.write('Name:\nDate:\nPeriod:\n\n' + (' '*20) + f'State Capitals Quiz (Form{quizNum+1})\n\n')
    
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f'{questionNum}. What is the Capital of {states[questionNum]}\n' +
            " "*5 + f'a. {answerOptions[0]}\n' + 
            " "*5 + f'b. {answerOptions[1]}\n' + 
            " "*5 + f'c. {answerOptions[2]}\n' + 
            " "*5 + f'd. {answerOptions[3]}\n')
    quizFile.close()

