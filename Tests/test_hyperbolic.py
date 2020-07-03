# tests cosh function from calculator.transcendental
# Kyungjin Kim
import math
from Calculator import cosh
from MathHelper import computePi

ACCURACY_DIGITS = '.10g'

class TestCosh:
    def test_high(self):
        x = 0
        y1 = cosh(x)
        y2 = math.cosh(x)
        difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        while difference:
            x += 0.1
            y1 = cosh(x)
            y2 = math.cosh(x)
            difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        print(f'maximum within error threshold: x={x}, cosh(x)={y1}, expected cosh(x)={y2}')
    def test_low(self):
        x = 0
        y1 = cosh(x)
        y2 = math.cosh(x)
        difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        while difference:
            x -= 0.1
            y1 = cosh(x)
            y2 = math.cosh(x)
            difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        print(f'minimum within error threshold: x={x}, cosh(x)={y1}, expected cosh(x)={y2}')
    def test_transcendental_nb(self):
        assert format(cosh(computePi()), ACCURACY_DIGITS) == format(math.cosh(math.pi), ACCURACY_DIGITS)
    def test_zero(self):
        assert format(cosh(0), ACCURACY_DIGITS) == format(float(1), ACCURACY_DIGITS)
