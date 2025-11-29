# Time:  O(n * sqrt(n))
# Space: O(1)

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        """
        result = 0
        for num in nums:
            facs, i = [], 1
            while i*i <= num:
                if num % i:
                    i+= 1
                    continue
                facs.append(i)
                if i != num//i:
                    facs.append(num//i)
                    if len(facs) > 4:
                        break
                i += 1
            if len(facs) == 4:            
                result += sum(facs)
        return result 


