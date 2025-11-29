class C1(object):

    def partition(self, a1):
        """
        """
        v1 = []
        self.partitionRecu(v1, [], a1, 0)
        return v1

    def partitionRecu(self, a1, a2, a3, a4):
        if a4 == len(a3):
            a1.append(list(a2))
        else:
            for v1 in range(a4, len(a3)):
                if self.isPalindrome(a3[a4:v1 + 1]):
                    a2.append(a3[a4:v1 + 1])
                    self.partitionRecu(a1, a2, a3, v1 + 1)
                    a2.pop()

    def isPalindrome(self, a1):
        for v1 in range(len(a1) / 2):
            if a1[v1] != a1[-(v1 + 1)]:
                return False
        return True
