'''
람다 함수
'''
# 익명 함수, 람다 표현식

def plus_one(x):
    return x+1
print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))

plus = lambda x, y: x+y
print(plus(3, 2))

a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(plus_two, a)))
print(list(map(lambda x: x+3, a)))