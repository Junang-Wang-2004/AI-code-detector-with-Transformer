class SQL:

    def __init__(self, table_names, col_lists):
        self.headers = dict(zip(table_names, col_lists))
        self.data_rows = {name: [] for name in table_names}
        self.del_flags = {name: [] for name in table_names}

    def insertRow(self, table, values):
        self.data_rows[table].append(values)
        self.del_flags[table].append("")

    def deleteRow(self, table, rid):
        self.del_flags[table][rid - 1] = "deleted"

    def selectCell(self, table, rid, cid):
        if rid == 0:
            return ""
        flag = self.del_flags[table][rid - 1]
        if flag != "":
            return ""
        return self.data_rows[table][rid - 1][cid - 1]
