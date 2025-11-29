class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        num_jobs = len(difficulty)
        job_pairs = [(difficulty[idx], profit[idx]) for idx in range(num_jobs)]
        job_pairs.sort(key=lambda tp: tp[0])
        if num_jobs == 0:
            return 0
        prefix_max = [0] * num_jobs
        prefix_max[0] = job_pairs[0][1]
        for jdx in range(1, num_jobs):
            prefix_max[jdx] = max(prefix_max[jdx - 1], job_pairs[jdx][1])
        overall = 0
        for cap in worker:
            lo, hi = 0, num_jobs - 1
            furthest = -1
            while lo <= hi:
                md = (lo + hi) // 2
                if job_pairs[md][0] <= cap:
                    furthest = md
                    lo = md + 1
                else:
                    hi = md - 1
            if furthest >= 0:
                overall += prefix_max[furthest]
        return overall
