class C1(object):

    def __init__(self, a1):
        """
        initialize your data structure here.
        """
        self.accu = [0]
        for v1 in a1:
            (self.accu.append(self.accu[-1] + v1),)

    def sumRange(self, a1, a2):
        """
        sum of elements nums[i..j], inclusive.
        """
        return self.accu[a2 + 1] - self.accu[a1]
