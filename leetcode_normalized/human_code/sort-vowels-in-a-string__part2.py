class C1(object):

    def sortVowels(self, a1):
        """
        """
        v1 = 'AEIOUaeiou'
        v2 = set(v1)
        v3 = [x for v4 in a1 if v4 in v2]
        v3.sort(reverse=True)
        return ''.join((v3.pop() if v4 in v2 else v4 for v4 in a1))
