#Single use function that computes a very accurate estimation of pi, I copied the result into the pi function.
def ComputePi():
    pi = 3
    sign = -1
    for i in range(2,500000000,2):
        sign = -sign
        pi += sign*4/((i)*(i+1)*(i+2))
        print(i)
    return pi

#   This function just returns the first 16 digits of Pi, as calculated by the previous function
def Pi():
    return 3.141592653589793


#intPow is a simple multiplacation loop to serve as a power function for integer exponents
def intPow(X, Y):
    x = 1
    for i in range(1, Y+1):
        x *= X
    return x

#   Simple looping multiplication to return a factorial
def fact(X):
    out = 1
    for i in range(1, X+1):
        out *= i
    return out

#   a conversion from Degrees to Radians, required as the taylor series for Sin functions in Rad
def radian(X):
    return X*Pi()/180

#   a conversion from Radians to Degrees
def degrees(X):
    return X*180/Pi()

#   Computes the taylor series for Sin. Source = "https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions"
def radSin(X):
    X = X%(2*Pi())
    out = 0
    sign = -1
    for i in range(1, 100, 2):
        sign = -sign
        out += sign*intPow(X,i)/fact(i)
        print(out)
    return out

#   converts input into Rad, then  runs radSin
def sin(X):
    X = radian(X)
    return radSin(X)

#   Computes Cos by doing Sin(X + 90)
def cos(X):
    return sin(X + 90)

#   Same concesp as Cos, converts radSin by inputing (X+(Pi/2))
def radCos(X):
    return radSin(X + (Pi()/2))


