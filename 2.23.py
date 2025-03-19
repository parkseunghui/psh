Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
