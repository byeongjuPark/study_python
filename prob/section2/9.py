# 뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 출력

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True


N = 5
input = "32 55 62 3700 250"
a = list(map(int, input.split()))
for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")