class C1(object):

    def buildArray(self, a1, a2):
        """
        """
        v1, v2 = ([], 1)
        for v3 in a1:
            v1.extend(['Push', 'Pop'] * (v3 - v2))
            v1.append('Push')
            v2 = v3 + 1
        return v1
