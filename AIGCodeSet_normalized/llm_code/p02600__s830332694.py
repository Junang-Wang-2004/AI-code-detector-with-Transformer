try:
    v1 = int(input())
    if 400 <= v1 <= 599:
        print(8)
    elif 600 <= v1 < 800:
        print(7)
    elif 800 <= v1 < 1000:
        print(6)
    elif 1000 <= v1 < 1200:
        print(5)
    elif 1200 <= v1 < 1400:
        print(4)
    elif 1400 <= v1 < 1600:
        print(3)
    elif 1600 <= v1 < 1800:
        print(2)
    elif 1800 <= v1 <= 1999:
        print(1)
except EOFError:
    print('')
except Exception as v2:
    print(v2)
