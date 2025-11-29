class C1(object):

    def find132pattern(self, a1):
        """
        """
        v1 = float('-inf')
        v2 = []
        for v3 in reversed(range(len(a1))):
            if a1[v3] < v1:
                return True
            while v2 and v2[-1] < a1[v3]:
                v1 = v2.pop()
            v2.append(a1[v3])
        return False
