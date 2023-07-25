# 자릿수의 합
# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 
# 그 합이 최대인 자연수를 출력

def digit_sum(x):
    sum = 0
    while True:
        if x == 0:
            break
        else:
            temp = x//10
            sum += x%10
            x = temp
    return sum

NUM = "125 15232 97 4569 12 64949 9999"
num = list(map(int, NUM.split()))
max =0
for i in num:
    sum = digit_sum(i)
    if max < sum:
        max = sum
        result = i
print(result)

