class C1(object):

    def camelMatch(self, a1, a2):

        def check_match(a1, a2):
            v1 = 0
            v2 = len(a2)
            for v3 in a1:
                v4 = False
                if v1 < v2 and v3 == a2[v1]:
                    v1 += 1
                    v4 = True
                if v3.isupper() and (not v4):
                    return False
            return v1 == v2
        return [check_match(txt, a2) for v1 in a1]
