import itertools

class C1(object):

    def sortSentence(self, a1):
        """
        """
        v1 = a1.split()
        for v2 in range(len(v1)):
            while int(v1[v2][-1]) - 1 != v2:
                v1[int(v1[v2][-1]) - 1], v1[v2] = (v1[v2], v1[int(v1[v2][-1]) - 1])
        return ' '.join(map(lambda x: x[:-1], v1))
