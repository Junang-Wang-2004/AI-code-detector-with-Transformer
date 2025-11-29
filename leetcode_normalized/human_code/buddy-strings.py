import itertools

class C1(object):

    def buddyStrings(self, a1, a2):
        """
        """
        if len(a1) != len(a2):
            return False
        v1 = []
        for v2, v3 in zip(a1, a2):
            if v2 != v3:
                v1.append((v2, v3))
                if len(v1) > 2:
                    return False
        return not v1 and len(set(a1)) < len(a1) or (len(v1) == 2 and v1[0] == v1[1][::-1])
