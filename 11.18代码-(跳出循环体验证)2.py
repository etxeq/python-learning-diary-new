"""检验beak和continue语句只能跳出一层循环体"""
day = 1
hour = 1
while day <= 7:
    while hour <= 8:
        print("我今天一定要坚持学习8个小时!")
        hour += 1
        if hour > 1:
            break
        day += 1
        input("按回车键退出")

