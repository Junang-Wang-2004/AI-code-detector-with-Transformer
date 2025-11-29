class Solution:
    def minimumLengthEncoding(self, words):
        terms = list(set(words))
        root = {}
        endings = []
        for term in terms:
            current = root
            for char in reversed(term):
                if char not in current:
                    current[char] = {}
                current = current[char]
            endings.append(current)
        return sum(len(term) + 1 for term, ending in zip(terms, endings) if not ending)
