# Time:  O(2^(k-1) * k * n)
# Space: O(k)
# backtracking, number theory
class Solution3(object):
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
            if len(curr) == k-1:
                curr.append(remain)
                if not result or max(result)-min(result) > max(curr)-min(curr):
                    result[:] = curr
                curr.pop()
                return
            for i in factors(remain):
                curr.append(i)
                backtracking(remain//i)
                curr.pop()
                    
        result, curr = [], []
        backtracking(n)
        return result
