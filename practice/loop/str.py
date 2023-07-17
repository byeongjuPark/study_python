import random as r

'''
문자열과 내장함수
'''
msg = "It is Time"
#대문자, 소문자로 변환 
print(msg.upper())
print(msg.lower())
tmp=msg.upper()
print(tmp)

#find -> 처음 나오는 T에 Index를 반환
print(tmp.find('T'))
#count -> 'T'의 개수를 반환
print(tmp.count('T'))
#slice -> 0번부터 2개 -> [0], [1]
print(tmp[:2]) # --> IT
print(tmp[3:5]) #--> IS
#len -> 문자열의 길이, 공백 포함
print(len(tmp))

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

#msg의 문자 한개한개를 접근
for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.upper()==x:
        if x != ' ':
            print(x, end=' ')
print()

# isupper -> 대문자일 경우 참
for x in msg:
    if x.isupper(): 
            print(x, end=' ')
print()
# islower -> 소문자일 경우 참
for x in msg:
    if x.islower(): 
            print(x, end=' ')
print()

#isalpha -> 알파벳만 출력
for x in msg:
    if x.isalpha(): 
            print(x, end=' ')
print()

#ord -> 문자 -> 아스키코드
tmp='AZ'
for x in tmp:
    print(ord(x))
tmp='az'
for x in tmp:
    print(ord(x))

#chr -> 아스키코드 -> 문자
tmp = 65
print(chr(tmp))
print()

# 문장화 s.title()
s = '3PeOple UnFOllowed ME'
print(s.title())
print(s.lower().title())

# capitalize() 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
s = '3People'
print(s.capitalize())