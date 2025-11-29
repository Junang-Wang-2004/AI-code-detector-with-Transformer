# Time:  O(1) ~ O(nlogn), n is 10^3
# Space: O(1)
import collections


class Solution4(object):
    def findEvenNumbers(self, digits):
        """
        """
        k = 3
        def backtracking(curr, digit_cnt, result):
            if len(curr) == k:
                result.append(reduce(lambda x, y: x*10+y, curr))
                return
            for i, (digit, cnt) in enumerate(digit_cnt):
                if (not curr and digit == 0) or (len(curr) == k-1 and digit%2 != 0):
                    continue
                digit_cnt[i][1] -= 1
                digit_cnt[i], digit_cnt[-1] = digit_cnt[-1], digit_cnt[i]
                removed = []
                if digit_cnt[-1][1] == 0:
                    removed = digit_cnt.pop()
                curr.append(digit)
                backtracking(curr, digit_cnt, result)
                curr.pop()
                if removed:
                    digit_cnt.append(removed)
                digit_cnt[i], digit_cnt[-1] = digit_cnt[-1], digit_cnt[i]
                digit_cnt[i][1] += 1

        cnt = collections.Counter(digits)
        digit_cnt = list(map(list, iter(cnt.items())))
        result = []
        backtracking([], digit_cnt, result)
        result.sort()
        return result
