class Solution:
    def addNegabinary(self, num1, num2):
        digits = []
        borrow = 0
        idx1 = len(num1) - 1
        idx2 = len(num2) - 1
        while idx1 >= 0 or idx2 >= 0 or borrow:
            sum_val = borrow
            if idx1 >= 0:
                sum_val += num1[idx1]
                idx1 -= 1
            if idx2 >= 0:
                sum_val += num2[idx2]
                idx2 -= 1
            digits.append(sum_val % 2)
            borrow = -(sum_val // 2)
        while len(digits) > 1 and digits[-1] == 0:
            digits.pop()
        digits.reverse()
        return digits
