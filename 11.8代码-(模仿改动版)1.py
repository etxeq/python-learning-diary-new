"""每周打卡小程序---改进版"""
day = 1
while day <= 7:
    answer = input("今天有好好学习吗?")
    if answer != "有":
        print("明天可以开始好好学习!")
        continue
    print("明天继续!")
    day += 1
else:
    print("非常棒，你已经坚持了7天连续学习!")
