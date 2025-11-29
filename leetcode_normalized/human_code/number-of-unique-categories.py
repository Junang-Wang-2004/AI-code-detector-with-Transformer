class C1:

    def haveSameCategory(self, a1, a2):
        pass

class C2(object):

    def numberOfCategories(self, a1, a2):
        """
        """
        return sum((all((not a2.haveSameCategory(j, i) for v1 in range(i))) for v2 in range(a1)))
