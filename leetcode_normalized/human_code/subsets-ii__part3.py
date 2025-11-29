class C1(object):

    def subsetsWithDup(self, a1):
        """
        """
        v1 = []
        self.subsetsWithDupRecu(v1, [], sorted(a1))
        return v1

    def subsetsWithDupRecu(self, a1, a2, a3):
        if not a3:
            if a2 not in a1:
                a1.append(a2)
        else:
            self.subsetsWithDupRecu(a1, a2, a3[1:])
            self.subsetsWithDupRecu(a1, a2 + [a3[0]], a3[1:])
