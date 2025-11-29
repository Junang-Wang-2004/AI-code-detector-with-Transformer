from collections import deque

class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        rev_adj = [[] for _ in range(n)]
        for i in range(n):
            rev_adj[favorite[i]].append(i)
        
        state = [0] * n
        cycles = []
        for i in range(n):
            if state[i] != 0:
                continue
            path_pos = {}
            step = 0
            x = i
            while state[x] == 0:
                state[x] = 1
                path_pos[x] = step
                step += 1
                x = favorite[x]
            if state[x] == 1 and x in path_pos:
                clen = step - path_pos[x]
                cycles.append((x, clen))
            for nd in path_pos:
                state[nd] = 2
        
        def longest_chain(start, exclude):
            q = deque([start])
            depth = 0
            while q:
                depth += 1
                sz = len(q)
                for _ in range(sz):
                    u = q.popleft()
                    for nei in rev_adj[u]:
                        if nei == exclude:
                            continue
                        q.append(nei)
            return depth
        
        max_long_cycle = 0
        total_pairs = 0
        for rep, clen in cycles:
            if clen > 2:
                max_long_cycle = max(max_long_cycle, clen)
            elif clen == 2:
                oth = favorite[rep]
                total_pairs += longest_chain(rep, oth) + longest_chain(oth, rep)
        
        return max(max_long_cycle, total_pairs)
