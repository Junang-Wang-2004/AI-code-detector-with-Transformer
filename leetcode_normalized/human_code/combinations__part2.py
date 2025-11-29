class C1(object):

    def combine(self, a1, a2):
        """
        """
        v1, v2 = ([], [])
        v3 = 1
        while True:
            if len(v2) == a2:
                v1.append(v2[:])
            if len(v2) == a2 or len(v2) + (a1 - v3 + 1) < a2:
                if not v2:
                    break
                v3 = v2.pop() + 1
            else:
                v2.append(v3)
                v3 += 1
        return v1
