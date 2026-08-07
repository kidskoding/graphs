class GraphNode[T]:
    def __init__(self, val: T):
        self.val = val
        self.neighbors: list[T] = []
