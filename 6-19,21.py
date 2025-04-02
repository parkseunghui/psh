Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #6.19
>>> s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
>>> new_s_list = []
>>> for a in s_list:
...     if a in new_s_list:
...         continue
...     new_s_list.append(a)
... 
...     
>>> print('s_list =', s_list, 'new_s_list =', new_s_list)
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq'] new_s_list = ['abc', 'bcd', 'abba', 'cddc', 'opq']
>>> #6.21
>>> def solve(a):
...     result = []
...     i = 0
...     n = len(a)
... 
...     
>>> def slove(a):
...     result = []
...     i = 0
...     n = len(a)
...     while i <n:
...         char
... 
...         
>>> s = 'a2b3c6a2c3f1g1'
>>> result = ''.join([s[i]*int(s[i+1]) for i in range(0, len(s), 2)])
>>> print(f"src = '{s}'")
src = 'a2b3c6a2c3f1g1'
>>> print(f"output = '{result}'")
output = 'aabbbccccccaacccfg'
>>> #6.23
>>> def person(p_list):
...     return len(p_list) // 5
... p1 = ['온달', 20,1,180.0,100.0]
SyntaxError: invalid syntax
>>> person1 = ['온달', 20,1,180.0,100.0]
>>> person2 = ['이사부', 25,1,170.0,70.0]
>>> person3 = ['평강', 22,0,169.0,60.0]
>>> person4 = ['학거세', 40,1,150.0,50.0]
