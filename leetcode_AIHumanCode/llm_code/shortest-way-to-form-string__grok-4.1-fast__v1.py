import bisect

class Solution:
    def shortestWay(self, source, target):
        m = len(source)
        positions = [[] for _ in range(26)]
        for i in range(m):
            positions[ord(source[i]) - ord('a')].append(i)
        copies = 1
        ptr = 0
        for ch in target:
            cid = ord(ch) - ord('a')
            lst = positions[cid]
            if not lst:
                return -1
            idx = bisect.bisect_left(lst, ptr)
            if idx < len(lst):
                ptr = lst[idx] + 1
            else:
                copies += 1
                ptr = lst[0] + 1
        return copies
