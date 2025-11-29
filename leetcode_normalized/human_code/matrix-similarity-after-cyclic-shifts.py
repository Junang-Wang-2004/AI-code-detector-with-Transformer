class C1(object):

    def areSimilar(self, a1, a2):
        """
        """
        return all((row[i] == row[(i + a2) % len(row)] for v1 in a1 for v2 in range(len(v1))))
