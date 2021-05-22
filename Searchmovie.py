class vertex:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

class graph:
    def __init__(self):
        self.dict = {}
        self.current_vertex = None

    def add_vertex(self, vertex):
        self.dict[vertex] = []
        return vertex

    def add_edge(self, from_vertex, to_vertex):
        if self.dict.get(from_vertex) is None:
            return None
        self.dict[from_vertex].append(to_vertex)
        return to_vertex

    def get_current_vertex(self):
        return self.current_vertex

    def search_graph(self, from_vertex, to_vertex):
        path_count = 0
        if from_vertex == to_vertex:
            return path_count
        nodes_list = [from_vertex]
        while len(nodes_list) > 0:
            self.current_vertex = nodes_list.pop(0)
            path_count += 1
            for node in self.dict[self.current_vertex]:
                if node == to_vertex:
                    return path_count
                nodes_list.append(node)
        return None
            
aa = vertex('A', 1)
bb = vertex('B', 2)
cc = vertex('C', 3)
dd = vertex('D', 4)
ee = vertex('E', 5)
ff = vertex('F', 6)
map = graph()
map.add_vertex(aa)
map.add_vertex(bb)
map.add_vertex(cc)
map.add_vertex(dd)
map.add_vertex(ee)
map.add_vertex(ff)
map.add_edge(aa, bb)
map.add_edge(aa, cc)
map.add_edge(aa, dd)
map.add_edge(bb, ee)
map.add_edge(cc, ff)

count = map.search_graph(aa, ff)
print(count)