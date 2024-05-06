import random

class Bottle: # parent class or base class
  def __init__(self, brand, size, material, shape, typ):
    self.brand = brand
    self.size = size
    self.material = material
    self.shape = shape
    self.typ = typ

  # A getter function returns the value of a property
  def getSize(self):
    print("The size of this bottle is "+str(self.size))

  # A setter function sets/changes the value of a property
  def setSize(self, size):
    print("The size has been configured to "+str(size))
    self.size = size

  def setType(self):
    types = input("Choose a type of Bottle:\n1. Normal (Cap)\n2. No Cap\n3. Thermal\n4. Jug\n5. One time use\n> ")
    if types == "1":
      self.typ = "Cap"
    if types == "2":
      self.typ = "No Cap"
    if types == "3":
      self.typ = "Thermal"
    if types == "4":
      self.typ = "Jug"
    if types == "5":
      self.typ = "One Use"
    print("The bottle's type has been changed to "+self.typ)


class Dopper(Bottle): # Child Class, or Subclass
  def __init__(self, brand, size, material, shape, typ, capColor, bodyColor):
    Bottle.__init__(self, brand, size, material, shape, typ)
    self.capColor = capColor
    self.bodyColor = bodyColor

  def randomColor(self):
    cColor = random.randrange(0, 2**24)
    cValue = hex(cColor)
    bColor = random.randrange(0, 2**24)
    bValue = hex(bColor)
    self.capColor = cValue
    self.bodyColor = bValue
    print("The cap color is: #"+cValue+"\nThe body color is: #"+bValue)

c = Dopper("Dopper", 200, "plastic", "Cylinder", None, None, None)
c.randomColor()

bottle = Bottle("Nike", 10, "glass", "Organic", None)
bottle.getSize()
bottle.setSize(100)
bottle.setType()

