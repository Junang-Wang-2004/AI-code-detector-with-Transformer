class ArrayReader(object):
    def query(self, a, b, c, d):
        pass

    def length(self):
        pass

class Solution(object):
    def guessMajority(self, reader):
        base = reader.query(0, 1, 2, 3)
        q024 = reader.query(0, 1, 2, 4)
        matches = 1
        mismatches = 0
        mis_idx = None
        nlen = reader.length()
        if q024 == base:
            matches += 1
        else:
            mismatches += 1
            mis_idx = 4
        for j in range(5, nlen):
            qj = reader.query(0, 1, 2, j)
            if qj == base:
                matches += 1
            else:
                mismatches += 1
                mis_idx = j
        ex0 = reader.query(1, 2, 3, 4)
        if ex0 == q024:
            matches += 1
        else:
            mismatches += 1
            mis_idx = 0
        ex1 = reader.query(0, 2, 3, 4)
        if ex1 == q024:
            matches += 1
        else:
            mismatches += 1
            mis_idx = 1
        ex2 = reader.query(0, 1, 3, 4)
        if ex2 == q024:
            matches += 1
        else:
            mismatches += 1
            mis_idx = 2
        if matches == mismatches:
            return -1
        return 3 if matches > mismatches else mis_idx
