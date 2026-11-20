i = 1
while i < 5:
    print("循环内，i的值是", i)
    i += 1
else:
    print("循环外，i的值是",i)
    input("按回车键退出")


i = 1
while i < 5:
    print("循环内，i的值是", i)
    if i == 2:
        break
    i += 1
else:
    print("循环外，i的值是",i)
    input("按回车键退出")



"""每周打卡小程序"""
day = 1
while day <= 7:
    answer = input("今天有好好学习吗?")
    if answer != "有":
        break
    day += 1
else:
    print("非常棒，你已经坚持了7天连续学习!")
   


   
