def room_area(width, lenght):
  return width*lenght

def room_name():
  return input("What is the name of the room?\n")

def price(name, area, ):
  if name == "bathrooom":
    return 20*area
  elif name == "bedroom":
    return 10*area
  elif name == "kitchen":
    return 5*area
  else:
    return 30*area

def run():
  name = room_name()
  w = float(input("What is the width of the room?"))
  l = float(input("What is the lenght of the room?"))
  print("To paint {}  you need to pay £{:.2f}".format(name, price(name, room_area(w,l))))

run()