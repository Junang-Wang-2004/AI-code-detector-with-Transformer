# Time:  O(k^n)
# Space: O(k^n)
class Solution2(object):
    def crackSafe(self, n, k):
        """
        """
        total = k**n
        M = total//k
        unique_rolling_hash = 0
        result = [str(0)]*(n-1)
        lookup = set()
        while len(lookup) < total:
            for i in reversed(range(k)):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use 0 until there is no other choice
                new_unique_rolling_hash = unique_rolling_hash*k + i
                if new_unique_rolling_hash not in lookup:
                    lookup.add(new_unique_rolling_hash)
                    result.append(str(i))
                    unique_rolling_hash = new_unique_rolling_hash%M
                    break
        return "".join(result)


