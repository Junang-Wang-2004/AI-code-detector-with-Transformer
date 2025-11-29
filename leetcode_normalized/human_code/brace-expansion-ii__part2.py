import itertools

class C1(object):

    def braceExpansionII(self, a1):
        """
        """

        def form_words(a1):
            v1 = []
            v2 = 1
            for v3 in a1:
                v2 *= len(v3)
            for v4 in range(v2):
                v5 = []
                for v3 in reversed(a1):
                    v4, v6 = divmod(v4, len(v3))
                    v5.append(v3[v6])
                v5.reverse()
                v1.append(''.join(v5))
            v1.sort()
            return v1

        def generate_option(a1, a2):
            v1 = set()
            while a2[0] != len(a1) and a1[a2[0]] != '}':
                a2[0] += 1
                for v2 in generate_words(a1, a2):
                    v1.add(v2)
            a2[0] += 1
            v2 = list(v1)
            v2.sort()
            return v2

        def generate_words(a1, a2):
            v1 = []
            while a2[0] != len(a1) and a1[a2[0]] not in ',}':
                v2 = []
                if a1[a2[0]] not in '{,}':
                    v2.append(a1[a2[0]])
                    a2[0] += 1
                elif a1[a2[0]] == '{':
                    v2 = generate_option(a1, a2)
                v1.append(v2)
            return form_words(v1)
        return generate_words(a1, [0])
