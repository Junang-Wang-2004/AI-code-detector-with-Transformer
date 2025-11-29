class C1(object):

    def twoSum(self, a1, a2):
        v1, v2 = (0, len(a1) - 1)
        while v1 != v2:
            sum = a1[v1] + a1[v2]
            if sum > a2:
                v2 -= 1
            elif sum < a2:
                v1 += 1
            else:
                return [v1 + 1, v2 + 1]
