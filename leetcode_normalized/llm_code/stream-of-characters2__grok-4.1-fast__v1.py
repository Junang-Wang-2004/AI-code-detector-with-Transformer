from collections import deque

class C1:

    def __init__(self, a1):
        self.graph = [{'go': {}, 'link': 0, 'end': False}]
        v1 = 1
        for v2 in a1:
            v3 = 0
            for v4 in v2:
                if v4 not in self.graph[v3]['go']:
                    self.graph[v3]['go'][v4] = v1
                    self.graph.append({'go': {}, 'link': 0, 'end': False})
                    v1 += 1
                v3 = self.graph[v3]['go'][v4]
            self.graph[v3]['end'] = True
        v5 = deque()
        for v4, v6 in self.graph[0]['go'].items():
            self.graph[v6]['link'] = 0
            v5.append(v6)
        while v5:
            v3 = v5.popleft()
            for v4, v6 in self.graph[v3]['go'].items():
                v5.append(v6)
                v7 = self.graph[v3]['link']
                while v7 and v4 not in self.graph[v7]['go']:
                    v7 = self.graph[v7]['link']
                v8 = self.graph[v7]['go'].get(v4, 0)
                self.graph[v6]['link'] = v8
                self.graph[v6]['end'] |= self.graph[v8]['end']
        self.pos = 0

    def query(self, a1):
        v1 = self.pos
        while v1 and a1 not in self.graph[v1]['go']:
            v1 = self.graph[v1]['link']
        v2 = self.graph[v1]['go'].get(a1, 0)
        self.pos = v2
        return self.graph[v2]['end']
