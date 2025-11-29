class Solution(object):
    def reformatNumber(self, number):
        s = ''.join(c for c in number if c.isdigit())
        n = len(s)
        chunks = []
        i = 0
        while i < n:
            remaining = n - i
            if remaining == 4:
                chunks.append(s[i:i+2])
                chunks.append(s[i+2:])
                i = n
            else:
                chunk_size = min(3, remaining)
                chunks.append(s[i:i + chunk_size])
                i += chunk_size
        return '-'.join(chunks)
