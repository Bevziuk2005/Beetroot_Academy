"""
            Task
"""
from typing import Dict, Optional, Tuple

class Vertex:

    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict["Vertex", int] = {}

    def add_neighbor(self, nbr, weight=0) -> None:
        self.connected_to[nbr] = weight

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.connected_to]}"

    def get_connections(self):
        return tuple(self.connected_to.keys())

    def get_id(self) -> int:
        return self._id

class Graph:

    def __init__(self) -> None:
        self.vertices_dict: Dict[int, Vertex] = {}
        self.num_vertices: int = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n: int) -> Optional[Vertex]:
        if n in self.vertices_dict:
            return self.vertices_dict[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices_dict

    def add_edge(self, f, t, weight=0) -> None:
        if f not in self.vertices_dict:
            self.add_vertex(f)
        if t not in self.vertices_dict:
            self.add_vertex(t)
        self.vertices_dict[f].add_neighbor(self.vertices_dict[t], weight)

    def get_vertices(self) -> tuple:
        return tuple(self.vertices_dict.keys())

    def all_vertices_for_dfs(self, start=None, visited=None):
        if self.num_vertices == 0:
            return "In graph no vertices"
        if visited is None:
            visited = set()
        if start is None:
            start = next(iter(self.vertices_dict.values()))
        visited.add(start)
        for i in start.get_connections():
            if i not in visited:
                self.all_vertices_for_dfs(i, visited)
        return bool(len(visited) == self.num_vertices)
"""
    def alg_deicstra(self, start, end):
        distance = []
        for i in range(self.num_vertices-1):
            distance.append(None)
        distance[start] = 0

        no_visited = self.vertices_dict.values()
        while no_visited:
            min_item = int(min(no_visited, distance[]))

    def __iter__(self):
        return iter(self.vertices_dict.values())
"""

if __name__ == "__main__":
    g = Graph()
    for i in range(8):
        g.add_vertex(i)

    g.add_edge(0, 1, 4)
    g.add_edge(1, 0, 4)

    g.add_edge(0, 7, 8)
    g.add_edge(7, 0, 8)

    g.add_edge(1, 2, 8)
    g.add_edge(2, 1, 8)

    g.add_edge(1, 7, 11)
    g.add_edge(7, 1, 11)

    g.add_edge(7, 6, 1)
    g.add_edge(6, 7, 1)

    g.add_edge(7, 8, 7)
    g.add_edge(8, 7, 7)

    g.add_edge(2, 3, 7)
    g.add_edge(3, 2, 7)

    g.add_edge(2, 5, 4)
    g.add_edge(5, 2, 4)

    g.add_edge(2, 8, 2)
    g.add_edge(8, 2, 2)

    g.add_edge(8, 6, 6)
    g.add_edge(6, 8, 6)

    g.add_edge(6, 5, 2)
    g.add_edge(5, 6, 2)

    g.add_edge(3, 4, 9)
    g.add_edge(4, 3, 9)

    g.add_edge(3, 5, 14)
    g.add_edge(5, 3, 14)

    g.add_edge(5, 4, 10)
    g.add_edge(4, 5, 10)

    print("Зв'язність: ", g.all_vertices_for_dfs())
    print("0 -> 2: ", g.alg_deicstra(0, 2))
    print("0 -> 4: ", g.alg_deicstra(0, 4))

"""
    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
"""