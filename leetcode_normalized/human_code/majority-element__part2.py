import collections

class C1(object):

    def majorityElement(self, a1):
        """
        """
        return collections.Counter(a1).most_common(1)[0][0]
