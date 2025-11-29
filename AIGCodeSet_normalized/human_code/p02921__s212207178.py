import sys
input = sys.stdin.readline

class C1:

    def main(self):
        v1 = input().rstrip()
        v2 = input().rstrip()
        v3 = 0
        for v4, v5 in enumerate(v1):
            if v5 == v2[v4]:
                v3 += 1
        print(v3)
if __name__ == '__main__':
    C1().main()
