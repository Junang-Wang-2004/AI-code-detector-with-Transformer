# Time:  O(n^2)
# Space: O(1)

import itertools


# brute force
class Solution(object):
    def minimizeResult(self, expression):
        """
        """
        def stoi(s, i, j):
            result = 0
            for k in range(i, j):
                result = result*10+(ord(s[k])-ord('0'))
            return result

        best = None
        min_val = float("inf")
        pos = expression.index('+')
        left, right = stoi(expression, 0, pos), stoi(expression, pos+1, len(expression))
        base1, base2_init = 10**pos, 10**(len(expression)-(pos+1)-1)
        for i in range(pos):
            base2 = base2_init
            for j in range(pos+1, len(expression)):
                a, b = divmod(left, base1)
                c, d = divmod(right, base2)
                val = max(a, 1)*(b+c)*max(d, 1)
                if val < min_val:
                    min_val = val
                    best = (i, j)
                base2 //= 10
            base1 //= 10
        return "".join(itertools.chain((expression[i] for i in range(best[0])),
                                       '(', (expression[i] for i in range(best[0], best[1]+1)), ')',
                                       (expression[i] for i in range(best[1]+1, len(expression)))))


