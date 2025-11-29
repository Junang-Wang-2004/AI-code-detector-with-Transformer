# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    def multiply(self, num1, num2):
        """
        """
        result = [0]*(len(num1)+len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                result[i+j+1] += int(num1[i])*int(num2[j])
                result[i+j] += result[i+j+1]//10
                result[i+j+1] %= 10
        for i in range(len(result)):
            if result[i]:
                break
        return "".join([str(x) for x in result[i:]])

