#problem 92
import time

dic = {}

'''def Flen(n):
    dic2 = {}
    c = 0
    if n < 10:
        dic2[0] = n
        return dic2
    while 1:
        dic2[c] = n%10
        n /= 10
        c += 1
        if n < 10:
            dic2[c] = n
            return dic2'''

def Llen(n):
    d = []
    if n < 10:
        return [n]
    while 1:
        d.append(n%10)
        n /= 10
        if n < 10:
            d.append(n)
            return d
    
def chain(n):
    #mi mojem ispolzivats Flen(dictionary) ili Llen(list)
    #we can use Flen(dictionary) or Llen(list)
    listn = Llen(n)
    check = n
    while 1:
        d = 0
        for i in listn:
            d += i**2
        if check > 568:
            if dic.get(d) != None:
                return 0
            return 1
        if d == 89:
            return 1
        if d == 1:
            dic[check] = 0
            return 0
        listn = Llen(d) #<--- Flen or Llen

def main():
    d = 0
    for i in xrange(1,10000000):
        if chain(i)==1:
            d += 1
    return d

n = time.time()
print main()
print time.time()-n
