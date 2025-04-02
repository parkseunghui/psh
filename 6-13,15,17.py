Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n_list = list(map(int,input('5개의 정수를 입력하세요:').split()))
5개의 정수를 입력하세요:45 67 20 34 2
>>> sum_nlist = sum(n_list)
>>> average = sum(n_list)/len(n_list)
>>> max_nlist = max(n_list)
>>> min_nlist = min(n_list)
>>> print('합',sum_nlist)
합 168
>>> print('합 :', sum_nlist)
합 : 168
>>> print('평균 :', average)
평균 : 33.6
>>> print('최댓값 :', max_nlist)
최댓값 : 67
>>> print('최솟값 :', min_nlist)
최솟값 : 2
>>> 
>>> #6.15
>>> greet = 'Have a beautiful day.'
>>> greet[0:1]
'H'
>>> greet[0:4]
'Have'
>>> greet[5:8]
'a b'
>>> greet[8:8]
''
>>> greet[8:16]
'eautiful'
>>> greet[7:16]
'beautiful'
>>> greet[18:20]
'ay'
>>> greet[17:20]
'day'
>>> #6.17
>>> animals = ['dog', 'cat', 'tiger', 'lion']
>>> print('animals =', animals)
animals = ['dog', 'cat', 'tiger', 'lion']
>>> animals.append(animals.pop(0))
>>> print('animals =', animals)
animals = ['cat', 'tiger', 'lion', 'dog']
>>> #6.19
>>> s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
>>> new_s_list = []
>>> for a in s_list:
...     if a in new_s_list:
        continue
    new_s_list.append(item)

    
Traceback (most recent call last):
  File "<pyshell#33>", line 4, in <module>
    new_s_list.append(item)
NameError: name 'item' is not defined. Did you mean: 'iter'?
import warnings
warnings.filterwarning('ignore')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    warnings.filterwarning('ignore')
AttributeError: module 'warnings' has no attribute 'filterwarning'. Did you mean: 'filterwarnings'?
