# Time:  O(n^3 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set
class Solution_TLE(object):
    def distinctEchoSubstrings(self, text):
        """
        """
        def compare(text, l, s1, s2):
            for i in range(l):
                if text[s1+i] != text[s2+i]:
                    return False
            return True

        MOD = 10**9+7
        D = 27  # a-z and ''
        result = set()
        for i in range(len(text)):
            left, right, pow_D = 0, 0, 1
            for l in range(1, min(i+2, len(text)-i)):
                left = (D*left + (ord(text[i-l+1])-ord('a')+1)) % MOD
                right = (pow_D*(ord(text[i+l])-ord('a')+1) + right) % MOD
                if left == right and compare(text, l, i-l+1, i+1):
                    result.add(text[i+1:i+1+l])
                pow_D = (pow_D*D) % MOD 
        return len(result)
