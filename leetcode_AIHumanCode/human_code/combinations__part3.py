# Time:  O(k * C(n, k))
# Space: O(k)
class Solution3(object):
    def combine(self, n, k):
        """
        """
        def combineDFS(n, start, intermediate, k, result):
            if k == 0:
                result.append(intermediate[:])
                return
            for i in range(start, n):
                intermediate.append(i+1)
                combineDFS(n, i+1, intermediate, k-1, result)
                intermediate.pop()

        result = []
        combineDFS(n, 0, [], k, result)
        return result


