from functools import reduce
from operator import and_
v1 = int(input())
v2 = reduce(and_, [i % 3 == 0 or i % 5 == 0 for v3 in map(int, input().split()) if v3 % 2 == 0])
print('APPROVED' if v2 else 'DENIED')
