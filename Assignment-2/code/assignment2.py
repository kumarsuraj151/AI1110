from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import *
import sympy as sp
x = sp.symbols ('x')
y= sp.Function('y')(x)

diffeq=Eq(y.diff(x)-(x+y+2)/(2*x+2*y-1),0)

q=dsolve(diffeq,y)
print(q)