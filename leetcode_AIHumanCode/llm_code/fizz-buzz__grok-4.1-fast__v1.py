class Solution:
    def fizzBuzz(self, n):
        output = []
        for num in range(1, n + 1):
            msg = ""
            if num % 3 == 0:
                msg += "Fizz"
            if num % 5 == 0:
                msg += "Buzz"
            if not msg:
                msg = str(num)
            output.append(msg)
        return output
