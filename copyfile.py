#!/usr/bin/env python3
import sys

def copy_file(src,dst):
    with open(src,'r') as src_file:
        with open(dst,'w') as dst_file:
            dst_file.write(src_file.read())



if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print('Parameter Error')
        print(sys.argv[0],'srcfile dstfile')
        sys.exit(-1)
    sys.exit(0)







def testa():

    if len(sys.argv) < 3:
        print("wrong parameter")
        print("./copyfile.py file1 file2")
        sys.exit(1)
    f1 = open(sys.argv[1])
    s = f1.read()
    f1.close
    f2 = open(sys.argv[2],'w')
    f2.write(s)
    f2.close()

