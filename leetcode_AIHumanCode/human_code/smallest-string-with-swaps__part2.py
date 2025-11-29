# Time:  O(nlogn)
# Space: O(n)
import itertools
class Solution2(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        """
        def dfs(i, adj, lookup, component):
            lookup.add(i)
            component.append(i)
            for j in adj[i]:
                if j in lookup:
                    continue
                dfs(j, adj, lookup, component)
            
        adj = collections.defaultdict(list)
        for i, j in pairs:
            adj[i].append(j)
            adj[j].append(i)
        lookup = set()
        result = list(s)
        for i in range(len(s)):
            if i in lookup:
                continue
            component = []
            dfs(i, adj, lookup, component)
            component.sort()
            chars = sorted(result[k] for k in component)
            for comp, char in zip(component, chars):
                result[comp] = char
        return "".join(result)
