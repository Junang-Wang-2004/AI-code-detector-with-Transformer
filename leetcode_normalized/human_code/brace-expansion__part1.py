import itertools

class C1(object):

    def expand(self, a1):
        """
        """

        def form_words(a1):
            v1 = list(map(''.join, itertools.product(*a1)))
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
