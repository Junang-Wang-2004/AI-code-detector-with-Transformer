class Solution(object):
    def findMinFibonacciNumbers(self, k):
        fib = [1, 1]
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])
        count = 0
        for f in fib[::-1]:
            while k >= f:
                k -= f
                count += 1
        return count
