#!/usr/bin/python3
import sys
import csv
class cft():
    def __init__(self,configfile):
        self.configfile = configfile
        self._config = {}
    def read(self):
        with open(self.configfile,'r') as file:
            for i in file:        
                a = i.split(' = ')               
                self._config[a[0]] = a[1].strip()
            return self._config

class UserData():
    def __init__(self,userdatafile):
        self.userdatafile = userdatafile
        self.userdata = {}
        self.gongzi = []
    def use(self):
        with open(self.userdatafile,'r') as file:
            for i in file:        
                a = i.split(',')               
                self.userdata[a[0]] = a[1].strip()
            return self.userdata
    def calculator(self,cof):
        for gh , gz in self.userdata.items():
            conf = cft(cof)
            try:
                jishu1 = float(conf.read()['JiShuL'])
                jishu2 = float(conf.read()['JiShuH'])
                yanglao = float(conf.read()['YangLao'])
                yiliao = float(conf.read()['YiLiao'])
                shiye = float(conf.read()['ShiYe'])
                gongshang = float(conf.read()['GongShang'])
                shengyu = float(conf.read()['ShengYu'])
                gjjbl = float(conf.read()['GongJiJin'])
                sbbili = gjjbl + yanglao + yiliao + shiye + gongshang + shengyu
            except:
                print("Parameter Error")
                sys.exit()
            gh = int(gh)
            gz = int(gz)   
            if gz < jishu2 and gz > jishu1:
                shebao = gz * sbbili
            elif gz > jishu2:
                shebao = jishu2 * sbbili
            elif gz < jishu1:
                shebao = jishu1 * sbbili
            
            gongjj = gz * 0.06
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
            self.gongzi.append(temp)
        return self.gongzi

    def dumptofile(self,outputfile):
        with open(outputfile,'w') as file_out:
            tmpcsv = csv.writer(file_out)
            tmpcsv.writerows(self.gongzi)
                #mywriter = csv.writer(file_out)
                #mywriter.writerow([gh,gz,shebao,geshui,gz2])
               # file_out.write(\n)



if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            args = sys.argv[1:]
            index1 = args.index('-c')
            configfile = args[index1 + 1]
            index2 = args.index('-d')
            userfile = args[index2 + 1]
            index3 = args.index('-o')
            outfile = args[index3 + 1]
            
            a = cft(configfile)
            print(a.read())
            b = UserData(userfile)
            print(b.use())
            print(b.calculator(configfile))
            b.dumptofile(outfile)
   
        else:
            print("Parameter Error")
    except:
        print('Parameter Error')

