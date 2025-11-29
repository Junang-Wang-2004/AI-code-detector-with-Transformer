# Time:  O(n^2)
# Space: O(n)
# brute force
class Solution2(object):
    def minimizeResult(self, expression):
        """
        """
        best = None
        min_val = float("inf")
        pos = expression.index('+')
        left, right = int(expression[0:pos]), int(expression[pos+1:])  # Space: O(n)
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
        return "".join([expression[:best[0]], '(', expression[best[0]:best[1]+1], ')', expression[best[1]+1:]])  # Space: O(n)

    
