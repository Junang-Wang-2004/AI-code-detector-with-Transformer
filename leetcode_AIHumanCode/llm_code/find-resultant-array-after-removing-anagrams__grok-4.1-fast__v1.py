def removeAnagrams(words):
    res = []
    i = 0
    N = len(words)
    while i < N:
        res.append(words[i])
        j = i + 1
        while j < N and sorted(words[j]) == sorted(words[i]):
            j += 1
        i = j
    return res
