class Solution:
    def lemonadeChange(self, bills):
        register = {5: 0, 10: 0}
        for payment in bills:
            if payment == 5:
                register[5] += 1
            elif payment == 10:
                if register[5] == 0:
                    return False
                register[5] -= 1
                register[10] += 1
            else:
                provided = False
                if register[10] > 0 and register[5] > 0:
                    register[10] -= 1
                    register[5] -= 1
                    provided = True
                if not provided and register[5] >= 3:
                    register[5] -= 3
                    provided = True
                if not provided:
                    return False
        return True
