# 회문 문자열 검사
# 앞으로 읽나 뒤로 읽나 같은 문자열을 검사
# 대,소문자 구분 안함.
# level, lol  ...

n = 5
input = "level moon abcba soon gooG"
text = list(input.split())
for s in text:
    str=s.upper()
    size=len(str)
    for j in range(size//2):
        if str[j] != str[-1-j]: #  -1 - j 끝에서부터 인덱스
            print("NO")
            break
    else: #포문 정상 종료시..
        print("YES")
