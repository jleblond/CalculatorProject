# tester.py
# Author: Alexis Laurens-Renner
# Intially made for testing log10(X) for values between 1 and usrInp
# Returns values from the math library and the user defined function, as well as the amount of exact accurate decimal places, with the total average at the end
# Added runtime data for performance purposes
import math, timeit
from Calculator import log10


usrInp = int(input("Amount of iterations (positive integer): "))
totalStart = timeit.default_timer()
avg = 0
for i in range(0, usrInp+1):
    iterStart = timeit.default_timer()
    if i!=0:
        x = str(math.log10(i))
        y = str(log10(i))
        print(i, x)
        print(i, y)


        if len(x) >= len(y):
            count = 0
            for char in range(len(y)):
               if x[char] == y[char]:
                   count = count + 1
               else:
                   break
            print("Same decimal digits: ", count-2)
            avg = avg + count - 2
            print(x[:count+1])
            print(y[:count+1])
        else:
            count = 0
            for char in range(len(x)):
               if x[char] == y[char]:
                   count = count + 1
               else:
                   break
            print("Same decimal digits: ", count-2)
            avg = avg + count-2
            print(x[:count+1])
            print(y[:count+1])
        iterStop = timeit.default_timer()
        print("iteration runtime for i =",i,iterStop-iterStart)
        print()

avg = avg+10*math.log10(usrInp)
print("Average accuracy: ", (avg/(usrInp)))
totalStop = timeit.default_timer()
print("total runtime for",usrInp,"iterations:",totalStop-totalStart)
print("average runtime for",usrInp,"iterations",(totalStop-totalStart)/usrInp)