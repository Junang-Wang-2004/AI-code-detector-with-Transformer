from collections import deque, defaultdict

class Solution:
    def sequenceReconstruction(self, org, seqs):
        n = len(org)
        valid_nums = set(org)
        adj = defaultdict(list)
        in_deg = {num: 0 for num in valid_nums}
        seen = set()
        for sequence in seqs:
            for val in sequence:
                if val not in valid_nums:
                    return False
                seen.add(val)
            for j in range(len(sequence) - 1):
                u = sequence[j]
                v = sequence[j + 1]
                if v not in adj[u]:
                    adj[u].append(v)
                    in_deg[v] += 1
        if len(seen) != n:
            return False
        ready = deque([nd for nd in valid_nums if in_deg[nd] == 0])
        if len(ready) != 1:
            return False
        result = []
        while ready:
            if len(ready) != 1:
                return False
            node = ready.popleft()
            result.append(node)
            for neighbor in adj[node]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    ready.append(neighbor)
        return result == org
