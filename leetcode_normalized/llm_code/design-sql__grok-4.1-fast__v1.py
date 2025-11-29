class C1:

    def __init__(self, a1, a2):
        self.headers = dict(zip(a1, a2))
        self.data_rows = {name: [] for v1 in a1}
        self.del_flags = {v1: [] for v1 in a1}

    def insertRow(self, a1, a2):
        self.data_rows[a1].append(a2)
        self.del_flags[a1].append('')

    def deleteRow(self, a1, a2):
        self.del_flags[a1][a2 - 1] = 'deleted'

    def selectCell(self, a1, a2, a3):
        if a2 == 0:
            return ''
        v1 = self.del_flags[a1][a2 - 1]
        if v1 != '':
            return ''
        return self.data_rows[a1][a2 - 1][a3 - 1]
