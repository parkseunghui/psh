Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def how_many_persons(person_list):
...     return len(person_list) // 5
... 
>>> person1 = ['온달', 20, 1, 180.0, 100.0]
>>> person2 = ['이사부', 25, 1, 170.0, 70.0]
>>> person3 = ['평강', 22, 0, 169.0, 60.0]
>>> person4 = ['학거세', 40, 1, 150.0, 50.0]
>>> 
>>> person_list = person1 + person3 + person4
>>> n_persons = how_many_persons(person_list)
>>> print(str(n_persons) + '명의 정보가 담겨 있습니다.')
3명의 정보가 담겨 있습니다.
>>> 
>>> def compute_average_age(person_list):
...     ages = person_list[1::5]
...     return sum(ages) / len(ages)
... 
>>> average_age = compute_average_age(person_list)
>>> print('평균 나이는 ' + str(average_age) + '세입니다.')
평균 나이는 27.333333333333332세입니다.
>>> person_list = person1 + person2 + person3 + person4
>>> average_age = compute_average_age(person_list)
>>> print('평균 나이는 ' + str(average_age) + '세입니다.')
평균 나이는 26.75세입니다.
>>> 
>>> def count_males_females(person_list):
...     genders = person_list[2::5]
...     n_male = sum(genders)
...     n_female = len(genders) - n_male
...     return n_male, n_female
... 
>>> person_list = person1 + person2 + person3 + person4
>>> n_male, n_female = count_males_females(person_list)
>>> print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')
리스트에는 남자가 3 명, 여자가 1 명입니다.
>>> 
>>> def display_persons(person_list):
...     for i in range(0, len(person_list), 5):
...         print(person_list[i:i+5])
... 
>>> person_list = person1 + person2 + person3 + person4
>>> display_persons(person_list)
['온달', 20, 1, 180.0, 100.0]
['이사부', 25, 1, 170.0, 70.0]
['평강', 22, 0, 169.0, 60.0]
['학거세', 40, 1, 150.0, 50.0]
