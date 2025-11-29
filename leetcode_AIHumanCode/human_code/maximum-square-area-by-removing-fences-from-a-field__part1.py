# Time:  O(h^2 + v^2)
# Space: O(h^2 + v^2)

# hash table
class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        """
        MOD = 10**9+7
        def diff(arr, x):
            arr.append(1)
            arr.append(x)
            return {abs(arr[i]-arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr))}

        lookup = diff(hFences, m)
        result = -1
        for x in diff(vFences, n):
            if x in lookup:
                result = max(result, x**2)
        return result%MOD if result != -1 else -1


