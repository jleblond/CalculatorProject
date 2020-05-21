
def ComputePi():
    pi = 3
    sign = -1
    for i in range(2,500000000,2):
        sign = -sign
        pi += sign*4/((i)*(i+1)*(i+2))
        print(i)
    return pi

def Pi():
    return 3.141592653589793



def intPow(X, Y):
    x = 1
    for i in range(1, Y+1):
        x *= X
    return x

def fact(X):
    out = 1
    for i in range(1, X+1):
        out *= i
    return out

def radian(X):
    return X*Pi()/180

def degrees(X):
    return X*180/Pi()

def radSin(X):
    X = X%(2*Pi())
    out = 0
    sign = -1
    for i in range(1, 100, 2):
        sign = -sign
        out += sign*intPow(X,i)/fact(i)
        print(out)
    return out

def sin(X):
    print("%s deg = %s rad" % (X, radian(X)))
    X = radian(X)
    return radSin(X)


def cos(X):
    return sin(X + 90)

def radCos(X):
    return radSin(X + (Pi()/2))

print(radSin(72))


