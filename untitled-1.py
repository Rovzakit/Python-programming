
##def naive_mul(x, y):
    ##r = 0
    ##for i in range(y):
        ##r += x
    ##return r

##for i in range(101):
    ##for j in range(101):
        ##if(not (naive_mul(i, j) == i * j)):
            ##print(False, i, j)
            ##break
        ##else:
            ##print(True, i, j)
          
#def fast_mul(x, y):
    #r = 0
    #while(x > 0):
        #if(x % 2 == 1):
            #r += y
        #x //= 2
        #y *= 2
    #return r

##for i in range(101):
    ##for j in range(101):
        ##if(not (fast_mul(i, j) == i * j)):
            ##print(False, i, j)
        ##else:
            ##print(True, i, j)
            
#def fast_pow(a, b):
    #l = 1
    #if(not b):
        #return 1
    #while(b):
        #if(b % 2 == 0):
            #b//=2
            #a *= a
        #else:
            #b -= 1
            #l *= a
    #return l

##for i in range(101):
    ##for j in range(101):
        ##if(not (fast_pow(i, j) == pow(i, j))):
            ##print(False, i, j)
        ##else:
            ##print(True, i, j)

import math

def f(x, y):
    return (32 * pow(y, 6) - 90 * y)/(math.sin(78 * pow(y, 7) + pow(y, 2)) - math.cos(y)) - math.sqrt((pow(x, 4) - pow(y, 2) - 23) / (pow(x, 7) + math.log(x))) - math.sqrt((math.tan(x) + pow(x, 8))/(pow(y, 2) + 58 * pow(y, 3)))

#print(f(79, 35))
#print(f(7, 15))

def f2(x):
    if(x < 72):
        return 32 * pow(pow(x, 7) + 23 * pow(x, 3), 6) - 59 * x
    elif(72 <= x and x < 117):
        return 77 * (x - pow(x, 2)) - 51 * pow(x, 5)
    elif(117 <= x and x < 208):
        return math.cos(47 * pow(x, 7) + math.cos(x)) + abs(pow(x, 3) + 53 * pow(x, 4))
    else:
        return math.sin(56 * pow(x, 7)) - x / 90 - 29
    
#print(f2(262))
#print(f2(192))

def f3(n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += 32 * pow(j, 2) - 90 * pow(j, 7) + 77 * (math.tan(j) + 59 * i + 5)
    return res
    
#print(f3(85, 45))
#print(f3(86, 95))

def f4(n):
    if(n == 0):
        return 7
    elif(n == 1):
        return 9
    else:
        return math.tan(f4(n - 2)) + abs(f4(n - 1))
    
#print(f4(2))
#print(f4(8))











