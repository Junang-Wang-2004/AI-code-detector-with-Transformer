# Time:  O(n * q)
# Space: O(p + n)
import collections


class Solution2(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :rtyp
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        result = []
        for i, j in queries:
            stk, lookup = [i], set([i])
            while stk:
                node = stk.pop()
                for nei in graph[node]:
                    if nei in lookup:
                        continue
                    stk.append(nei)
                    lookup.add(nei)
            result.append(j in lookup)
        return result
