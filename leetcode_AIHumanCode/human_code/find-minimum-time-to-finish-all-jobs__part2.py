# Time:  O(k * k^n), the real complexity shoud be less, but hard to analyze
# Space: O(n + k)
class Solution2(object):
    def minimumTimeRequired(self, jobs, k):
        """
        """
        def backtracking(jobs, i, counts, result):
            if i == len(jobs):
                result[0] = min(result[0], max(counts))
                return
            for j in range(len(counts)):
                if counts[j]+jobs[i] <= result[0]:
                    counts[j] += jobs[i]
                    backtracking(jobs, i+1, counts, result)
                    counts[j] -= jobs[i]
                if counts[j] == 0:
                    break

        jobs.sort(reverse=False)
        result = [sum(jobs)]
        backtracking(jobs, 0, [0]*k, result)
        return result[0]
