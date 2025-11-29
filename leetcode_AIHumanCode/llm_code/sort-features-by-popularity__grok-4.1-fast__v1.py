class Solution:
    def sortFeatures(self, features, responses):
        count = {f: 0 for f in features}
        for reply in responses:
            words = set(reply.split())
            for w in words:
                if w in count:
                    count[w] += 1
        indexed = [(f, i) for i, f in enumerate(features)]
        indexed.sort(key=lambda p: (-count[p[0]], p[1]))
        return [p[0] for p in indexed]
