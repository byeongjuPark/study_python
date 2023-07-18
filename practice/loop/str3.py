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

# x를 tuple로
# 튜플은 값 변경이 불가능
for x in enumerate(a):
    print(x)
    print(x[0], end= ', ')
    print(x[1])
print()

for index, value in enumerate(a):
    print(index, value) 
print()

# all() 모두가 다 참이여야 true 반환
if all(60>x for x in a):
    print("YES")
else:
    print("NO")

# any 한번이라도 참이면 true
if any(60>x for x in a):
    print("YES")
else:
    print("NO")