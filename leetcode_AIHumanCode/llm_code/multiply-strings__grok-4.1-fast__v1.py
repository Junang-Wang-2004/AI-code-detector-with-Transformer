class Solution:
    def multiply(self, num1, num2):
        digits1 = [int(c) for c in reversed(num1)]
        digits2 = [int(c) for c in reversed(num2)]
        len1 = len(digits1)
        len2 = len(digits2)
        product = [0] * (len1 + len2)
        for i in range(len1):
            for j in range(len2):
                product[i + j] += digits1[i] * digits2[j]
        for k in range(len1 + len2 - 1):
            product[k + 1] += product[k] // 10
            product[k] %= 10
        idx = len1 + len2 - 1
        while idx > 0 and product[idx] == 0:
            idx -= 1
        if idx == 0 and product[0] == 0:
            return "0"
        return "".join(str(product[k]) for k in range(idx, -1, -1))
