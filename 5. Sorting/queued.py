import os

os.system('clear')

class Queue:
  def __init__(self, length):
    self.length = length
    self.front = 0
    self.rear = 0
    self.queue = [None]*length
    
  def enQueue(self, arg):
    if self.length == 0:
      print("no availability")
    else:
      self.queue[self.rear] = arg
      self.rear += 1
      self.length -= 1

  def deQueue(self):
    if len(self.queue) == 0:
      print("no")
    else:
      self.queue[self.front] = None
      self.length+= 1
      self.rear-= 1
  
  def peak(self):
    print(self.queue[self.front])
  
  def tail(self):
    print(self.queue[self.rear-1])

  def everything(self):
    print(self.queue)

  def increase(self, num):
    self.queue.extend([None]*num) # Extend pretty much adds the given elements. Like a plus
    self.length += num

size = input("Give me a maximum length:\n>")
Queued = Queue(int(size))

while True:
  function = input("choose a function:\n>")
  value = function.split(" ")
  # print(value[0])
  # print(value[1])
  if value[0] == "insert":
    Queued.enQueue(value[1])
  elif value[0] == "remove":
    Queued.deQueue()
  elif value[0] == "peak":
    Queued.peak()
  elif value[0] == "tail":
    Queued.tail()
  elif value[0] == "list":
    Queued.everything()
  elif value[0] == "increase":
    Queued.increase(int(value[1]))