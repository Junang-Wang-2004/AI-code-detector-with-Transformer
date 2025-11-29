from collections import deque

class Solution:
    def countSubTrees(self, n, edges, labels):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        childs = [[] for _ in range(n)]
        seen = [False] * n
        q = deque([0])
        seen[0] = True
        while q:
            curr = q.popleft()
            for neigh in graph[curr]:
                if not seen[neigh]:
                    seen[neigh] = True
                    childs[curr].append(neigh)
                    q.append(neigh)
        ans = [0] * n
        def postorder(node):
            idx = ord(labels[node]) - ord('a')
            total_same = 1
            freqs = [0] * 26
            freqs[idx] = 1
            for kid in childs[node]:
                kid_freqs = postorder(kid)
                total_same += kid_freqs[idx]
                for j in range(26):
                    freqs[j] += kid_freqs[j]
            ans[node] = total_same
            return freqs
        postorder(0)
        return ans
