class Solution(object):
    def longestDecomposition(self, text):
        def segments_match(s, ln, start1, start2):
            for k in range(ln):
                if s[start1 + k] != s[start2 + k]:
                    return False
            return True

        s = text
        n = len(s)
        count = 0
        begin = 0
        finish = n - 1
        base = 29
        modulus = 10**9 + 7
        while begin < finish:
            maxl = (finish - begin + 1) // 2
            phash = 0
            shash = 0
            pw = 1
            gotit = False
            clen = 0
            while clen < maxl:
                clen += 1
                pchar = ord(s[begin + clen - 1]) - ord('a')
                phash = (phash * base + pchar) % modulus
                schar = ord(s[finish - clen + 1]) - ord('a')
                shash = (schar * pw + shash) % modulus
                pw = (pw * base) % modulus
                if phash == shash and segments_match(s, clen, begin, finish - clen + 1):
                    count += 1
                    begin += clen
                    finish -= clen
                    gotit = True
                    break
            if not gotit:
                break
        return count
