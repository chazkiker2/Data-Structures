class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edge = []

    def __str__(self):
        return f"{self.value} + edges: {[x.value for x in self.edge]}"


a = GraphNode(7)
b = GraphNode(3)
c = GraphNode(1)
d = GraphNode(6)
e = GraphNode(9)
