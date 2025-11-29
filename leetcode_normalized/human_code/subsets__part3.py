class C1(object):

    def subsets(self, a1):
        """
        """
        return self.subsetsRecu([], sorted(a1))

    def subsetsRecu(self, a1, a2):
        if not a2:
            return [a1]
        return self.subsetsRecu(a1, a2[1:]) + self.subsetsRecu(a1 + [a2[0]], a2[1:])
