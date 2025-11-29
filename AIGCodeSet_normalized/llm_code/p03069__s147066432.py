import re
v1 = int(input())
v2 = input()
if not '#' in v2:
    print(0)
else:
    v2 = '#' + v2.split('#', 1)[-1]
    v3 = re.search(re.compile('#+$'), v2)
    if v3:
        v2 = v2[:v3.start()]
    print(min(v2.count('.'), v2.count('#')))
