# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set
class Solution2(object):
    def distinctEchoSubstrings(self, text):
        """
        """
        result = set()
        for l in range(1, len(text)//2+1):
            count = sum(text[i] == text[i+l] for i in range(l))
            for i in range(len(text)-2*l):
                if count == l:
                    result.add(text[i:i+l])
                count += (text[i+l] == text[i+l+l]) - (text[i] == text[i+l])
            if count == l:
                result.add(text[len(text)-2*l:len(text)-2*l+l])
        return len(result)


