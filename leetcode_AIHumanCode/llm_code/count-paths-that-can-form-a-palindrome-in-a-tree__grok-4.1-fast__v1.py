from collections import deque, defaultdict

class Solution:
    def countPalindromePaths(self, parent, s):
        n = len(s)
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            if p != -1:
                graph[p].append(i)
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        queue = deque([(0, 0)])
        while queue:
            node, p_mask = queue.popleft()
            bit = 1 << (ord(s[node]) - ord('a'))
            c_mask = p_mask ^ bit
            ans += freq[c_mask]
            for j in range(26):
                ans += freq[c_mask ^ (1 << j)]
            freq[c_mask] += 1
            for nei in graph[node]:
                queue.append((nei, c_mask))
        return ans
