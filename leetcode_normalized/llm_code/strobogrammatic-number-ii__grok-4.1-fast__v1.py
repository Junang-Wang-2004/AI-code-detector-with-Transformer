class C1:

    def findStrobogrammatic(self, a1):
        v1 = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        v2 = [('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        v3 = ['0', '1', '8'] if a1 % 2 else ['']
        v4 = v3
        for v5 in range(a1 // 2):
            v6 = len(v4[0])
            v7 = v2 if v6 == a1 - 2 else v1
            v8 = []
            for v9 in v4:
                for v10, v11 in v7:
                    v8.append(v10 + v9 + v11)
            v4 = v8
        return v4
