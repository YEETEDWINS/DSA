class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.adjacent = [[]for i in range(nodes)]

  def DFSapp(self, temp, node, visited):
    visited[node] = True
    temp.append(node)
    for i in self.adjacent[node]:
      if visited[i] == False:
        temp = self.DFSapp(temp, i, visited)
    return temp

  def addEdge(self, node1, node2):
    self.adjacent[node1].append(node2)
    self.adjacent[node2].append(node1)
  
  def connectedComponents(self):
    visited = []
    cc = []
    for i in range(self.nodes):
      visited.append(False)
    
    for i in range(self.nodes):
      if visited[i] == False:
        temp = []
        cc.append(self.DFSapp(temp, i, visited))
    
    return cc

graph = Graph(5)

graph.addEdge(1, 0)
graph.addEdge(1, 2)
graph.addEdge(3, 4)
components = graph.connectedComponents()
print(components)