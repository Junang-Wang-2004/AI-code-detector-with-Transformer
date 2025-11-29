from collections import Counter
input()
print(sum((j if i > j else j - i for v1, v2 in Counter(map(int, input().split())).items())))
