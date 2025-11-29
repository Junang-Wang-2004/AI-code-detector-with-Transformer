class Solution:
    def toGoatLatin(self, S):
        terms = S.split()
        processed = []
        for position, term in enumerate(terms, start=1):
            if term[0] not in 'aeiouAEIOU':
                term = term[1:] + term[0]
            processed.append(term + 'ma' + 'a' * position)
        return ' '.join(processed)
