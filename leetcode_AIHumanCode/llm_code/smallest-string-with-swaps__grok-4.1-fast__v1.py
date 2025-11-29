from collections import deque

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = [[] for _ in range(n)]
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        output = list(s)
        for start in range(n):
            if seen[start]:
                continue
            comp = []
            queue = deque([start])
            seen[start] = True
            while queue:
                node = queue.popleft()
                comp.append(node)
                for neigh in graph[node]:
                    if not seen[neigh]:
                        seen[neigh] = True
                        queue.append(neigh)
            comp.sort()
            letters = sorted(output[i] for i in comp)
            for idx, letter in zip(comp, letters):
                output[idx] = letter
        return ''.join(output)
