import itertools

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__table = {name: [column] for v1, v2 in zip(a1, a2)}

    def insertRow(self, a1, a2):
        """
        """
        a2.append('')
        self.__table[a1].append(a2)

    def deleteRow(self, a1, a2):
        """
        """
        self.__table[a1][a2][-1] = 'deleted'

    def selectCell(self, a1, a2, a3):
        """
        """
        return self.__table[a1][a2][a3 - 1] if self.__table[a1][a2][-1] == '' else ''
