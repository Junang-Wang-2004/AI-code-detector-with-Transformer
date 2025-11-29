# Time:  O(logn * logn)
# Space: O(logn)
class Solution2(object):
    def findKthNumber(self, n, k):
        """
        """
        def count(n, prefix):
            result, number = 0, 1
            while prefix <= n:
                result += number
                prefix *= 10
                number *= 10
            result -= max(number/10 - (n - prefix/10 + 1), 0)
            return result

        def findKthNumberHelper(n, k, cur, index):
            if cur:
                index += 1
                if index == k:
                    return (cur, index)

            i = int(cur == 0)
            while i <= 9:
                cur = cur * 10 + i
                cnt = count(n, cur)
                if k > cnt + index:
                    index += cnt
                elif cur <= n:
                    result = findKthNumberHelper(n, k, cur, index)
                    if result[0]:
                        return result
                i += 1
                cur /= 10
            return (0, index)

        return findKthNumberHelper(n, k, 0, 0)[0]

