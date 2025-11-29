# Time:  O(d * n)
# Space: O(d)
# case works, math, freq table
class Solution2(object):
    def countSubstrings(self, s):
        """
        """
        result = 0
        # digit 4
        for i in range(len(s)):
            if s[i] == '4':
                result += 1
                if i-1 >= 0 and int(s[i-1:i+1])%4 == 0:
                    result += i
        # digit 8
        for i in range(len(s)):
            if s[i] == '8':
                result += 1
                if i-1 >= 0 and int(s[i-1:i+1])%8 == 0:
                    result += 1
                if i-2 >= 0 and int(s[i-2:i+1])%8 == 0:
                    result += i-1
        for d in range(1, 9+1):
            if d in (4, 8):
                continue
            base = 1
            remain = 0
            cnt = [0]*d
            c = 0
            for i in range(len(s)):
                remain = (remain+base*(ord(s[~i])-ord('0')))%d
                c += cnt[remain]
                if s[~i] == str(d):
                    c += d != 8
                    cnt[remain] += 1
                base = (base*10)%d
            result += c
        return result


