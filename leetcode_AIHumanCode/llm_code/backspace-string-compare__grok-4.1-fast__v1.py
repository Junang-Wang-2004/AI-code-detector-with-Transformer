class Solution:
    def backspaceCompare(self, s, t):
        def clean(st):
            result = []
            for ch in st:
                if ch == '#':
                    result.pop() if result else None
                else:
                    result.append(ch)
            return result
        
        return clean(s) == clean(t)
