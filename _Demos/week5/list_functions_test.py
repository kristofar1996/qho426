#Program that shows a list with students and is able to add and delete students from it 
#the program can calculate average max


def generate_sts():
  name = input("What is the name?\n")
  grade = input("What is the grade?\n")
  dog = input("Does this student have a dogo?(type yes or No\n")
  if dog.upper() == "yes" :
    dog = True
  else:
    dog = False
  return name,grade,dog




def all_sts():
  database = []
  while True:
    database.append(generate_sts())
    x= input("TO stop, type 0. Otherwise Type anything\n")
    if x == '0':
      break
  return database 

def remove(lista = []):
  to_remove = input("Type the name of student to be removed:\n")
  for tuplex in lista:
    if tuplex[0] == to_remove:
      lista.remove(tuplex)
      break
  
  return lista

def print_sts(lista):
  for tuplex in lista:
    print(tuplex [0], "earned", tuplex[1], "grade this semester!")


def keep_sts(lista = [], mark = 100):
  for tuplex in lista:
    if tuplex[1] < mark:
      lista.remove(tuplex)
  return lista

    


def average(lista = []):
  suma = 0
  for tuplex in lista:
    suma = suma + tuplex[1]
  return suma/len(lista)
  

def run():
  dtbs = all_sts()
  while true:
    print("Choose one of the following options:\n1-Retrieve all students\n2-Calculate the average\n3-Remove a student\n4-Remove all student below a grade\n")
    opt = int(input())
    if opt == 1:
      print_sts(dtbs)
    elif opt == 2:
      print(f"The average mark of all students is{average(dtbs):.2f})
    elif opt == 3:
      remove(dtbs)
    elif opt == 4:
      dtbs = keep_sts(dtbs, int(input("What is the benchmark(0-100):")))
    elif opt == 5:
      print("Good bye - I will miss you!")
      break
    else:
    print("Giving spacesavers mate, no such option exist")

run()
