import collections

class Solution:
    def killProcess(self, pid, ppid, kill):
        graph = collections.defaultdict(list)
        for idx, par in enumerate(ppid):
            graph[par].append(pid[idx])
        res = []
        q = collections.deque([kill])
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                q.append(nxt)
        return res
