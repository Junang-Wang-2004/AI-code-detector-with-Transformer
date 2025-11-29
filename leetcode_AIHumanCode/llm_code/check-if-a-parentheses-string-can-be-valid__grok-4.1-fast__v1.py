class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        def check_forward():
            bal = 0
            unlocks = 0
            for i in range(n):
                if locked[i] == '0':
                    unlocks += 1
                elif s[i] == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal + unlocks < 0:
                    return False
            return True
        
        def check_backward():
            bal = 0
            unlocks = 0
            for i in range(n - 1, -1, -1):
                if locked[i] == '0':
                    unlocks += 1
                elif s[i] == ')':
                    bal += 1
                else:
                    bal -= 1
                if bal + unlocks < 0:
                    return False
            return True
        
        return check_forward() and check_backward()
