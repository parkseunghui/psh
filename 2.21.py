Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n= int(input("정수를 입력하시요: "))
정수를 입력하시요: 2
>>> bit_n=bin(n)
>>> print(f"{n}의 2진수 값: {bit_n}")
2의 2진수 값: 0b10
>>> bit_not = ~n
>>> bit_not = bin(bit_not)
>>> print(f"{n}의 2진수 값에 대한 비트단위 부정값: {bit_not}")
2의 2진수 값에 대한 비트단위 부정값: -0b11
