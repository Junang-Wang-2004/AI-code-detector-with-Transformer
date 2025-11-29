class Solution:
    def sumFourDivisors(self, nums):
        output = 0
        for value in nums:
            divs_cnt = 0
            divs_total = 0
            sqrtn = int(value ** 0.5)
            for idx in range(1, sqrtn + 1):
                if value % idx == 0:
                    divs_total += idx
                    divs_cnt += 1
                    mate = value // idx
                    if idx != mate:
                        divs_total += mate
                        divs_cnt += 1
            if divs_cnt == 4:
                output += divs_total
        return output
