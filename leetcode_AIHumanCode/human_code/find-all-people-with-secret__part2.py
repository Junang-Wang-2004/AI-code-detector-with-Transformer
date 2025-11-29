# Time:  O(nlogn)
# Space: O(n)
import collections


class Solution2(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        """
        meetings.sort(key=lambda x: x[2])
        result = {0, firstPerson}
        adj = collections.defaultdict(list)
        for i, (x, y, _) in enumerate(meetings):
            adj[x].append(y)
            adj[y].append(x)
            if i+1 != len(meetings) and meetings[i+1][2] == meetings[i][2]:
                continue
            stk = [i for i in adj.keys() if i in result]
            while stk:
                u = stk.pop()
                for v in adj[u]:
                    if v in result:
                        continue
                    result.add(v)
                    stk.append(v)
            adj = collections.defaultdict(list)
        return list(result)


