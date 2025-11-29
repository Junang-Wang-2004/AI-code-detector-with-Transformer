class C1(object):

    def removeDuplicates(self, a1, a2):
        """
        """
        v1 = [['^', 0]]
        for v2 in a1:
            if v1[-1][0] == v2:
                v1[-1][1] += 1
                if v1[-1][1] == a2:
                    v1.pop()
            else:
                v1.append([v2, 1])
        return ''.join((v2 * a2 for v2, a2 in v1))
