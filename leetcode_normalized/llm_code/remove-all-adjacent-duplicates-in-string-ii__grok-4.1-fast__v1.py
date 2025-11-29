class C1(object):

    def removeDuplicates(self, a1, a2):
        v1 = []
        for v2 in a1:
            v1.append(v2)
            while len(v1) >= a2 and v1[-a2:] == [v1[-1]] * a2:
                del v1[-a2:]
        return ''.join(v1)
