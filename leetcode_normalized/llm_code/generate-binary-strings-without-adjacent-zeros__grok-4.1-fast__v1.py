class C1:

    def validStrings(self, a1):

        def build(a1, a2):
            if a1 == a1:
                return ['']
            v1 = []
            if a2:
                for v2 in build(a1 + 1, False):
                    v1.append('0' + v2)
            for v2 in build(a1 + 1, True):
                v1.append('1' + v2)
            return v1
        return build(0, True)
