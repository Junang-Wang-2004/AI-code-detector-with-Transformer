class Solution:
    def letterCasePermutation(self, S):
        res = []
        def backtrack(i, path):
            if i == len(S):
                res.append(''.join(path))
                return
            ch = S[i]
            if ch.isalpha():
                path.append(ch.lower())
                backtrack(i + 1, path)
                path.pop()
                path.append(ch.upper())
                backtrack(i + 1, path)
                path.pop()
            else:
                path.append(ch)
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res
