class C1:

    def __init__(self):
        self.children = {}
        self.pass_count = 0
        self.best = 0

class C2:

    def longestCommonPrefix(self, a1, a2):
        v1 = C1()

        def traverse_update(a1, a2):
            v1 = [v1]
            v2 = v1
            for v3 in a1:
                if v3 not in v2.children:
                    v2.children[v3] = C1()
                v2 = v2.children[v3]
                v1.append(v2)
            for v4 in range(len(a1), -1, -1):
                v5 = v1[v4]
                v5.pass_count += a2
                v5.best = v4 if v5.pass_count >= a2 else 0
                for v6 in v5.children.values():
                    v5.best = max(v5.best, v6.best)
        v2 = len(a1)
        v3 = [0] * v2
        for v4 in a1:
            traverse_update(v4, 1)
        for v5 in range(v2):
            traverse_update(a1[v5], -1)
            v3[v5] = v1.best
            traverse_update(a1[v5], 1)
        return v3
