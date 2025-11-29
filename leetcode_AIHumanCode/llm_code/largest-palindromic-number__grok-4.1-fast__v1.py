import collections

class Solution:
    def largestPalindromic(self, num):
        freq = collections.Counter(num)
        front = []
        for d in range(9, 0, -1):
            pairs = freq[str(d)] // 2
            front.extend([str(d)] * pairs)
        zero_pairs = freq['0'] // 2
        if front:
            front.extend(['0'] * zero_pairs)
        center = ''
        for d in range(9, -1, -1):
            if freq[str(d)] % 2:
                center = str(d)
                break
        back = front[::-1]
        res = ''.join(front) + center + ''.join(back)
        return res if res else '0'
