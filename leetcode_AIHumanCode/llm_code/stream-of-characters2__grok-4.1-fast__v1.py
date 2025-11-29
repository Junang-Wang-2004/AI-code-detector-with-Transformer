from collections import deque

class StreamChecker:
    def __init__(self, words):
        self.graph = [{'go': {}, 'link': 0, 'end': False}]
        nxt = 1
        for w in words:
            u = 0
            for c in w:
                if c not in self.graph[u]['go']:
                    self.graph[u]['go'][c] = nxt
                    self.graph.append({'go': {}, 'link': 0, 'end': False})
                    nxt += 1
                u = self.graph[u]['go'][c]
            self.graph[u]['end'] = True
        q = deque()
        for c, v in self.graph[0]['go'].items():
            self.graph[v]['link'] = 0
            q.append(v)
        while q:
            u = q.popleft()
            for c, v in self.graph[u]['go'].items():
                q.append(v)
                f = self.graph[u]['link']
                while f and c not in self.graph[f]['go']:
                    f = self.graph[f]['link']
                g = self.graph[f]['go'].get(c, 0)
                self.graph[v]['link'] = g
                self.graph[v]['end'] |= self.graph[g]['end']
        self.pos = 0

    def query(self, c):
        u = self.pos
        while u and c not in self.graph[u]['go']:
            u = self.graph[u]['link']
        v = self.graph[u]['go'].get(c, 0)
        self.pos = v
        return self.graph[v]['end']
