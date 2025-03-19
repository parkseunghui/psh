Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("섭씨   화씨")
섭씨   화씨
>>> for celsius in range(0,51,10):
...     fahrenheit = (9/5) * celsius +32
...     print(f"{celsius}   {fahrenheit}")
... 
...     
0   32.0
10   50.0
20   68.0
30   86.0
40   104.0
50   122.0
