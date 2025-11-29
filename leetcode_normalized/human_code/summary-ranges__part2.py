class C1(object):

    def summaryRanges(self, a1):
        return [re.sub('->.*>', '->', '->'.join((repr(n) for v1, v2 in g))) for v1, v3 in itertools.groupby(enumerate(a1), lambda i_n: i_n[1] - i_n[0])]
