#problem 92
import time

dic = {}

def chain(n):
    d = 0
    check = n
    while 1:
        if n < 10:
            d += n**2
            if check < 568:
                if d == 1:
                    dic[check] = 0
                    return 0
                if d == 89:
                    return 1
                n = d
                d = 0
            else:
                if dic.get(d) != None:
                    return 0
                return 1
        d += (n%10)**2
        n /= 10
        
def main():
    d = 0
    for i in xrange(1,10000000):
        if chain(i)==1:
            d += 1
    return d

n = time.time()
print main()
print time.time()-n
