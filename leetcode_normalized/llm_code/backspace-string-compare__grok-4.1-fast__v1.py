class C1:

    def backspaceCompare(self, a1, a2):

        def clean(a1):
            v1 = []
            for v2 in a1:
                if v2 == '#':
                    v1.pop() if v1 else None
                else:
                    v1.append(v2)
            return v1
        return clean(a1) == clean(a2)
