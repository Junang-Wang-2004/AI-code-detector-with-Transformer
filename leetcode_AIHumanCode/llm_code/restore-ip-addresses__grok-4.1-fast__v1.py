class Solution:
    def restoreIpAddresses(self, s):
        res = []
        def backtrack(pos, path):
            if len(path) == 4:
                if pos == len(s):
                    res.append('.'.join(path))
                return
            for nxt in range(pos + 1, min(pos + 4, len(s) + 1)):
                part = s[pos:nxt]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                path.append(part)
                backtrack(nxt, path)
                path.pop()
        backtrack(0, [])
        return res
