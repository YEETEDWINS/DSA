class Graph:
  def __init__(self, values):
    self.node = values
    self.adjacent = [[]*values for i in range(values)]

  def edgeCreation(self, x, y):
    self.adjacent[x-1].append(y-1)
    self.adjacent[y-1].append(x-1)

  def BFS(self, start):
    visited = [False]*self.node
    empty = []
    queue = []
    visited[start] = True
    while len(queue) > 0:
      temp = queue.pop(0)
      empty.append(temp)
      for i in self.adjacent[temp]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True
    return empty

graph1 = Graph(5)
graph1.edgeCreation(3, 4)
graph1.edgeCreation(1, 5)
graph1.edgeCreation(4, 5)
graph1.edgeCreation(1, 2)

print(graph1.BFS(0))