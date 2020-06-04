"""
   Driver

   Date: June 4th 2020
   Author: Alexis Laurens-Renner - 40055137
   Driver for presentation purposes
   """
from Calculator import Transcendental


def static_driver():
    print("<------------------DRIVER------------------>\n")
    print("x^y examples:")
    print("5^0 =", Transcendental.power(5, 0))
    print("5^2.5 =", Transcendental.power(5, 2.5))
    print("5^0.13 =", Transcendental.power(5, 0.13))
    print("5^-2.5 =", Transcendental.power(5, -2.5))
    print("where y is very large or very small")
    print("5^200 =", Transcendental.power(5, 200))
    print("5^0.00000001235 =", Transcendental.power(5, 0.00000001235))

    print("\n\nsin(x) examples:")
    print("sin(60) =", Transcendental.sin(60))
    print("sin(180) =", Transcendental.sin(180))
    print("sin(0) =", Transcendental.sin(0))
    print("sin(0.0001) =", Transcendental.sin(0.0001))

    print("\n\nlog10(x) examples:")
    print("log10(1000) =", Transcendental.log10(1000))
    print("log10(0) =", Transcendental.log10(0))
    print("log10(1) =", Transcendental.log10(1))
    print("log10(875) =", Transcendental.log10(875))
    print("log10(753.6) =", Transcendental.log10(753.6))

    print("\n\nstandard_deviation(list) examples:")
    print("standard_deviation([5,10,11,14,26,58,98]) =", Transcendental.standard_deviation([5, 10, 11, 14, 26, 58, 98]))
    print("standard_deviation([5,10.215,11.948,14,26,58,98]) =",
          Transcendental.standard_deviation([5, 10.215, 11.948, 14, 26, 58, 98]))

    print("\n\nMAD(list) examples:")
    print("MAD([5,10,11,14,26,58,98]) =", Transcendental.MAD([5, 10, 11, 14, 26, 58, 98]))
    print("MAD([5,10.215,11.948,14,26,58,98]) =", Transcendental.MAD([5, 10.215, 11.948, 14, 26, 58, 98]))

    print("\n\ncosh(x) examples:")
    print("cosh(0) =", Transcendental.cosh(0))
    print("cosh(15) =", Transcendental.cosh(15))
    print("cosh(-15) =", Transcendental.cosh(-15))
    print("cosh(0.000001) =", Transcendental.cosh(0.000001))

    print("\n\n10^x examples:")
    print("10^0 =", Transcendental.powTen(0))
    print("10^2.5 =", Transcendental.powTen(2.5))
    print("10^0.13 =", Transcendental.powTen(0.13))
    print("10^-2.5 =", Transcendental.powTen(-2.5))
    print("10^200 =", Transcendental.powTen(200))
    print("10^0.00000001235 =", Transcendental.powTen(0.000000001235))

    print("\n<----------------END DRIVER---------------->\n")



print("Transcendental functions:")
print("0 - Default Driver")
print("1 - x^y")
print("2 - sin(x)")
print("3 - log10(x)")
print("4 - Standard Deviation(list)")
print("5 - MAD(list)")
print("6 - cosh(x)")
print("7 - 10^x")
#print("Other functions:")

while True:
    menu = input("\nEnter the number associated with the function you want to use: ")
    try:
        menu = int(menu)
        if menu == 0:
            static_driver()
        elif menu == 1:
            xval = int(input("Enter the value for x: "))
            yval = int(input("Enter the value for y: "))
            print(Transcendental.power(xval,yval))
        elif menu == 2:
            xval = int(input("Enter the value for x: "))
            print(Transcendental.sin(xval))
        elif menu == 3:
            xval = int(input("Enter the value for x: "))
            print(Transcendental.log10(xval))
        elif menu == 4:
            strLst = input("Enter a list of numbers separated by a space: ")
            lst = strLst.split()
            try:
                for i in range(0, len(lst)):
                    lst[i] = float(lst[i])
            except:
                print("An element is not a number")
            else:
                print("standard deviation("+str(lst)+") =",Transcendental.standard_deviation(lst))
        elif menu == 5:
            strLst = input("Enter a list of numbers separated by a space: ")
            lst = strLst.split()
            try:
                for i in range(0, len(lst)):
                    lst[i] = float(lst[i])
            except:
                print("An element is not a number")
            else:
                print("MAD("+str(lst)+") =",Transcendental.MAD(lst))
        elif menu == 6:
            xval = int(input("Enter the value for x: "))
            print(Transcendental.cosh(xval))
        elif menu == 7:
            xval = int(input("Enter the value for x: "))
            print(Transcendental.powTen(xval))
        else:
            print("Invalid Input: not an option")
            continue

    except:
        print("Invalid Input: needs a number")
        continue
    finally:
        tryAgain = input("\nDo you want to try again? y/n: ")
        if tryAgain != "y":
            break



print("\nGoodbye")
