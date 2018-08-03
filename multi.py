import os 
from multiprocessing import Process

def hello(name):
    print('child process:{}'.format(os.getgid()))
    print('Hello ' + name)

def main():
    p = Process(target = hello , args = ('shiyanlou', ))
    p.start()
    p.join()
    print('parent process: {}'.format(os.getgid()))

if __name__ == '__main__':
    main()
