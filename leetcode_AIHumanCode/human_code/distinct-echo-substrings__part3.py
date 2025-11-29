# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set
class Solution3(object):
    def distinctEchoSubstrings(self, text):
        """
        """
        MOD = 10**9+7
        D = 27  # a-z and ''
        result = set()
        for i in range(len(text)-1):
            left, right, pow_D = 0, 0, 1
            for l in range(1, min(i+2, len(text)-i)):
                left = (D*left + (ord(text[i-l+1])-ord('a')+1)) % MOD
                right = (pow_D*(ord(text[i+l])-ord('a')+1) + right) % MOD
                if left == right:  # assumed no collision
                    result.add(left)
                pow_D = (pow_D*D) % MOD 
        return len(result)


