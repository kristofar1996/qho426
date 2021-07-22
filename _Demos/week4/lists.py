#declare an empy  list
red = []

#declare a not empty list
amber = ["Poland", "Portugal", "Romania", "Fiji", "Amber"]
#printing a list 
print(amber)

#print a single element from list
print(amber[2])

#add elements to the end of a list
red.append("Brazil")
red.append("Somalia")

#for i in range(3):
#  red.append(input("Enter new red list counry: "))


#insert data not in the end of the list
red.insert(1, "Ghana")
print(red)
red.insert(3, "Switzerland")
print(red)


#remove an item from the list by name
#red.remove(input("Witch counrtry to remove: "))


#remove item by Index 
red.pop(0)
print(red)
new_amber_country = red.pop(1)
amber.append(new_amber_country)
print(amber)
red.pop(1)
print(red)

#delete an item
del red[0]
print(red)


#slicing
print("---Slicing---")
print(amber[2:4])



#strings in python are LISTS!!!