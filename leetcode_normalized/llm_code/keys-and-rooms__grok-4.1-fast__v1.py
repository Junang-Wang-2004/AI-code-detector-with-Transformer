class C1:

    def canVisitAllRooms(self, a1):
        v1 = set()

        def traverse(a1):
            v1.add(a1)
            for v1 in a1[a1]:
                if v1 not in v1:
                    traverse(v1)
        traverse(0)
        return len(v1) == len(a1)
