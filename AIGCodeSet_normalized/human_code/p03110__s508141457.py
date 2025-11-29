import array
from bisect import *
from collections import *
import fractions
import heapq
from itertools import *
import math
import random
import re
import string
import sys
v1 = 0
v2 = int(input())
for v3 in range(v2):
    v4, v5 = input().split()
    if v5 == 'JPY':
        v1 += int(v4)
    else:
        v1 += float(v4) * 380000.0
print('{:.9f}'.format(v1))
