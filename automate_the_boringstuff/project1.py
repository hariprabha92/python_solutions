 #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

import random
def quiz():
   # The quiz data. Keys are states and values are their capitals
  capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 
  'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   # Generate 35 quiz files.
  for quizNum in range(35):
    quizfile=open('questinon_file_%d.txt'%(quizNum+1),'w')
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    answerfile=open('answer_file_%d.txt'%(quizNum+1),'w')
    states = list(capitals.keys())
    random.shuffle(states)
    for i in range(50):
      quizfile.write('\n%d. What is the capital of %s?\n' % (i+1,states[i]))
      answer=capitals[states[i]]
      ans=capitals.values()
      ans.remove(answer)
      options=[]
      options=random.sample(ans,3)
      options=[answer]+options
      random.shuffle(options)
      for j in range(4):
        quizfile.write(' %s. %s\n' % ('ABCD'[j], options[j]))
        quizfile.write('\n')
      answerfile.write('%s. %s\n' % (i + 1, 'ABCD'[options.index(answer)]))
  quizfile.close()
  answerfile.close()      
quiz()





