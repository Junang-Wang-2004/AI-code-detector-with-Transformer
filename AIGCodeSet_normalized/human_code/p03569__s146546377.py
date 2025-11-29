s = raw_input()

replaced = s.replace('x', '')
l = len(replaced)
halfl = int(l / 2)

if l > 1 and replaced[:halfl] != replaced[-halfl:][::-1]:
  print "-1"
  exit()

xset = {}
i = 0
for c in s:
  if c == 'x':
    d = min(i, l-i)
    if i != l-i:
      xset[d] = xset.get(d, 0) + [-1, 1][i < l-i]
  else:
    i += 1

ans = 0
for v in xset.itervalues():
  ans += abs(v)
print ans
