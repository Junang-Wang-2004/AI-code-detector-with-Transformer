import itertools

class C1(object):

    def busyStudent(self, a1, a2, a3):
        """
        """
        return sum((s <= a3 <= e for v1, v2 in zip(a1, a2)))
