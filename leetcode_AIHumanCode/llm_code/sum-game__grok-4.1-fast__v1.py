class Solution:
    def sumGame(self, num):
        n = len(num)
        m = n // 2
        left_sum = sum(int(num[i]) for i in range(m) if num[i] != '?')
        right_sum = sum(int(num[i]) for i in range(m, n) if num[i] != '?')
        left_q = sum(1 for i in range(m) if num[i] == '?')
        right_q = sum(1 for i in range(m, n) if num[i] == '?')
        diff = left_sum - right_sum
        delta = right_q - left_q
        if delta % 2 != 0:
            return True
        return diff != (delta // 2) * 9
