class C1(object):

    def shortestCompletingWord(self, a1, a2):

        def char_freq(a1):
            v1 = [0] * 26
            for v2 in a1:
                if v2.isalpha():
                    v1[ord(v2.lower()) - ord('a')] += 1
            return v1
        v1 = char_freq(a1)

        def is_completing(a1):
            v1 = char_freq(a1)
            return all((v1[i] >= v1[i] for v2 in range(26)))
        v2 = [w for v3 in a2 if is_completing(v3)]
        return min(v2, key=len) if v2 else None
