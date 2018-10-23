### 숫자###

#정수 진법
# %d : 2진수
# %o : 8진수
# %x : 16진수
#숫자 표현 : 15를 각 진수로 변환하여 프린트
#표현 자릿수와 숫자의 개수가 동일해야한다.
print ("%d %x %o" % (15,15,15))
print ("%d" % (100))


# 진수 변환
#  2진수
print(bin(25))
#  8진수
print(oct(25))
#  16진수
print(hex(25))

#예제 1
sel=int(input("입력 진수 결정(16/10/8/2) : "))
num = int(input("값 입력 :"))

if sel == 16 :
    print("16진수 ==>",hex(num))
if sel == 10:
    print("10진수 ==>", num)
if sel == 8 :
    print("8진수 ==>",oct(num))
if sel == 2:
    print("2진수 ==>", bin(num))

#예제 2
#10
#16진수 0~9 & a~F
cnt = 0 #cycling 때문에 설정

while True:
    if cnt >= 5:
        break #if문에서 나가기
    num = input("16진수 한 글자를 입력 :")
    if len(num) != 1 :
        print("한글자를 입력하세요.")
        cnt = cnt+1 #6~7번 줄과 연계되서 5번만 cycling
        continue

    if (num >= '0' and num <='9') or (num >='a' and num <= 'f'):

        num10 = int(num, 16)
        print("10진수 ==>  %d" % num10)
        exit() #모든 함수 종료

    else:
        print("16 진수가 아닙니다.")





# 실수
# %f : 실수
# %5.2f : 5자리의 실수를 소수전 2자리수 까지 표현
print ("%f" % (56/3))
print ("%5.2f" % (56/3))

pi=3.14
print("{0:10.4f}".format(pi))
#10.4f : 10자리 숫자를 소숫점 4째짜리까지 표현하는 형식으로 표현하라
#    3.1400 : 앞 4자리가 비어있다.(10자리 숫자이기 때문)


#실수의 정수변형
f = 5.2
int(f)
#결과  5

#사칙연산
# a+b or a+=b  : 더하기
# a-b : 빼기
#a*b : 곱
#a**b : 거듭 제곱
# a%b : 나머지
print(7%4)

# a/b : 나누기
print(7/4)

# a//b :몫
print(7//4)

#4.2*10의 7승
a= 4.2E7

#4.2*10의 -7승
a= 4.2E-7

#몫과 나머지 예제 1
money = int(input("교환할 돈은 얼마? "))

c500=money//500
money = money % 500

c100 = money//100
money = money%100

c50 = money//50
money = money%50

c10 = money//10
money = money%10

print("500원 짜리 : %d 개" % c500)
print("100원 짜리 : %d 개" % c100)
print("50원 짜리 : %d 개" % c50)
print("10원 짜리 : %d 개" % c10)
print("나머지 갯수 : %d 원" % money)


