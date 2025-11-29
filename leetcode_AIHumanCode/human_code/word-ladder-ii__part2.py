# Time:  O(b^d), b is the branch factor of bfs, d is the result depth
# Space: O(w * l), w is the number of words, l is the max length of words
class Solution2(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        """
        dictionary = set(wordList)
        result, cur, visited, found, trace = [], [beginWord], set([beginWord]), False, defaultdict(list)

        while cur and not found:
            for word in cur:
                visited.add(word)

            next = set()
            for word in cur:
                for i in range(len(word)):
                    for c in ascii_lowercase:
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate not in visited and candidate in dictionary:
                            if candidate == endWord:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next

        if found:
            self.backtrack(result, trace, [], endWord)

        return result

    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            path.append(word)
            result.append(path[::-1])
            path.pop()
        else:
            for prev in trace[word]:
                path.append(word)
                self.backtrack(result, trace, path, prev)
                path.pop()
