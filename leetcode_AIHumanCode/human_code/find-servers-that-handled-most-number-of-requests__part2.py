# Time:  O(nlogk)
# Space: O(k)
import sortedcontainers  # required to do pip install
import itertools
import heapq


# reference: http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html
class Solution2(object):
    def busiestServers(self, k, arrival, load):
        """
        """
        count = [0]*k 
        min_heap_of_endtimes = []
        availables = sortedcontainers.SortedList(range(k))  # O(klogk)
        for i, (t, l) in enumerate(zip(arrival, load)):
            while min_heap_of_endtimes and min_heap_of_endtimes[0][0] <= t:
                _, free = heapq.heappop(min_heap_of_endtimes)  # O(logk)
                availables.add(free)  # O(logk)
            if not availables: 
                continue
            idx = availables.bisect_left(i % k) % len(availables)  # O(logk)
            node = availables.pop(idx)  # O(logk)
            count[node] += 1
            heapq.heappush(min_heap_of_endtimes, (t+l, node))  # O(logk)
        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count]
