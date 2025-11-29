# Time:  O(n^2 * logn)
# Space: O(n)
import bisect


class Solution3(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        """
        def check(tasks, workers, pills, strength, x):
            t = tasks[:x]
            for worker in workers[-x:]:  # enumerate from the weakest worker to the strongest worker, greedily assign him to the hardest task which he can do
                i = bisect.bisect_right(t, worker)-1
                if i != -1:
                    t.pop(i)
                    continue
                if pills:
                    i = bisect.bisect_right(t, worker+strength)-1
                    if i != -1:
                        t.pop(i)
                        pills -= 1
                        continue
                return False
            return True

        tasks.sort()
        workers.sort()
        left, right = 1, min(len(workers), len(tasks))
        while left <= right:
            mid = left + (right-left)//2
            if not check(tasks, workers, pills, strength, mid):
                right = mid-1
            else:
                left = mid+1
        return right


