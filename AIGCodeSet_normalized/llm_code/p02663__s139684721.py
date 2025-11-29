v1 = int(input('Enter WakeUp Hour: '))
v2 = int(input('Enter WakeUp Minute: '))
v3 = int(input('Enter Sleep Hour: '))
v4 = int(input('Enter Sleep Minute: '))
v5 = int(input('Study time: '))
v6 = v3 * 60 + v4 - (v1 * 60 + v2)
if v6 > v5:
    print('You can finish the study')
    v7 = (v3 * 60 + v4 - v5) % 60
    v8 = (v3 * 60 + v4 - v5) // 60
    print('Start before: ', v8, ':', v7)
else:
    print('You are lazy!!!. Wake up early')
