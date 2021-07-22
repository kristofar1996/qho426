#empy set initials
set1 = set()
#initialise a non empy set
colors = {"blue", "red","black", "yellow"}
#add elements to set
set1.add("Purple")
set1.add("Green")
set1.add("Pink")
set1.add("black")
#check membership
print("red" in set1)
#union of sets
print(set1.union(colors))
#intersection
print(set1&colors)
#set difference
print(set1 - colors)
#comprehension
numbers = {a for a in range(101) if a%2 == 0}
print(numbers)
#conversion
lista = ["piotr", "ivo", "gogo","John"]
print(len(lista))
set2 = set(lista)
print(len(set2))
