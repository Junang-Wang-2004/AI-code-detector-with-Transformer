class C1(object):

    def hardestWorker(self, a1, a2):
        """
        """
        return a2[max(range(len(a2)), key=lambda x: (a2[x][1] - (a2[x - 1][1] if x - 1 >= 0 else 0), -a2[x][0]))][0]
