def f1(a1, a2, a3, a4, a5):
    if a1 == a3:
        return True
    if a2 == a4:
        return False
    if a2 > a4:
        return (a3 - a1) % (a2 - a4) == 0
    else:
        return (a1 - a3) % (a4 - a2) == 0
