class Solution:
    def smallestEquivalentString(self, s1, s2, target):
        par = list(range(26))
        def root(x):
            r = x
            while par[r] != r:
                r = par[r]
            i = x
            while i != r:
                nxt, i = par[i], nxt
                par[i] = r
            return r
        n = len(s1)
        a = ord('a')
        for i in range(n):
            u = ord(s1[i]) - a
            v = ord(s2[i]) - a
            ru = root(u)
            rv = root(v)
            if ru != rv:
                if ru < rv:
                    par[rv] = ru
                else:
                    par[ru] = rv
        res = []
        for c in target:
            res.append(chr(root(ord(c) - a) + a))
        return ''.join(res)
