class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        procs = sorted(processorTime)
        jobs = sorted(tasks, reverse=True)
        max_finish = 0
        n = len(procs)
        for idx in range(n):
            max_finish = max(max_finish, procs[idx] + jobs[4 * idx])
        return max_finish
