class C1(object):

    def reverseWords(self, a1):
        v1 = [word[::-1] for v2 in a1.split(' ')]
        return ' '.join(v1)
