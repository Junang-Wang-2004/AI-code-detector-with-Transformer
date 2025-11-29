class C1:

    def __init__(self, a1):
        self.cells = {}

    def setCell(self, a1, a2):
        self.cells[a1] = a2

    def resetCell(self, a1):
        self.cells.pop(a1, None)

    def getValue(self, a1):
        v1 = a1[1:].split('+')
        v2 = self.parse_operand(v1[0])
        v3 = self.parse_operand(v1[1])
        return v2 + v3

    def parse_operand(self, a1):
        try:
            return int(a1)
        except ValueError:
            return self.cells.get(a1, 0)
