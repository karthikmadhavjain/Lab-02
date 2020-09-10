#Author: kmj5614@psu.edu Karthik Madhav Jain
#Collaborator:mmm7378@psu.edu Marquis Mcmillan
#Collaborator:drr5348@psu.edu Daniela Rigazio
#Collaborator:ckv5108@psu.edu Chinmay Vibhute
#Section:003
#Breakout room number:

def getLettergrade(grade):
  global letter_grade
  if float(grade) >= 93.00:
    letter_grade = 'A'
  elif float(grade) >= 90.00:
    letter_grade = 'A-'
  elif float(grade) >= 87.00:
    letter_grade = 'B+'
  elif float(grade) >= 83.00:
    letter_grade = 'B'
  elif float(grade) >= 80.00:
    letter_grade = 'B-'
  elif float(grade) >= 77.00:
    letter_grade = 'C+'
  elif float(grade) >= 70.00:
    letter_grade = 'C'
  elif float(grade) >= 60.00:
    letter_grade = 'D'
  elif float(grade) < 60.00:
    letter_grade = 'F'
  return letter_grade

def run():
  grade = input('Enter your CMPSC 131 grade: ')
  getLettergrade(grade)
  print(f"Your letter grade for CMPSC 131 is {letter_grade}.")

if __name__=="__main__":
  run()
