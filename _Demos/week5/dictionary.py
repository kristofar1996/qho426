#dictionary empy
phonebook = {}
#non empty dictionary
d = {"name":"Kris", "age":"25", "doggo":False}
#Search in a dictionary
print(d["name"])
#populate dictionary (add to it)
phonebook["ivo"] = 342442
phonebook["Nasko"]= 342
phonebook["Koki"]= 43254
print(phonebook)
#populating dictionary more effisent and easy
for i in range (5):
  phonebook[input("Enter name:")]= input("Enter the number: ")

print(phonebook)
#accessing by value
for i in d.values():
  if i:
    print("dog!")
  else:
    print("No Dog!")