# Time:  O(n + n * 26)
# Space: O(26)
# greedy, counting sort
class Solution3(object):
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
        cnt2 = [0]*26
        for _ in range(s.count('?')):
            i = min(range(len(cnt)), key=lambda x: cnt[x]+cnt2[x])
            cnt2[i] += 1
        it = counting_sort(cnt2)
        result = list(s)
        for i in range(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)
