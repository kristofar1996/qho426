print("Program Started!")
print("Please enter an ASCII code:")
a = abs(int(input()))
if a in range (32,127):
  print("The character represented by the ASCII code {} is {}.".format(a, chr(a)))
else:
  print("This is an error")
print("Program ended")
