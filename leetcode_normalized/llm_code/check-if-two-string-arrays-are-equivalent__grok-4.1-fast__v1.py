class C1:

    def arrayStringsAreEqual(self, a1, a2):

        def stream(a1):
            for v1 in a1:
                for v2 in v1:
                    yield v2
        v1 = stream(a1)
        v2 = stream(a2)
        while True:
            v3 = next(v1, None)
            v4 = next(v2, None)
            if v3 != v4:
                return False
            if v3 is None:
                return True
