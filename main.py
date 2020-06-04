from Calculator.Calculator import Calculator
from Calculator import Transcendental

print("<------------------DRIVER------------------>\n")
print("x^y examples:")
print("5^0 =",Transcendental.power(5,0))
print("5^2.5 =", Transcendental.power(5,2.5))
print("5^0.13 =", Transcendental.power(5,0.13))
print("5^-2.5 =", Transcendental.power(5,-2.5))
print("where y is very large or very small")
print("5^200 =", Transcendental.power(5,200))
print("5^0.00000001235 =", Transcendental.power(5,0.00000001235))


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
print("standard_deviation([5,10,11,14,26,58,98]) =", Transcendental.standard_deviation([5,10,11,14,26,58,98]))
print("standard_deviation([5,10.215,11.948,14,26,58,98]) =", Transcendental.standard_deviation([5,10.215,11.948,14,26,58,98]))

print("\n\nMAD(list) examples:")
print("MAD([5,10,11,14,26,58,98]) =", Transcendental.MAD([5,10,11,14,26,58,98]))
print("MAD([5,10.215,11.948,14,26,58,98]) =", Transcendental.MAD([5,10.215,11.948,14,26,58,98]))


print("\n\ncosh(x) examples:")
print("cosh(0) =", Transcendental.cosh(0))
print("cosh(15) =", Transcendental.cosh(15))
print("cosh(-15) =", Transcendental.cosh(-15))
print("cosh(0.000001) =", Transcendental.cosh(0.000001))


print("\n\n10^x examples:")
print("10^0 =",Transcendental.powTen(0))
print("10^2.5 =", Transcendental.powTen(2.5))
print("10^0.13 =", Transcendental.powTen(0.13))
print("10^-2.5 =", Transcendental.powTen(-2.5))
print("10^200 =", Transcendental.powTen(200))
print("10^0.00000001235 =", Transcendental.powTen(0.000000001235))


print("\n<----------------END DRIVER---------------->\n")
