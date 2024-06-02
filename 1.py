'''
Задача №1

Написати програму для пошуку найкоротшого
шляху з кожної вершини до усіх інших вершин

Виконала студентка групи 31І Гриб Наталія 
'''


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u]= []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            current_vertex = None
            min_distance = float('inf')
            for vertex in self.graph:
                if vertex not in visited and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    current_vertex = vertex

            visited.add(current_vertex)
            for neighbor, weight in self.graph[current_vertex]:
                distance = distances[current_vertex] + weight
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance

        return distances

g = Graph()
g.add_edge('A', 'C', 1)
g.add_edge('A', 'B', 2)
g.add_edge('C', 'D', 2)
g.add_edge('B', 'D', 3)
g.add_edge('B', 'A', 2)
g.add_edge('C', 'F', 3)
g.add_edge('C', 'A', 1)
g.add_edge('D', 'F', 1)
g.add_edge('D', 'C', 2)
g.add_edge('D', 'B', 3)
g.add_edge('F', 'G', 1)
g.add_edge('F', 'H', 2)
g.add_edge('F', 'C', 3)
g.add_edge('F', 'D', 1)
g.add_edge('G', 'H', 2)
g.add_edge('G', 'F', 1)
g.add_edge('H', 'G', 2)
g.add_edge('H', 'F', 2)

start_vertex = 'H'
shortest_distances = g.dijkstra(start_vertex)

print('Найкоторші відстані від вершини', start_vertex)
for vertex, distance in shortest_distances.items():
    print(f'До вершини {vertex}: {distance}')
