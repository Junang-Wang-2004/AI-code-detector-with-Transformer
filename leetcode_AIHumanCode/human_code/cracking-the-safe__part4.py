# Time:  O(n * k^n)
# Space: O(n * k^n)
class Solution4(object):
    def crackSafe(self, n, k):
        """
        """
        result = [str(k-1)]*(n-1)
        lookup = set()
        total = k**n
        while len(lookup) < total:
            node = result[len(result)-n+1:]
            for i in range(k):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use k-1 until there is no other choice
                neighbor = "".join(node) + str(i)
                if neighbor not in lookup:
                    lookup.add(neighbor)
                    result.append(str(i))
                    break
        return "".join(result)


