Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #6.7
>>> n_list = [10,20,30,50,60]
>>> total = 0
>>> 
>>> for num in n_list:
...     total = total + num
... 
...     
>>> print('리스트 원소들: ', n_list)
리스트 원소들:  [10, 20, 30, 50, 60]
>>> print('리스트 원소들의 합: ', total)
리스트 원소들의 합:  170
>>> #6.9
>>> def max(n_list):
...     a = n_list[0]
...     for num in n_list:
...         if num > a:
...             a = num
...     return a
... 
>>> n_list = [10,20,30,50,60]
>>> print('리스트의 원소들:', n_list)
리스트의 원소들: [10, 20, 30, 50, 60]
>>> print('리스트의 최댓값:',max(n_list))
리스트의 최댓값: 60
>>> #6.11
>>> import math
>>> 
>>> n=int(input('n을 입력하세요: '))
n을 입력하세요: 10
>>> n_list = list(map(int, input('10개의 수를 입력하세요: ').split()))
10개의 수를 입력하세요: 45 67 20 34 2 100 23 45 67 89
>>> mean = sum(n_list)/n
>>> variance = sum((x-mean)**2 for x in n_list)/n
>>> std_dev = math.sqrt(variance)
>>> print('합:', sum(n_list))
합: 492
>>> print('평균:', mean)
평균: 49.2
>>> print('표준편차:', round(std_dev, 2))
표준편차: 29.72
