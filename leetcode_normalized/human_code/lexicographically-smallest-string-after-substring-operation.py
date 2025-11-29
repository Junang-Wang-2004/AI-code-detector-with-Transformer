class C1(object):

    def smallestString(self, a1):
        """
        """
        v1 = list(a1)
        v2 = next((v2 for v2 in range(len(a1)) if a1[v2] != 'a'), len(a1))
        if v2 == len(a1):
            v1[-1] = 'z'
        else:
            for v2 in range(v2, len(a1)):
                if v1[v2] == 'a':
                    break
                v1[v2] = chr(ord(v1[v2]) - 1)
        return ''.join(v1)
