def isPrime(number):
  for i in range(2,number,1):
    if number % i == 0:
      return False
  return True

def findPrime(start, end):
  for stuff in range(start, end+1):
    if isPrime(stuff):
      return stuff


def encrypt():
  x= int(input("Provide an integer: "))
  y= int(input("Provide a secon integer (lager): "))
  p1= findPrime(x,y)
  x= int(input("Provide an integer: "))
  y= int(input("Provide a secon integer (lager): "))
  p2= findPrime(x,y)
  return p1*p2