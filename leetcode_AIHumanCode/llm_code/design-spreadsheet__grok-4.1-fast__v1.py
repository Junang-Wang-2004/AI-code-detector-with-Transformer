class Spreadsheet:

    def __init__(self, rows):
        self.cells = {}

    def setCell(self, cell, value):
        self.cells[cell] = value

    def resetCell(self, cell):
        self.cells.pop(cell, None)

    def getValue(self, formula):
        parts = formula[1:].split('+')
        a = self.parse_operand(parts[0])
        b = self.parse_operand(parts[1])
        return a + b

    def parse_operand(self, op):
        try:
            return int(op)
        except ValueError:
            return self.cells.get(op, 0)
