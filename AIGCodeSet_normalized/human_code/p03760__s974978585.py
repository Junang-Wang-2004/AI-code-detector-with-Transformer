a=raw_input()
b=raw_input()
l=''
for i in range(len(a)):
    l+=a[i]
    if i<len(b):
        l+=b[i]
print l
