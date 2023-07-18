'''
함수 만들기
'''

# def add(a, b):
#     return a+b

# return값이 여러개면 튜플로 반환이 됨.
# def add(a, b):
#     c=a+b
#     d=a-b
#     return c, d
# print(add(3,2))

# 솟수만 출력하는 함수
def isPrime(x):
    for i in range(2, x):
        if x%i ==0:
            return False
    return True

a=[12, 13, 7, 9, 19]

for x in a:
    if isPrime(x):
        print(x, end=' ')
