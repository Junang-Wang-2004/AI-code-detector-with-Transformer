from collections import Counter

class Solution:
    def permuteUnique(self, numbers):
        freq = Counter(numbers)
        total = len(numbers)
        ans = []
        stack = []
        
        def backtrack():
            if len(stack) == total:
                ans.append(list(stack))
                return
            for digit in freq:
                if freq[digit] > 0:
                    freq[digit] -= 1
                    stack.append(digit)
                    backtrack()
                    stack.pop()
                    freq[digit] += 1
        
        backtrack()
        return ans
