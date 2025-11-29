class C1:

    def flipLights(self, a1, a2):
        if a2 == 0:
            return 1
        if a1 == 1:
            return 2
        if a2 == 1:
            return 3 if a1 == 2 else 4
        if a1 == 2 or a2 == 2:
            return 4 if a1 == 2 else 7
        return 8
