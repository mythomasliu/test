#!/usr/bin/python3
import sys

def cal(x):
    b = 0
    d = 0
    for i in range(1,len(x)):
        num , gongzi = x[i].split(':')
        try:
            a = int(gongzi)
            c = int(num)
            if type(a) != int and type(c) != int:
                raise TypeError
        except:
            print("Parameter Error")
            sys.exit()
        f = a * 0.165
        e = a - 3500 - f
        if e > 80000:
            b = e * 0.45 - 13505
            d = a - b - f
        if e > 55000 and e <= 80000:
            b = e * 0.35 - 5505
            d = a - b - f
        if e > 35000 and e <= 55000:
            b = e * 0.3 - 2755
            d = a - b - f
        if e > 9000 and e <= 35000:
            b = e * 0.25 - 1005
            d = a - b - f
        if e > 4500 and e <= 9000:
            b = e * 0.2 - 555
            d = a - b - f
        if e > 1500 and e <= 4500:
            b = e * 0.1 - 105
            d = a - b - f
        if e <= 1500 and e > 0:
            b = e * 0.03
            d = a - b - f
        if e <= 0:
            d = a - f
        print("{0}:{1:.2f}".format(c,d))



if __name__ == "__main__":
    if len(sys.argv) > 1:
        cal(sys.argv)
    else:
        print("Parameter Error")
