class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda t: t[2])
        informed = {0, firstPerson}
        idx = 0
        total = len(meetings)
        while idx < total:
            curr_t = meetings[idx][2]
            edges = []
            attendees = set()
            while idx < total and meetings[idx][2] == curr_t:
                p1, p2, _ = meetings[idx]
                edges.append((p1, p2))
                attendees.add(p1)
                attendees.add(p2)
                idx += 1
            if not attendees:
                continue
            finder = UF(n)
            for p1, p2 in edges:
                finder.unite(p1, p2)
            inf_roots = {finder.find(p) for p in attendees if p in informed}
            for p in attendees:
                if finder.find(p) in inf_roots:
                    informed.add(p)
        return sorted(informed)
