class Solution(object):
    def selfDividingNumbers(self, left, right):
        output = []
        for value in range(left, right + 1):
            current = value
            valid = True
            while current > 0:
                remainder = current % 10
                if remainder == 0 or value % remainder != 0:
                    valid = False
                    break
                current //= 10
            if valid:
                output.append(value)
        return output
