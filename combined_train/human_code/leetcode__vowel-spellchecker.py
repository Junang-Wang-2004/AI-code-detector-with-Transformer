class C1(object):

    def spellchecker(self, a1, a2):
        """
        """
        v1 = set(['a', 'e', 'i', 'o', 'u'])

        def todev(a1):
            return ''.join(('*' if c.lower() in v1 else c.lower() for v1 in a1))
        v2 = set(a1)
        v3 = {}
        v4 = {}
        for v5 in a1:
            v3.setdefault(v5.lower(), v5)
            v4.setdefault(todev(v5), v5)

        def check(a1):
            if a1 in v2:
                return a1
            v1 = a1.lower()
            if v1 in v3:
                return v3[v1]
            v2 = todev(v1)
            if v2 in v4:
                return v4[v2]
            return ''
        return list(map(check, a2))
