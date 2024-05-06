import math
state = True
root = None

class Tree():
  def __init__(self, data):
    self.data = data
    self.leftNode = None
    self.rightNode = None

def inOrderTraversal(root):
  if root.leftNode != None:
    inOrderTraversal(root.leftNode)
  print(root.data)
  if root.rightNode != None:
    inOrderTraversal(root.rightNode)

def Insert(root, k):
  if root != None:
    if k > root.data:
      root.rightNode = Insert(root.rightNode, k)
    elif k < root.date:
      root.leftNode = Insert(root.leftNode, k)
  else:
    return Tree(k)
  return root

def Search(root, k):
  if k > root.data and root.rightNode != None:
    return Search(root.rightNode, k)
  elif k < root.data and root.leftNode != None:
    return Search(root.leftNode, k)
  elif k == root.data:
    return root
  else:
    return -1
  
def Delete(root, k):
  if root == None:
    return root
  if k < root.data:
    root.leftNode = Delete(root.leftNode, k)
  elif k > root.data:
    root.rightNode = Delete(root.rightNode, k)
  else:
    if root.leftNode == None:
      temp = root.rightNode
      root = None
      return temp
    elif root.rightNode == None:
      temp = root.leftNode
      root = None
      return temp
    else:
      temp = Find(root)
      v = root.data
      root.data = temp.data
      temp.data = v
      root.rightNode = Delete(root.rightNode, temp.data)

def Find(root):
  current = root
  while current.leftNode != None:
    current = current.leftNode
    return current

i = 1
while state:

  value = input("What is value number "+str(i)+"\n> ")
  if value == "n":
    break
  elif not math.isnan(int(value)):
    Insert(root, value)
    i+=1
  else:
    continue
