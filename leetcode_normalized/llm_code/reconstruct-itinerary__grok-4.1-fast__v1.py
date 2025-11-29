from collections import defaultdict

class C1:

    def findItinerary(self, a1):
        v1 = defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
        for v4 in v1.values():
            v4.sort(reverse=True)
        v5 = []
        v6 = ['JFK']
        while v6:
            v7 = v6[-1]
            if v1[v7]:
                v6.append(v1[v7].pop())
            else:
                v5.append(v6.pop())
        v5.reverse()
        return v5
