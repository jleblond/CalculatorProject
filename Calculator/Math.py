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


# formula based on: Beebe, N. H. (2017). 10.3.2. In The Mathematical-Function Computation Handbook: Programming Using the MathCW
# Portable Software Library (pp. 287-290). Springer International Publishing. doi:https://doi-org.lib-ezproxy.concordia.ca/10.1007/978-3-319-64110-2
# A simplified version of the formula is used here
def log10(X): # Handle exceptional cases, return -1 until adding exceptions
    if (X == 1):
        return 0
    if (X == 0):
        return -1
    if (X < 0):
        return -1

    n = 0  # Start exponent of base 10

    while (X >= 1.0):
        X = X / 10.0
        n += 1

    while (X <= 0.316227766016838):
        X = X * 10.0
        n = n - 1

    # Produce a change of variable
    z = (X - 1.0) / (X + 1.0)
    D = 0.868588963807  # 2*log10(e) approximated to the first 12 digits

    # Taylor series
    sum = z
    for k in range(3, 53, 2):
        sum += (z ** k) / k

    return D * sum + n

#end of log10(X)






