from collections import deque

class C1(object):

    def letterCombinations(self, a1):
        if not a1:
            return []
        v1 = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        v2 = deque([''])
        for v3 in a1:
            v4 = len(v2)
            for v5 in range(v4):
                v6 = v2.popleft()
                for v7 in v1[v3]:
                    v2.append(v6 + v7)
        return list(v2)
