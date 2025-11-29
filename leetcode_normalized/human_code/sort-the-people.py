class C1(object):

    def sortPeople(self, a1, a2):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a2[x], reverse=True)
        return [a1[i] for v2 in v1]
