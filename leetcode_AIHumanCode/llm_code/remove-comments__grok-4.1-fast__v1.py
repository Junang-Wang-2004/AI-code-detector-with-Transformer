class Solution:
    def removeComments(self, source):
        ans = []
        in_block = False
        for s in source:
            buf = []
            i = 0
            n = len(s)
            while i < n:
                if in_block:
                    if i + 1 < n and s[i:i+2] == '*/':
                        in_block = False
                        i += 2
                    else:
                        i += 1
                    continue
                if i + 1 < n and s[i:i+2] == '//':
                    break
                if i + 1 < n and s[i:i+2] == '/*':
                    in_block = True
                    i += 2
                    continue
                buf.append(s[i])
                i += 1
            if buf:
                ans.append(''.join(buf))
        return ans
