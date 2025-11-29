class Solution:
    def generateTag(self, caption):
        limit = 100
        parts = []
        terms = caption.split()
        if terms:
            parts.append(terms[0].lower())
            for term in terms[1:]:
                if term:
                    parts.append(term[0].upper() + term[1:].lower())
        combined = '#' + ''.join(parts)
        return combined[:limit]
