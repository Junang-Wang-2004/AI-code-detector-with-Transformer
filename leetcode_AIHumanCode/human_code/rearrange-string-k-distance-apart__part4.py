# Time:  O(nlogc), c is the count of unique characters.
# Space: O(c)
from collections import Counter
from heapq import heappush, heappop
class Solution4(object):
    def rearrangeString(self, s, k):
        """
        """
        if k <= 1:
            return s

        cnts = Counter(s)
        heap = []
        for c, cnt in cnts.items():
            heappush(heap, [-cnt, c])

        result = []
        while heap:
            used_cnt_chars = []
            for _ in range(min(k, len(s) - len(result))):
                if not heap:
                    return ""
                cnt_char = heappop(heap)
                result.append(cnt_char[1])
                cnt_char[0] += 1
                if cnt_char[0] < 0:
                    used_cnt_chars.append(cnt_char)
            for cnt_char in used_cnt_chars:
                heappush(heap, cnt_char)

        return "".join(result)
