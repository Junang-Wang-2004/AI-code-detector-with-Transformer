# Time:  O(26 * n + 26 * log(26))
# Space: O(26)
# hash table, sort, greedy
class Solution2(object):
    def maxSubstringLength(self, s, k):
        """
        """
        def erase_overlap_intervals(intervals):
            intervals.sort(key=lambda interval: interval[1])
            result, right = 0, float("-inf")
            for l, r in intervals:
                if l <= right:
                    result += 1
                else:
                    right = r
            return result

        cnt = [0]*26
        lookup1, lookup2 = [-1]*26, [-1]*26
        for i, c in enumerate(s):
            cnt[ord(c)-ord('a')] += 1
            if lookup1[ord(c)-ord('a')] == -1:
                lookup1[ord(c)-ord('a')] = i
            lookup2[ord(c)-ord('a')] = i 
        intervals = []
        for i in range(len(s)):
            if i != lookup1[ord(s[i])-ord('a')]:
                continue
            x = i+1
            j = lookup2[ord(s[i])-ord('a')]
            while x <= j and lookup1[ord(s[x])-ord('a')] >= i:
                j = max(j, lookup2[ord(s[x])-ord('a')])
                x += 1
            if x == j+1 and (i != 0 or j != len(s)-1):
                intervals.append((i, j))
        return len(intervals)-erase_overlap_intervals(intervals) >= k
