Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#4.1
for i in range(1,10):
    print('2 *', i, '=', 2 * i)

    
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
i=1
while i<10:
    print('2 *', i, '=', 2 * i)
    i+=1

    
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
#4.3
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')

    
Python 
is 
FUN! 
Python 
is 
FUN! 
Python 
is 
FUN! 
for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')
SyntaxError: invalid syntax
for i in range(3):
    print('Python ')
print('is ')
SyntaxError: invalid syntax
print('FUN! ')
FUN! 
#4.5
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.
print('-햄버거(입력 b)')
-햄버거(입력 b)
print('-치킨(입력 c)')
-치킨(입력 c)
print('-피자(입력 p)')
-피자(입력 p)
while True:
    menu = input('메뉴를 선택하세요(알파벳 b,c,p 입력) : ')
    if menu == 'b':
        print('햄버거를 선택하였습니다.')
        break
    elif menu == 'c':
        print('치킨을 선택하였습니다.')
        break
    elif menu == 'p':
        print('피자를 선택하였습니다.')
        break
    else:
        print('메뉴를 다시 입력하세요(알파벳 b,c,p 입력) : ')

        
메뉴를 선택하세요(알파벳 b,c,p 입력) : x
메뉴를 다시 입력하세요(알파벳 b,c,p 입력) : 
메뉴를 선택하세요(알파벳 b,c,p 입력) : c
치킨을 선택하였습니다.
#4.7
n = int(input("숫자를 입력하세요 : "))
숫자를 입력하세요 : 5
if n < 2:
    print(n, "는 소수가 아닙니다.")
else:
    is_prime = True
    if n % 2 == 0 and n != 2:
        is_prime = False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        print(n, "는 소수입니다.")
    else:
        print(n, "는 소수가 아닙니다.")

        
5 는 소수입니다.
#4.9
n = int(input('숫자를 입력하세요 : '))
숫자를 입력하세요 : 10
total = 0
for i in range(1,n+1):
    total += 1
    print('결과는' total '입니다.')
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?

#4.11
depth = 30
climb = 7
slide = 5
position =0
days=0
while True:
    days += 1
    position += climb
    if position >=depth:
        print('우물을 탈출하는데 걸린 날은', days,'일입니다.')
        break
    position -= slide

    
우물을 탈출하는데 걸린 날은 13 일입니다.
#4.13
armstrong = []
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    sumsum=hundreds**3 + tens**3 + units**3
    if num == sumsum:
        armstrong.append(str(num))
        print('세 자리의 암스트롱 수 :', ''.join(armstrong))

        
세 자리의 암스트롱 수 : 153
세 자리의 암스트롱 수 : 153370
세 자리의 암스트롱 수 : 153370371
세 자리의 암스트롱 수 : 153370371407
#4.15
fuel = 500
running = True
while running:
    user_input = input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: ")
    if user_input.startswith('+'):
        num_part = user_input[1:]
        if num_part.isdigit():
            fuel += int(num_part)
        else:
            print("잘못된 숫자 형식입니다.")
    elif user_input.startswith('-'):
        num_part = user_input[1:]
        if num_part.isdigit():
            fuel -= int(num_part)
        else:
            print("잘못된 숫자 형식입니다.")
...     else:
...         print("+ 또는 - 기호로 시작해야 합니다.")
...     print('현재 탱크양은', fuel, '입니다.')
...     if fuel < 50:
...         print('경고 : 연료가 10% 미만이니 충전하세요!')
...         running = False
... 
...         
충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: +200
현재 탱크양은 700 입니다.
충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: abc
+ 또는 - 기호로 시작해야 합니다.
현재 탱크양은 700 입니다.
충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: -650
현재 탱크양은 50 입니다.
충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: -1
현재 탱크양은 49 입니다.
경고 : 연료가 10% 미만이니 충전하세요!
>>> #4.17
>>> def funtion(n):
...     if n == 1:
...         return 0
...     sum_div = 1
...     for i in range(2, int(n**0.5) + 1):
...         if n % i == 0:
...             sum_div += i
...             other_div = n // i
...             if other_div != i:
...                 sum_div += other_div
...     return sum_div
... found_pairs = set()
SyntaxError: invalid syntax
>>> for a in range(2, 20001):
...     if a in found_pairs:
...         continue
...     b = sum_proper_divisors(a)
...     if b > a:
...         if sum_proper_divisors(b) == a:
...             found_pairs.add(a)
...             found_pairs.add(b)
...             print(f"{a}의 친화수 {b}")
...             print(f"{b}의 친화수 {a}")
... 
...             
Traceback (most recent call last):
  File "<pyshell#139>", line 2, in <module>
    if a in found_pairs:
NameError: name 'found_pairs' is not defined
