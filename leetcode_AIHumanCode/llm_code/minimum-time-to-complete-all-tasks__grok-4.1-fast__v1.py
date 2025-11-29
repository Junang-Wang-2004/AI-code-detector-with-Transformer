class Solution:
    def findMinimumTime(self, tasks):
        max_end = max(t[1] for t in tasks)
        occupied = [False] * (max_end + 2)
        proc_tasks = sorted(tasks, key=lambda t: t[1])
        for interval in proc_tasks:
            begin, finish, req = interval
            covered = 0
            for pos in range(begin, finish + 1):
                if occupied[pos]:
                    covered += 1
            extra_needed = req - covered
            if extra_needed <= 0:
                continue
            for pos in range(finish, 0, -1):
                if extra_needed <= 0:
                    break
                if occupied[pos]:
                    continue
                occupied[pos] = True
                extra_needed -= 1
        ans = 0
        for i in range(1, max_end + 1):
            if occupied[i]:
                ans += 1
        return ans
