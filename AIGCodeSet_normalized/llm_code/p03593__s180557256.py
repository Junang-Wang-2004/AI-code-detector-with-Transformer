def f1():
    v1 = open(0).readlines()
    v2, v3 = map(int, v1[0].split())
    v4 = [list(map(lambda x: x.strip(), v1[1:]))]
    v5 = []
    for v6 in v4:
        v7 = [0] * 26
        for v8 in v6:
            v7[ord(v8) - ord('a')] += 1
        v5.append(v7)
    if v3 % 2 == 0:
        if all((all((x % 2 == 0 for v9 in b)) for v10 in v5)):
            v7 = []
        else:
            return 'No'
    else:
        v7 = [[i for v11, v9 in enumerate(v10) if v9 % 2 != 0] for v10 in v5]
        if all((len(v8) == 1 for v8 in v7)):
            v5 = [[v9 if v9 % 2 == 0 else v9 - 1 for v9 in v10] for v10 in v5]
            v7 = Counter([v8[0] for v8 in v7]).values()
        else:
            return 'No'
    v7
    v12 = Counter(map(tuple, v5)).values()
    if v2 % 2 == 0:
        if all((v8 % 2 == 0 for v8 in v7)) and all((d % 2 == 0 for v13 in v12)):
            return 'Yes'
    elif sum((v8 % 2 for v8 in v7)) <= 1 and sum((v13 % 2 for v13 in v12)) <= 1:
        return 'Yes'
    return 'No'
print(f1())
