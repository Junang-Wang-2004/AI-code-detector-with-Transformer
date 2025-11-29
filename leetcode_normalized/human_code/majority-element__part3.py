import collections

class C1(object):

    def majorityElement(self, a1):
        """
        """
        return sorted(list(collections.Counter(a1).items()), key=lambda a: a[1], reverse=True)[0][0]
