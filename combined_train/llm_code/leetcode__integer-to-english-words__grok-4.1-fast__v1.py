class C1:

    def numberToWords(self, a1):
        if a1 == 0:
            return 'Zero'
        v1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        v2 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        v3 = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
        v4 = ['Billion', 'Million', 'Thousand', '']
        v5 = [10 ** 9, 10 ** 6, 10 ** 3, 1]
        v6 = []
        for v7, v8 in enumerate(v5):
            v9 = a1 // v8 % 1000
            if v9 > 0:
                v10 = self._convert_group(v9, v1, v2, v3)
                if v4[v7]:
                    v10 += ' ' + v4[v7]
                v6.append(v10)
        return ' '.join(v6)

    def _convert_group(self, a1, a2, a3, a4):
        v1 = []
        v2 = a1 // 100
        v3 = a1 % 100
        if v2 > 0:
            v1.append(a2[v2] + ' Hundred')
        if v3 > 0:
            if v3 < 10:
                v1.append(a2[v3])
            elif v3 < 20:
                v1.append(a3[v3])
            else:
                v4 = v3 // 10
                v5 = v3 % 10
                v1.append(a4[v4])
                if v5 > 0:
                    v1.append(a2[v5])
        return ' '.join(v1)
