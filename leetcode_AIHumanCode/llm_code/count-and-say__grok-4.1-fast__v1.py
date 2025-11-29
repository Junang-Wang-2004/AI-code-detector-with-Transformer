class Solution:
    def countAndSay(self, n):
        current = "1"
        for _ in range(n - 1):
            nxt = []
            idx = 0
            slen = len(current)
            while idx < slen:
                ch = current[idx]
                num = 1
                idx += 1
                while idx < slen and current[idx] == ch:
                    num += 1
                    idx += 1
                nxt.append(str(num) + ch)
            current = "".join(nxt)
        return current
