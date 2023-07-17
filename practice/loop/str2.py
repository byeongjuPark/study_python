import random as r

'''
문자열과 내장함수2
'''

#리스트 만들기
a=[]
print(a)
b=list()
print(b)

a=[1,2,3,4,5]
print(a)
print(a[0])


b=list(range(1, 11))
print(b)

for x in b:
    print(x, end=' ')
print()

#리스트 합치기
c = a + b
print(c)

#리스트 값 추가
a.append(6)
print(a)
# 특정 Index 지점에 값 넣기
# a[3]에 7을 넣음, 뒷 값은 밀려남
a.insert(3, 7)
print(a)

# 리스트 뒤에서 하나 뺌
a.pop()
print(a)

# 해당 Index값을 뺌
popdata = a.pop(3)
print(a)
print(popdata)

# 4의 값을 가진걸 지움
a.remove(4)
print(a)

# 5라는 값의 Index 번호를 리턴함
print(a.index(5))

a=list(range(1,11))
print(a)

# sum(a) -> a라는 list의 값을 다 합해줌.
print(sum(a))
# max(a) -> a라는 list의 값중 가장 큰 값
print(max(a))
# min(a) -> 가장 작은 값
print(min(a))
# 인자 값 들 중에서 최소 값을 찾아줌.
print(min(7, 5))
print(min(7, 3, 5))
print(a)

# 리스트 섞기 
r.shuffle(a)
print(a)
# 내림차순 정렬
a.sort(reverse=True)
print(a)
# 오름차순 정렬
a.sort()
print(a)
# 리스트 초기화
a.clear()
print(a)