# Time:  O(n * k^n)
# Space: O(n * k^n)
class Solution5(object):
    def crackSafe(self, n, k):
        """
        """
        def dfs(k, node, lookup, result):
            for i in range(k):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use k-1 until there is no other choice
                neighbor = node + str(i)
                if neighbor not in lookup:
                    lookup.add(neighbor)
                    result.append(str(i))
                    dfs(k, neighbor[1:], lookup, result)
                    break

        result = [str(k-1)]*(n-1)
        lookup = set()
        dfs(k, "".join(result), lookup, result)
        return "".join(result)

