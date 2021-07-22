def students_marks():
  name = input("Enter students name: ")
  mark = float(input(f"Enter the mark for {name} :"))
  return name, mark 


#unpack tuple

x, y = students_marks()
print(x)
print(y)
y = y + 10
t = x,y
print(t)