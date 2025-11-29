# Time:  O(n + n * log(26))
# Space: O(26)
import heapq


# greedy, counting sort, heap
class Solution2(object):
    def minimizeStringValue(self, s):
        """
        """
        def counting_sort(cnt):
            for i in range(len(cnt)):
                for _ in range(cnt[i]):
                    yield i

        cnt = [0]*26
        for x in s:
            if x == '?':
                continue
            cnt[ord(x)-ord('a')] += 1
        min_heap = [(x, i) for i, x in enumerate(cnt)]
        heapq.heapify(min_heap)
        cnt2 = [0]*26
        for _ in range(s.count('?')):
            c, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (c+1, i))
            cnt2[i] += 1
        it = counting_sort(cnt2)
        result = list(s)
        for i in range(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)


