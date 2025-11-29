class C1(object):

    def evaluate(self, a1, a2):
        """
        """
        v1 = {k: v for v2, v3 in a2}
        v4, v5 = ([], [])
        v6 = False
        for v7 in a1:
            if v7 == '(':
                v6 = True
            elif v7 == ')':
                v6 = False
                v4.append(v1.get(''.join(v5), '?'))
                v5 = []
            elif v6:
                v5.append(v7)
            else:
                v4.append(v7)
        return ''.join(v4)
