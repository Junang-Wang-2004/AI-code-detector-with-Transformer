class C1(object):

    def minRemoveToMakeValid(self, a1):
        """
        """
        v1 = list(a1)
        v2 = 0
        for v3, v4 in enumerate(v1):
            if v4 == '(':
                v2 += 1
            elif v4 == ')':
                if v2:
                    v2 -= 1
                else:
                    v1[v3] = ''
        if v2:
            for v3 in reversed(range(len(v1))):
                if v1[v3] == '(':
                    v1[v3] = ''
                    v2 -= 1
                    if not v2:
                        break
        return ''.join(v1)
