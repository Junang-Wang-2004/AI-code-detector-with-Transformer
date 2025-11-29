class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def helper(x: str, y: str) -> bool:
            n = len(x)
            pos = 0
            while pos < n - pos:
                if x[pos] != y[n - 1 - pos]:
                    break
                pos += 1
            else:
                return True
            end = n - 1 - pos
            # Check if x[pos:end+1] is palindrome
            i = pos
            j = end
            while i < j:
                if x[i] != x[j]:
                    break
                i += 1
                j -= 1
            x_good = i >= j
            # Check if y[pos:end+1] is palindrome
            i = pos
            j = end
            while i < j:
                if y[i] != y[j]:
                    break
                i += 1
                j -= 1
            y_good = i >= j
            return x_good or y_good

        return helper(a, b) or helper(b, a)
