#problem 206
import time
def main():
    b = 1010101030
    jump = [40,60]
    while 1:
        for i in jump:
            b += i
            a = str(int(b**2))
            if a[0] == '1' and a[2] == '2' and a[4] == '3' and a[6] == '4' and a[8] == '5' and a[10] == '6' and a[12] == '7' and a[14] == '8' and a[16] == '9' and a[18] == '0':
                return b
print main()


