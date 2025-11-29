class C1(object):

    def find132pattern(self, a1):
        """
        """
        for v1 in range(len(a1)):
            v2 = False
            for v3 in range(v1):
                if a1[v3] < a1[v1]:
                    v2 = True
                elif a1[v3] > a1[v1]:
                    if v2:
                        return True
        return False
