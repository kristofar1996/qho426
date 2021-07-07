perfect_height = 1.5
current_height = float(input("Enter current height of grass: "))

if current_height <= perfect_height:
  print("Don't touch the grass!")
else:
  while current_height > perfect_height:
    current_height = current_height * 0.95
    print("The height of the grass is now {:.2f}".format(current_height))