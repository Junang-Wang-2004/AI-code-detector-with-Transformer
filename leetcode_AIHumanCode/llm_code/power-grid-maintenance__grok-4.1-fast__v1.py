class Solution(object):
    def processQueries(self, c, connections, queries):
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def unite(self, x, y):
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return
                if self.rank[px] < self.rank[py]:
                    self.parent[px] = py
                elif self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                else:
                    self.parent[py] = px
                    self.rank[px] += 1

        uf = UnionFind(c)
        for u, v in connections:
            uf.unite(u - 1, v - 1)

        stacks = {}
        for i in range(c - 1, -1, -1):
            rt = uf.find(i)
            if rt not in stacks:
                stacks[rt] = []
            stacks[rt].append(i)

        active = [True] * c
        output = []
        for tp, idd in queries:
            node = idd - 1
            if tp == 2:
                active[node] = False
            else:
                rt = uf.find(node)
                current_stack = stacks[rt]
                if active[node]:
                    output.append(node + 1)
                else:
                    while current_stack and not active[current_stack[-1]]:
                        current_stack.pop()
                    output.append(current_stack[-1] + 1 if current_stack else -1)
        return output
