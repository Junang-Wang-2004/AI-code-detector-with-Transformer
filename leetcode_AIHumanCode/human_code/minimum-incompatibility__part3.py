# Time:  O(nlogn)
# Space: O(n)
import collections
import sortedcontainers
# wrong with greedy solution
# nums = [15, 9, 7, 10, 15, 14, 12, 2, 10, 8, 10, 13, 4, 11, 2]
# k = 5
# greedy  => [[2, 4, 7], [2, 8, 9], [10, 11, 12], [10, 13, 15], [10, 14, 15]] => 24
# correct => [[2, 4, 7], [2, 8, 10], [9, 10, 11], [10, 12, 15], [13, 14, 15]] => 22
# optimized from Solution_Greedy, using SortedList (which is not supported in GoogleCodeJam / GoogleKickStart)
class Solution_Wrong_Greedy_SortedList(object):
    def minimumIncompatibility(self, nums, k):
        """
        """
        def greedy(nums, k, is_reversed):
            count = collections.Counter(nums)
            if max(count.values()) > k:
                return -1
            ordered_set = sortedcontainers.SortedList(iter(count.keys()))
            freq_to_nodes = collections.defaultdict(collections.OrderedDict)
            for x in ordered_set:
                freq_to_nodes[count[x]][x] = count[x]
            stks = [[] for _ in range(k)] 
            curr = 0
            while ordered_set:  # the while loop runs O(k) times
                if len(stks)-curr in freq_to_nodes:  # fill the deterministic elements into the remaining subsets
                    for x in freq_to_nodes[len(stks)-curr].keys():  # total time = O(n)
                        for i in range(curr, len(stks)):
                            stks[i].append(x)
                        count.pop(x)
                        ordered_set.remove(x)
                    freq_to_nodes.pop(len(stks)-curr)
                # greedily fill the contiguous ordered elements into the first vacant subset until it is full,
                # otherwise, the result sum would get larger => in fact, this is wrong
                to_remove = []
                direction = (lambda x:x) if not is_reversed else reversed
                for x in direction(ordered_set):
                    stks[curr].append(x)
                    freq_to_nodes[count[x]].pop(x)
                    if not freq_to_nodes[count[x]]:
                        freq_to_nodes.pop(count[x])
                    count[x] -= 1  # total time = O(n)
                    if not count[x]:
                        count.pop(x)
                        to_remove.append(x)
                    else:
                        freq_to_nodes[count[x]][x] = count[x]
                    if len(stks[curr]) == len(nums)//k:
                        curr += 1
                        break
                for x in to_remove:
                    ordered_set.remove(x)  # total time = O(nlogn)
            return sum([max(stk)-min(stk) for stk in stks])

        return min(greedy(nums, k, False), greedy(nums, k, True))  # two possible minimas


