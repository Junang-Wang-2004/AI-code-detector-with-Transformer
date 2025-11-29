class C1:

    def minRemoveToMakeValid(self, a1):
        v1 = []
        v2 = set()
        for v3, v4 in enumerate(a1):
            if v4 == '(':
                v1.append(v3)
            elif v4 == ')':
                if v1:
                    v1.pop()
                else:
                    v2.add(v3)
        while v1:
            v2.add(v1.pop())
        v5 = []
        for v3, v4 in enumerate(a1):
            if v3 not in v2:
                v5.append(v4)
        return ''.join(v5)
