class C1(object):

    def fizzBuzz(self, a1):
        """
        """
        v1 = []
        for v2 in range(1, a1 + 1):
            if v2 % 15 == 0:
                v1.append('FizzBuzz')
            elif v2 % 5 == 0:
                v1.append('Buzz')
            elif v2 % 3 == 0:
                v1.append('Fizz')
            else:
                v1.append(str(v2))
        return v1

    def fizzBuzz2(self, a1):
        """
        """
        v1 = [str(x) for v2 in range(a1 + 1)]
        v3 = list(range(0, a1 + 1, 3))
        v4 = list(range(0, a1 + 1, 5))
        for v5 in v3:
            v1[v5] = 'Fizz'
        for v5 in v4:
            if v1[v5] == 'Fizz':
                v1[v5] += 'Buzz'
            else:
                v1[v5] = 'Buzz'
        return v1[1:]

    def fizzBuzz3(self, a1):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for v1 in range(1, a1 + 1)]

    def fizzBuzz4(self, a1):
        return ['FizzBuzz'[i % -3 & -4:i % -5 & 8 ^ 12] or repr(i) for v1 in range(1, a1 + 1)]
