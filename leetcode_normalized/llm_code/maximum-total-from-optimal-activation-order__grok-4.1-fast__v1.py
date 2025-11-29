from collections import defaultdict

class C1:

    def maxTotal(self, a1, a2):
        v1 = defaultdict(list)
        for v2 in range(len(a1)):
            v1[a2[v2]].append(a1[v2])
        v3 = 0
        for v4, v5 in v1.items():
            v5.sort(reverse=True)
            v3 += sum(v5[:v4])
        return v3
