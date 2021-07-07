
while True:
  print("Please choose an option\n\n1-Nice message\n2-Area of a rectangle\n3-Area of triangle\n4-Multiplication message")

  option = int(input())

  if option == 1:
    print("We are happy to meet you!")
  elif option == 2:
    l = float(input("Enter the lenght of the rectange: "))
    w = float(input("Enter the height of the rectangle: "))
    print("Area of this rectangle is {:.2f}" .format(l*w))
  elif option == 3:
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    print("Area of this triangle is {:.2f}" .format(b*h/2))
  elif option == 4:
    n = int(input("Enter the number: "))
    counter = 1

    n2 = int(input("Enter the limit of table: "))

    while counter <= n2:
      print(f"{n}x{counter} = {counter*n} ")
      counter +=1
  elif option ==0:
      break 
  else:
    print("Go to specsavers!")

  