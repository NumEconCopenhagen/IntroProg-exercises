print('the limit is:')
x = sm.symbols('x')
sm.limit(sm.sin(x)/x,x,0)

print('the derivative is')
x = sm.symbols('x')
sm.diff(sm.sin(2*x),x)