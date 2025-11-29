def f1(a1):
    if a1 // 10 == 9:
        print('Yes')
    elif a1 % 10 == 9:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    while True:
        try:
            v1 = int(input('2桁の整数Nを入力してください。:'))
            if 10 <= v1 and v1 <= 99:
                break
            else:
                print('入力された整数が2桁の整数ではありません。')
                print('-----------------------------------------')
                continue
        except ValueError:
            print('2桁の整数Nを正しく入力してください。')
            print('-----------------------------------------')
    print(' ######## Result ######## ')
    f1(v1)
