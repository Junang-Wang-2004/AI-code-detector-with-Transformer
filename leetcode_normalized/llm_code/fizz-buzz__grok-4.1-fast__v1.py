class C1:

    def fizzBuzz(self, a1):
        v1 = []
        for v2 in range(1, a1 + 1):
            v3 = ''
            if v2 % 3 == 0:
                v3 += 'Fizz'
            if v2 % 5 == 0:
                v3 += 'Buzz'
            if not v3:
                v3 = str(v2)
            v1.append(v3)
        return v1
