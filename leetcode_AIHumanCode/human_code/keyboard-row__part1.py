# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findWords(self, words):
        """
        """
        rows = [set(['q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p']),
                set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']),
                set(['z', 'x', 'c', 'v', 'b' ,'n', 'm'])]

        result = []
        for word in words:
            k = 0
            for i in range(len(rows)):
                if word[0].lower() in rows[i]:
                    k = i
                    break
            for c in word:
                if c.lower() not in rows[k]:
                    break
            else:
                result.append(word)
        return result


