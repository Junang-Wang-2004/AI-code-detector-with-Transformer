class Solution(object):
    def secondHighest(self, s):
        present = [False] * 10
        for char in s:
            if char.isdigit():
                present[int(char)] = True
        max_val = -1
        sec_val = -1
        for digit in range(9, -1, -1):
            if present[digit]:
                if max_val == -1:
                    max_val = digit
                else:
                    sec_val = digit
                    break
        return sec_val
