# Time:  O(n)
# Space: O(n)

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        """
        def iter_flood_fill(adj, node, lookup, idxs):
            stk = [node]
            while stk:
                node = stk.pop()
                if node in lookup:
                    continue
                lookup.add(node)
                idxs.append(node)
                for child in adj[node]:
                    stk.append(child)

        adj = [set() for i in range(len(source))]
        for i, j in allowedSwaps:
            adj[i].add(j)
            adj[j].add(i)
        result = 0
        lookup = set()
        for i in range(len(source)):
            if i in lookup:
                continue
            idxs = []
            iter_flood_fill(adj, i, lookup, idxs)
            source_cnt = collections.Counter([source[i] for i in idxs])
            target_cnt = collections.Counter([target[i] for i in idxs])
            diff = source_cnt-target_cnt
            result += sum(diff.values())
        return result


