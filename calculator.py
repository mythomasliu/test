#!/usr/bin/python3
import sys

def cal(x):
    b = 0
    try:
        a = int(x[1])
        if type(a) != int:
            raise TypeError
    except:
        print("Parameter Error")
        return

    a = a - 3500
    if a > 80000:
        b = a * 0.45 - 13505
    
    if a > 55000 and a <= 80000:
        b = a * 0.35 - 5505
    if a > 35000 and a <= 55000:
        b = a * 0.3 - 2755
    if a > 9000 and a <= 35000:
        b = a * 0.25 - 1005
    if a > 4500 and a <= 9000:
        b = a * 0.2 - 555
    if a > 1500 and a <= 4500:
        b = a * 0.1 - 105
    if a <= 1500 and a > 0:
        b = a * 0.03

    print("{:.2f}".format(b))



if __name__ == "__main__":
    if len(sys.argv) > 1:
        cal(sys.argv)
    else:
        print("Parameter Error")
