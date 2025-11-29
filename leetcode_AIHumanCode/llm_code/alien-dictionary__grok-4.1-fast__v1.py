import collections
from collections import defaultdict

class Solution:
    def alienOrder(self, words):
        chars = set(c for w in words for c in w)
        if not chars:
            return ""
        graph = defaultdict(list)
        degree = {c: 0 for c in chars}
        for i in range(1, len(words)):
            a, b = words[i-1], words[i]
            if len(a) > len(b) and a[:len(b)] == b:
                return ""
            for k in range(min(len(a), len(b))):
                if a[k] != b[k]:
                    p, s = a[k], b[k]
                    if s not in graph[p]:
                        graph[p].append(s)
                        degree[s] += 1
                    break
        q = collections.deque(c for c in chars if degree[c] == 0)
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    q.append(v)
        return "".join(order) if len(order) == len(chars) else ""
