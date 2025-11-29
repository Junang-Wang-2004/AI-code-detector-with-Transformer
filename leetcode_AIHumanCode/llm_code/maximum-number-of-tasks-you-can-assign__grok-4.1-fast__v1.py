class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def feasible(k):
            if k == 0:
                return True
            pill_rem = pills
            t_idx = k - 1
            w_start = len(workers) - k
            w_idx = w_start
            while t_idx >= 0:
                task = tasks[t_idx]
                while w_idx < len(workers) and workers[w_idx] < task:
                    w_idx += 1
                if w_idx < len(workers):
                    w_idx += 1
                    t_idx -= 1
                    continue
                if pill_rem <= 0:
                    return False
                target = task - strength
                while w_idx < len(workers) and workers[w_idx] < target:
                    w_idx += 1
                if w_idx < len(workers):
                    w_idx += 1
                    pill_rem -= 1
                    t_idx -= 1
                    continue
                return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left
