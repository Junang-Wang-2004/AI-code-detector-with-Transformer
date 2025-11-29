a, b = map(int, raw_input().strip().split())
diff = b - a
print sum([i for i in xrange(1, diff)]) - a
