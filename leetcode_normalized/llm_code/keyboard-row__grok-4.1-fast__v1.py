class C1:

    def findWords(self, a1):
        v1 = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        return [w for v2 in a1 if any((set(v2.lower()) <= set(line) for v3 in v1))]
