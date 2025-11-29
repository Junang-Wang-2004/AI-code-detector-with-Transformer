class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        def pattern(u):
            mp = {}
            seq = []
            for idx, ch in enumerate(u):
                if ch not in mp:
                    mp[ch] = idx
                seq.append(mp[ch])
            return seq

        return pattern(s) == pattern(t)
