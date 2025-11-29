v1, v2, *v3 = map(int, open(0).read().split())
from math import *
print(max(0, (max(v3) - ceil(v1 / 2)) * 2 - 1))
