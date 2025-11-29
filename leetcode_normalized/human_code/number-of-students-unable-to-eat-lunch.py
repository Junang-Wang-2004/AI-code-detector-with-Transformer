import collections

class C1(object):

    def countStudents(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        for v2, v3 in enumerate(a2):
            if not v1[v3]:
                break
            v1[v3] -= 1
        else:
            v2 = len(a2)
        return len(a2) - v2
