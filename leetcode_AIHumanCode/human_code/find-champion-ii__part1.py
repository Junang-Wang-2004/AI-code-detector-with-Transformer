# Time:  O(n)
# Space: O(n)

# graph, hash table
class Solution2(object):
    def findChampion(self, n, edges):
        """
        """
        lookup = [False]*n
        for u, v in edges:
            lookup[v] = True
        result = -1
        for u in range(n):
            if lookup[u]:
                continue
            if result != -1:
                return -1
            result = u
        return result


