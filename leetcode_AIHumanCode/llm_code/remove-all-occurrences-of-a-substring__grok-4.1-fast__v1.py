class Solution(object):
    def removeOccurrences(self, s, part):
        m = len(part)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if part[i] == part[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        builder = []
        statuses = []
        q = 0
        for ch in s:
            p = q
            while p > 0 and ch != part[p]:
                p = lps[p - 1]
            if ch == part[p]:
                p += 1
            q = p
            builder.append(ch)
            statuses.append(q)
            if q == m:
                del builder[-m:]
                del statuses[-m:]
                q = statuses[-1] if statuses else 0
        return "".join(builder)
