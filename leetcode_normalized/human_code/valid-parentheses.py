class C1(object):

    def isValid(self, a1):
        v1, v2 = ([], {'(': ')', '{': '}', '[': ']'})
        for v3 in a1:
            if v3 in v2:
                v1.append(v3)
            elif len(v1) == 0 or v2[v1.pop()] != v3:
                return False
        return len(v1) == 0
