class C1(object):

    def judgeCircle(self, a1):
        v1 = a1.count('R') - a1.count('L')
        v2 = a1.count('U') - a1.count('D')
        return v1 == 0 and v2 == 0
