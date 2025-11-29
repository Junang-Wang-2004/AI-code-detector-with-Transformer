class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        tree = [[] for _ in range(n)]
        for i in range(n):
            p = parent[i]
            if p != -1:
                tree[p].append(i)
        path = [[] for _ in range(26)]
        vals = [1] * n
        def visit(cur):
            ci = ord(s[cur]) - ord('a')
            path[ci].append(cur)
            for nxt in tree[cur]:
                visit(nxt)
                ni = ord(s[nxt]) - ord('a')
                tgt = path[ni][-1] if path[ni] else cur
                vals[tgt] += vals[nxt]
            path[ci].pop()
        visit(0)
        return vals
