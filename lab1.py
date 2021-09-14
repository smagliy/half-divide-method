import math
import numpy
from matplotlib import pylab

func_glob = lambda x: ((5-x)**1/3)-x

a1, b1 = 1.0, 2.0
e = 0.02

def half_divide_method(a, b, f):
    x = (a + b) / 2
    while math.fabs(f(x)) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2


X = numpy.arange(0.0, 3.0, 0.1)
pylab.plot([x for x in X], [func_glob(x) for x in X])
pylab.grid(True)
pylab.show()


print('root of the equation half_divide_method %s' % half_divide_method(a1, b1, func_glob))

