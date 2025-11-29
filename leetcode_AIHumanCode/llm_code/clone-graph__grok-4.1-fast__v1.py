class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, start):
        if not start:
            return None
        
        mapping = {}
        
        def build_copy(source):
            if source in mapping:
                return mapping[source]
            replica = UndirectedGraphNode(source.label)
            mapping[source] = replica
            for adjacent in source.neighbors:
                replica.neighbors.append(build_copy(adjacent))
            return replica
        
        return build_copy(start)
