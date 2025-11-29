class C1:

    def isValid(self, a1):
        v1 = []
        for v2 in a1:
            if v2 == 'c':
                if not v1 or v1.pop() != 'b':
                    return False
                if not v1 or v1.pop() != 'a':
                    return False
            else:
                v1.append(v2)
        return not v1
