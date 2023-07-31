# 숫자만 추출
# 첫 줄에 자연수를 출력, 두 번째 줄에 약수의 개수 출력
str = "g0en2Ts8eSoft"
num = ""
for s in str:
    if s.isdigit():
        num += s
number = int(num)
print(number)
cnt = 0
for i in range(1, number+1):
    if number%i==0:
        cnt+=1
print(cnt)