class C1(object):

    def numberToWords(self, a1):
        """
        """
        if a1 == 0:
            return 'Zero'
        v1 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        v2 = ['', 'Thousand', 'Million', 'Billion']
        v3, v4 = ([], 0)
        while a1:
            v5 = a1 % 1000
            if a1 % 1000:
                v3.append(self.threeDigits(v5, v1, v2[v4]))
            a1 //= 1000
            v4 += 1
        return ' '.join(v3[::-1])

    def threeDigits(self, a1, a2, a3):
        v1 = []
        if a1 / 100:
            v1 = [a2[a1 / 100] + ' ' + 'Hundred']
        if a1 % 100:
            v1.append(self.twoDigits(a1 % 100, a2))
        if a3 != '':
            v1.append(a3)
        return ' '.join(v1)

    def twoDigits(self, a1, a2):
        if a1 in a2:
            return a2[a1]
        return a2[a1 / 10 * 10] + ' ' + a2[a1 % 10]
