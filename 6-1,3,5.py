Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#6.1
#40,60,30,60,70,70,90,20,7
list_ex = [10,20,30,40,50,60,70]
high = 5
low = 3
list_ex[low]
40
list_ex[low+2]
60
list_ex[high-low]
30
list_ex[low-high]
60
list_ex[-1]
70
list_ex[-low]
50
list_ex[2 * 3]
70
list_ex[2]*3
90
list_ex[5%4]
20
len(list_ex)
7
#6.3
list1 = [3,5,7]
list2 = [2,3,4,5,6]
for num1 in list1:
    for num2 in list2:
        print(num1, '*', num2, '=', num1 * num2)

        
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
>>> #6.5
>>> list1 = ['I like', 'I love']
>>> list2 = ['pancakes.', 'kiwi juice.', 'espresso']
>>> for n in list1:
...     for a in list2:
...         print(n,a)
... 
...         
I like pancakes.
I like kiwi juice.
I like espresso
I love pancakes.
I love kiwi juice.
I love espresso
>>> #6.7
>>> n_list=[10,20,30,50,60]
>>> total = 0
>>> for num in list:
...     total = total + num
... print('리스트 원소들:', n_list)
SyntaxError: invalid syntax
>>> n_list=[10,20,30,50,60]
>>> total = 0
>>> for num in n_list:
...     total = total + num
...     print('리스트 원소들 :',n_list)
...     print('리스트 원소들의 합 :',total)
... 
...     
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 10
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 30
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 60
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 110
리스트 원소들 : [10, 20, 30, 50, 60]
리스트 원소들의 합 : 170
