import collections

class C1(object):

    def groupStrings(self, a1):
        v1 = collections.defaultdict(list)
        for v2 in a1:
            v1[self.hashStr(v2)].append(v2)
        v3 = []
        for v4, v5 in v1.items():
            v3.append(sorted(v5))
        return v3

    def hashStr(self, a1):
        v1 = ord(a1[0])
        v2 = ''
        for v3 in range(len(a1)):
            if ord(a1[v3]) - v1 >= 0:
                v2 += chr(ord('a') + ord(a1[v3]) - v1)
            else:
                v2 += chr(ord('a') + ord(a1[v3]) - v1 + 26)
        return v2
