class C1(object):

    def sortTheStudents(self, a1, a2):
        """
        """
        a1.sort(key=lambda x: x[a2], reverse=True)
        return a1
