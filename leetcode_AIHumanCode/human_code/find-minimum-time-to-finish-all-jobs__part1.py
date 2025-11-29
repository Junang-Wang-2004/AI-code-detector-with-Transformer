# Time:  O(k^n * logr), the real complexity shoud be much less, but hard to analyze
# Space: O(n + k)

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        """
        def backtracking(jobs, i, cap, counts):
            if i == len(jobs):
                return True
            for j in range(len(counts)):
                if counts[j]+jobs[i] <= cap:
                    counts[j] += jobs[i]
                    if backtracking(jobs, i+1, cap, counts):
                        return True
                    counts[j] -= jobs[i]
                if counts[j] == 0:
                    break
            return False

        jobs.sort(reverse=True)
        left, right = max(jobs), sum(jobs)
        while left <= right:
            mid = left + (right-left)//2
            if backtracking(jobs, 0, mid, [0]*k):
                right = mid-1
            else:
                left = mid+1
        return left


