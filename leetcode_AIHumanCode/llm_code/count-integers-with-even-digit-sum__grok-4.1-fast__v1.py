class Solution:
    def countEven(self, num):
        s = str(num)
        p = sum(int(c) for c in s) % 2
        return (num - p) // 2
