import collections

class C1(object):

    def findRepeatedDnaSequences(self, a1):
        """
        """
        dict, v1, v2 = ({}, 0, [])
        for v3 in range(len(a1)):
            v1 = v1 << 3 & 1073741823 | ord(a1[v3]) & 7
            if v1 not in dict:
                dict[v1] = True
            elif dict[v1]:
                v2.append(a1[v3 - 9:v3 + 1])
                dict[v1] = False
        return v2

    def findRepeatedDnaSequences2(self, a1):
        """
        """
        v1, v2 = ([], [])
        if len(a1) < 10:
            return []
        for v3 in range(len(a1) - 9):
            v1.extend([a1[v3:v3 + 10]])
        return [k for v4, v5 in list(collections.Counter(v1).items()) if v5 > 1]
