class C1(object):

    def search(self, a1, a2):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) / 2
            if a1[v3] == a2:
                return True
            elif a1[v3] == a1[v1]:
                v1 += 1
            elif a1[v3] > a1[v1] and a1[v1] <= a2 < a1[v3] or (a1[v3] < a1[v1] and (not a1[v3] < a2 <= a1[v2])):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return False
