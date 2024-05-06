class Tree():
  def __init__(self, data):
    self.data = data
    self.leftNode = None
    self.rightNode = None

def preOrderTraversal(root):
  print(root.data)
  if root.leftNode != None:
    preOrderTraversal(root.leftNode)
  if root.rightNode != None:
    preOrderTraversal(root.rightNode)

def inOrderTraversal(root):
  if root.leftNode != None:
    preOrderTraversal(root.leftNode)
  print(root.data)
  if root.rightNode != None:
    preOrderTraversal(root.rightNode)

def postOrderTraversal(root):
  if root.leftNode != None:
    preOrderTraversal(root.leftNode)
  if root.rightNode != None:
    preOrderTraversal(root.rightNode)
  print(root.data)

tree = Tree(5)
tree.leftNode = Tree(4)
tree.leftNode.leftNode = Tree(2)
tree.rightNode = Tree(8)
tree.rightNode.leftNode = Tree(7)
tree.rightNode.rightNode = Tree(9)

preOrderTraversal(tree)
print()
inOrderTraversal(tree)
print()
postOrderTraversal(tree)