# Time:  O(k * (n^(1/2) * n^(1/4) * n^(1/8) * n^(1/6) + n^(1/2) * n^(1/4) * n^(1/8) + n^(1/2) * n^(1/4) + n^(1/2))) <= O(k^2 * n)
# Space: O(k)
# backtracking, number theory
class Solution2(object):
    def minDifference(self, n, k):
        """
        """
        def factors(n):
            for i in range(1, n+1):
                if i*i > n:
                    break
                if n%i:
                    continue
                yield i
                if n//i != i:
                    yield n//i

        def backtracking(remain):
            start = curr[-1] if curr else 1
            if len(curr) == k-1 and remain >= start:
                curr.append(remain)
                if not result or result[-1]-result[0] > curr[-1]-curr[0]:
                    result[:] = curr
                curr.pop()
                return
            for i in factors(remain):
                if i < start:
                    continue
                curr.append(i)
                backtracking(remain//i)
                curr.pop()
                    
        result, curr = [], []
        backtracking(n)
        return result


