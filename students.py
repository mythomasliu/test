#!/usr/bin/env python3
n = int(input("输入学生数量"))
data = {} #存储数据的字典变量
Subjects = ('物理','历史','化学')
for i in range(0,n):
    name = input('请输入学生姓名{}'.format(i + 1))
    marks = []
    for x in Subjects:
        marks.append(int(input('请输入科目分数：{}'.format(x))))
    data[name] = marks
for x , y in data.items():
    total = sum(y)
    print("{} 的分数为 {}".format(x,total))
    if total < 120:
        print(x,"failed:(")
    else:
        print(x,'passed:)')
