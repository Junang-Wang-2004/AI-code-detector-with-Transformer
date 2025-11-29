# Time:  O(h^2 + v^2)
# Space: O(min(h, v)^2)
# hash table
class Solution2(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        """
        MOD = 10**9+7
        def diff(arr, x, check):
            arr.append(1)
            arr.append(x)
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if not check:
                        lookup.add(abs(arr[i]-arr[j]))
                        continue
                    if abs(arr[i]-arr[j]) in lookup:
                        result[0] = max(result[0], (arr[i]-arr[j])**2)

        if len(hFences) > len(vFences):
            hFences, vFences = vFences, hFences
            m, n = n, m
        result = [-1]
        lookup = set()
        diff(hFences, m, False)
        diff(vFences, n, True)
        return result[0]%MOD if result[0] != -1 else -1
