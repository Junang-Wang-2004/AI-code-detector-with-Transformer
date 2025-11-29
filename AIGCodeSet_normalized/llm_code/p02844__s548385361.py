from itertools import combinations

def f1():
    v1 = int(input())
    v2 = input()
    v3 = set()
    for v4, v5, v6 in combinations(range(v1), 3):
        v3.add(''.join([v2[v4], v2[v5], v2[v6]]))
    print(len(v3))
if __name__ == '__main__':
    f1()
