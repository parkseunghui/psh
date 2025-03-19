Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#2.1
print(100,'+',200,'=',100+200)
100 + 200 = 300
print(200,'+',300,'+',400,'=',200+300+400)
200 + 300 + 400 = 900
#2.2
width = 30
height = 60
print(width)
30
print(height)
60
#2.3
#get_rect_area.py
width = 30
height = 60
area = width*height
print('사각형의 면적:',area)
사각형의 면적: 1800
#2.4
#get_triangle_area.py
width=40
height=20
area=width*height*0.5
print('삼각형의 면적:',area)
삼각형의 면적: 400.0
#2.5
width=int(input('정사각형의 밑변을 입력하시오 : '))
정사각형의 밑변을 입력하시오 : 40
area = width**2
print('정사각형의 면적 : ',area)
정사각형의 면적 :  1600
#2.6
print('1에서 10까지의 합 : ',1+2+3+4+5+6+7+8+9+10)
1에서 10까지의 합 :  55
#2.7
print('10! =',1*2*3*4*5*6*7*8*9*10)
10! = 3628800
#2.8
print("a n a**n")
a n a**n
for a in range(2,7):
    n=2
    print(f"{a}    {n}     {a**n}")

    
2    2     4
3    2     9
4    2     16
5    2     25
6    2     36
#2.9
print("섭씨   화씨")
섭씨   화씨
for celsius in range(0,51,10):
     fahrenheit = (9/5) * celsius +32
     print(f"{celsius}   {fahrenheit}")

     
0   32.0
10   50.0
20   68.0
30   86.0
40   104.0
50   122.0
#2.10
cel = int(input("섭씨 온도를 입력하세요: "))
섭씨 온도를 입력하세요: 30
fah = (9/5) * cel +32
print(f"섭씨는 {cel} 도는 화씨 {fah}도 입니다.")
섭씨는 30 도는 화씨 86.0도 입니다.
#2.11
fah = int(input("화씨 온도를 입력하세요 :" ))
화씨 온도를 입력하세요 :86
cel = (5 / 9) * (fah - 32)
print(f"화씨 {fah} 도는 섭씨 {cel} 도 입니다.")
화씨 86 도는 섭씨 30.0 도 입니다.
#2.12
radius = 11
PI = 3.141592
circumference = 2 * PI * radius
area = PI * (radius ** 2)
print(f"원의 반지름 = {radius}, 원의 둘레 = {circumference}, 원의 면적 = {area}")
원의 반지름 = 11, 원의 둘레 = 69.115024, 원의 면적 = 380.132632
#2.13
PI=3.141592
radius = int(input("원의 반지름을 입력하세요: "))
원의 반지름을 입력하세요: 11
circumference = 2 * PI * radius
area = PI *(radius**2)
print(f"원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.15f}")
원의 둘레 = 69.115024, 원의 면적 = 380.132632000000001
#2.15
a = int(input("밑변을 입력하세요: "))
밑변을 입력하세요: 5
b = int(input("높이를 입력하세요: "))
높이를 입력하세요: 12
c = (a**2 + b**2) ** 0.5
print(f"빗변: {c:.1f}")
빗변: 13.0
#2.17
for i in range(10):
    print(2 << i, end=' ')

    
2 4 8 16 32 64 128 256 512 1024 
#2.18
n= int(input("정수를 입력하세요: "))
정수를 입력하세요: 20
even = (n % 2 == 0)
print("이 수가 짝수인가요?", even)
이 수가 짝수인가요? True
n=int(input("정수를 입력하세요: "))
정수를 입력하세요: 21
even = (n % 2 == 0)
print("이 수가 짝수인가요?", even)
이 수가 짝수인가요? False
#2.19
n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    n = int(input("정수를 입력하세요: "))
ValueError: invalid literal for int() with base 10: ''

#2.21
n= int(input("정수를 입력하시요: "))
정수를 입력하시요: 2
bit_n=bin(n)
print(f"{n}의 2진수 값: {bit_n}")
2의 2진수 값: 0b10
>>> bit_not = ~n
>>> bit_not = bin(bit_not)
>>> print(f"{n}의 2진수 값에 대한 비트단위 부정값: {bit_not}")
2의 2진수 값에 대한 비트단위 부정값: -0b11
>>> #2.22
>>> a = int(input("정수 a를 입력하시오 : "))
정수 a를 입력하시오 : 202
>>> b = int(input("정수 b를 입력하시오 : "))
정수 b를 입력하시오 : 50
>>> m = a//b
>>> n = a%b
>>> print("a / b의 몫:", m)
a / b의 몫: 4
>>> print("a / b의 나머지:", n)
a / b의 나머지: 2
>>> #2.23
>>> n = int(input("세 자리 정수를 입력하시오 : "))
세 자리 정수를 입력하시오 : 349
>>> a = n //100
>>> b = (n % 100) //10
>>> c = n % 10
>>> print("백의 자리:",a)
백의 자리: 3
>>> print("십의 자리:",b)
십의 자리: 4
>>> print("일의 자리:",c)
일의 자리: 9
>>> #2.24
>>> n = int(input("세 자리 정수를 입력하시오: "))
세 자리 정수를 입력하시오: 349
>>> a = n//100
>>> b = (n//10)%10
>>> c = n%10
>>> print(c)
9
>>> print(b)
4
>>> print(a)
3
