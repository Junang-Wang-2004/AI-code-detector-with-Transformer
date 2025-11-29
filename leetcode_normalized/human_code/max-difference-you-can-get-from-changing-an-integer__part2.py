class C1(object):

    def maxDiff(self, a1):
        """
        """
        v1 = str(a1)
        v2 = next((x for v3 in v1 if v3 < '9'), '0')
        v4 = next((v3 for v3 in v1 if v3 > '1'), '0')
        return int(v1.replace(v2, '9')) - int(v1.replace(v4, '1' if v1[0] != '1' else '0'))
