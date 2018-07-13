import sys

def Hours(min):
    h = 0
    m = 0
    try:
        if min < 0:
            raise ValueError
        else:
            while min >= 60:
                min -= 60
                h += 1
        print(h ,' H,' , min , ' M')
    except ValueError:
        print("ValueError:Input number cannot be negative")

if __name__ == "__main__":
    # print(len(sys.argv), " " ,len(sys.argv[1]) , " ",len(sys.argv[0]))
    if len(sys.argv) > 1:
        Hours(int(sys.argv[1]))
    else:
        sys.exit()
    sys.exit(1)
