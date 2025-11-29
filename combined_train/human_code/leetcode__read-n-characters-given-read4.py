def f1(a1):
    global file_content
    v1 = 0
    while v1 < len(file_content) and v1 < 4:
        a1[v1] = file_content[v1]
        v1 += 1
    if len(file_content) > 4:
        v2 = v2[4:]
    else:
        v2 = ''
    return v1

class C1(object):

    def read(self, a1, a2):
        """
        """
        v1 = 0
        v2 = [''] * 4
        for v3 in range((a2 + 4 - 1) // 4):
            v4 = min(f1(v2), a2 - v1)
            a1[v1:v1 + v4] = v2[:v4]
            v1 += v4
        return v1
