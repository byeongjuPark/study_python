'''
문자열과 내장함수3
'''

a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

