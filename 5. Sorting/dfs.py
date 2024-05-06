class Graph:
  def __init__(self):
    self.graph = {}

  def edgeCreation(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)

  def DFS(self, start):
    visited = set()
    stack = [start]
    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        if vertex in self.graph:
          stack.extend(reversed(self.graph[vertex]))

g = Graph()
g.edgeCreation("1", "2")
g.edgeCreation("3", "2")
g.edgeCreation("6", "3")
g.edgeCreation("5", "3")
g.edgeCreation("5", "6")

g.DFS("3")