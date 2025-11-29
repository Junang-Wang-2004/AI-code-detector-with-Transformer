def f1(a1, a2):
    if a1 == a2:
        return 0
    if abs(a1) > abs(a2):
        return abs(a1) - abs(a2)
    else:
        return abs(a2) - abs(a1)
