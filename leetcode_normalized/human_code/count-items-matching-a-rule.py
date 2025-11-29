class C1(object):

    def countMatches(self, a1, a2, a3):
        """
        """
        v1 = {'type': 0, 'color': 1, 'name': 2}
        return sum((item[v1[a2]] == a3 for v2 in a1))
