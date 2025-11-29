class C1(object):

    def interpret(self, a1):
        """
        """
        v1, v2 = ([], 0)
        while v2 < len(a1):
            if a1[v2] == 'G':
                v1 += ['G']
                v2 += 1
            elif a1[v2] == '(' and a1[v2 + 1] == ')':
                v1 += ['o']
                v2 += 2
            else:
                v1 += ['al']
                v2 += 4
        return ''.join(v1)
