Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
for i in range(0,10,2):
    print("I love Fishc")

    
I love Fishc
I love Fishc
I love Fishc
I love Fishc
I love Fishc
for i in 5:
    print("I love Fishc")

    
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    for i in 5:
TypeError: 'int' object is not iterable
for i in "5"
    print("I love Fishc")
    
SyntaxError: expected ':'
for i in "5":
    print("I love Fishc")

    
I love Fishc
for i in range(5):
    print("I love Fishc")

    
I love Fishc
I love Fishc
I love Fishc
I love Fishc
I love Fishc
while True:
    answer = input("主人，我可以退出循环了吗?")
    if answer == "可以!":
            break
    print("哎，好累~~~")

    
主人，我可以退出循环了吗?no
哎，好累~~~
主人，我可以退出循环了吗?可以
哎，好累~~~
主人，我可以退出循环了吗?可以!
while True:
    answer = input("主人，我可以退出循环了吗?")
    if answer == "可以!":
            continue
    print("哎，好累~~~")

    
主人，我可以退出循环了吗?no
哎，好累~~~
主人，我可以退出循环了吗?可以!
主人，我可以退出循环了吗?可以!
主人，我可以退出循环了吗?NO
哎，好累~~~
主人，我可以退出循环了吗?
哎，好累~~~
主人，我可以退出循环了吗?
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    answer = input("主人，我可以退出循环了吗?")
KeyboardInterrupt
print range(10)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (range(10))
range(0, 10)
print (list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    while True:
        break
        print(1)
            print(2)
            
SyntaxError: unexpected indent
while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
SyntaxError: invalid syntax
while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
SyntaxError: invalid syntax
while True:
    while True:
        break
    print(2)
    break
print(3)
SyntaxError: invalid syntax
while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
SyntaxError: invalid syntax

============= RESTART: C:/Users/heiyu/Desktop/python学习日志/作业-测试1..py ============
2
3
i = 0
string = "I LoveFishc.com"
while i < len(string):
    print(i)
    i += 1

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
>>> 
============= RESTART: C:/Users/heiyu/Desktop/python学习日志/作业-测试1..py ============
2
3
请输入密码:小甲鱼
密码输入错误!您还有 2 次机会!请输入密码:*小甲鱼
Traceback (most recent call last):
  File "C:/Users/heiyu/Desktop/python学习日志/作业-测试1..py", line 16, in <module>
    print("密码中不能含有"*"号！您还有",count,"机会!",end="")
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
============= RESTART: C:/Users/heiyu/Desktop/python学习日志/作业-测试1..py ============
2
3
请输入密码:*小甲鱼*
Traceback (most recent call last):
  File "C:/Users/heiyu/Desktop/python学习日志/作业-测试1..py", line 23, in <module>
    print("密码中不能含有"*"号！您还有",count,"机会!",end="")
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
============= RESTART: C:/Users/heiyu/Desktop/python学习日志/作业-测试1..py ============
2
3
请输入密码:*小甲鱼
密码中不能含有'*'号！您还有 3 机会!请输入密码:小甲鱼
密码输入错误!您还有 2 次机会!请输入密码:Fishc.com
密码正确，进入程序......
按回车键退出
