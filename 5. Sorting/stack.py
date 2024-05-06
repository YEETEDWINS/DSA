import random

class Stack():
  def __init__(self, maxElements):
    self.stack = []
    self.maxElements = maxElements
  
  def push(self, element):
    if len(self.stack) < self.maxElements:
      self.stack.append(element)
      print(self.stack)
    else:
      print("no")

  def pop(self):
    if len(self.stack) == 0:
      print("you are gonna explode me")
    else:
      self.stack.pop(len(self.stack)-1)
      print(self.stack)

  def top(self):
    if len(self.stack) == 0:
      print("yes")
    else:
      print(self.stack[len(self.stack)-1])

  def getElements(self):
    if len(self.stack) == 0:
      rand = random.randint(1, 10000000)
      self.stack.append(rand)
      self.getElements()
    else:
      print(self.stack)
  
  def size(self):
    print(len(self.stack))

Stacky = Stack(4)

Stacky.push(1)
Stacky.push(2)
Stacky.push(6)
Stacky.push(6)
Stacky.push(3)
Stacky.pop()
Stacky.pop()
Stacky.pop()
Stacky.pop()
Stacky.pop()
Stacky.top()
Stacky.getElements()
Stacky.size()