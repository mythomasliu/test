#!/usr/bin/python3

from multiprocessing import Process , Queue
import sys, csv

class cft():
    def __init__(self,configfile):
        self.configfile = configfile

def cfgread(configfile):
    with open(configfile,'r') as file:
        tmp = {'s':0}
        for i in file:
            try:
                a = i.split(' = ')[0].strip()
                b = float(i.split(' = ')[1].strip())
            except:
                print("Parameter Error")
                sys.exit()
            if a == 'JiShuL' or a == 'JiShuH':
                tmp[a] = b
            else:
                tmp['s'] += b
        return tmp

class UserData():
    def __init__(self,userdatafile):
        self.userdatafile = userdatafile


def useread(userfile,q1):
    with open(userfile,'r') as file:
        tmp = {}
        for i in file:
            a = i.split(',')
            tmp[a[0]] = a[1].strip()
        q1.put(tmp)
        return tmp

def calculator(cfg,q1,q2):
    gongzi = []
    user = q1.get()
    for gh , gz in user.items():
        shebaon = cfg['s']
        jishu1 = cfg['JiShuL']
        jishu2 = cfg['JiShuH']
        gh = int(gh)
        gz = int(gz)
        if gz < jishu2 and gz > jishu1:
            shebao = gz * shebaon
        elif gz > jishu2:
            shebao = jishu2 * shebaon
        elif gz < jishu1:
            shebao = jishu1 * shebaon
        e = gz - shebao - 3500

        if e > 80000:
            geshui = e * 0.45 - 13505
            gz2 = gz - shebao - geshui
        if e > 55000 and e <= 80000:
            geshui = e * 0.35 - 5505
            gz2 = gz - shebao - geshui
        if e > 9000 and e <= 35000:
            geshui = e * 0.25 - 1005
            gz2 = gz - shebao - geshui
        if e > 4500 and e <= 9000:
            geshui = e * 0.2 - 555
            gz2 = gz - shebao - geshui
        if e > 1500 and e <= 4500:
            geshui = e * 0.1 - 105
            gz2 = gz - shebao - geshui
        if e <= 1500 and e > 0:
            geshui = e * 0.03
            gz2 = gz - shebao - geshui
        if e <= 0:
            geshui = 0.00
            gz2 = gz - shebao
        temp = ["{0},{1},{2:.2f},{3:.2f},{4:.2f}".format(gh,gz,shebao,geshui,gz2)]
            #temp = [gh,gz,shebao,geshui,gz2]
        gongzi.append(temp)
    q2.put(gongzi)
    return gongzi

def dumptofile(outfile,q2):
    gongzi = q2.get()
    with open(outfile,'w') as file_out:
        tmpcsv = csv.writer(file_out)
        tmpcsv.writerows(gongzi)

def main():
    configfile = r"c:\Users\x1c\Desktop\untitled\test.cfg"
    userfile = r"c:\Users\x1c\Desktop\untitled\user.csv"
    outfile = r"c:\Users\x1c\Desktop\untitled\gongzi.csv"

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            args = sys.argv[1:]
            index1 = args.index('-c')
            index2 = args.index('-d')
            index3 = args.index('-o')
            print(args,index1,index2,index3)
            configfile = str(args[index1 + 1])
            userfile = str(args[index2 + 1])
            outfile = str(args[index3 + 1])
            print(configfile)
            print(type(configfile))
            q1 = Queue()
            q2 = Queue()
            cfg = cfgread(configfile)
            print(cfg)
            Process(target=useread,args=(userfile,q1)).start()
            Process(target=calculator,args=(cfg,q1,q2)).start()
            Process(target=dumptofile,args=(outfile,q2)).start()
        else:
            print("Parameter Error")
    except:
        print('Parameter Error')

