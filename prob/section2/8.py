# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램

N=20
cnt = 0
ch = [0]*(N+1)
for i in range(2, N+1):
    if ch[i] == 0:
        cnt +=1
        for j in range(i, N+1, i):
            ch[j]=1

print(cnt)