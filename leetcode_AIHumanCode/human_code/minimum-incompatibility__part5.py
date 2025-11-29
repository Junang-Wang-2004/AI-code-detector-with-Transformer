# Time:  O(nlogn + k * n), could be improved to O(nlogn) by skiplist or orderedlist
# Space: O(n)
import collections
# wrong with greedy solution
# nums = [15, 9, 7, 10, 15, 14, 12, 2, 10, 8, 10, 13, 4, 11, 2]
# k = 5
# greedy  => [[2, 4, 7], [2, 8, 9], [10, 11, 12], [10, 13, 15], [10, 14, 15]] => 24
# correct => [[2, 4, 7], [2, 8, 10], [9, 10, 11], [10, 12, 15], [13, 14, 15]] => 22
class Solution_Wrong_Greedy(object):
    def minimumIncompatibility(self, nums, k):
        """
        """
        def greedy(nums, k, is_reversed):
            count = collections.Counter(nums)
            if max(count.values()) > k:
                return -1
            sorted_keys = sorted(list(count.keys()), reverse=is_reversed)
            stks = [[] for _ in range(k)] 
            curr, remain = 0, len(nums)
            while remain:  # the while loop runs O(k) times, and the inner loops runs O(n) times
                for x in sorted_keys:  # fill the deterministic elements into the remaining subsets
                    if count[x] != len(stks)-curr:
                        continue
                    for i in range(curr, len(stks)):
                        stks[i].append(x)
                    remain -= count[x]
                    count[x] = 0
                # greedily fill the contiguous ordered elements into the first vacant subset until it is full,
                # otherwise, the result sum would get larger => in fact, this is wrong
                for x in sorted_keys:
                    if not count[x]:
                        continue
                    stks[curr].append(x)
                    remain -= 1
                    count[x] -= 1
                    if len(stks[curr]) == len(nums)//k:
                        curr += 1
                        break
            return sum([max(stk)-min(stk) for stk in stks])

        return min(greedy(nums, k, False), greedy(nums, k, True))  # two possible minimas

