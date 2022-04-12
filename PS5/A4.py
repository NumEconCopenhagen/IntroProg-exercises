def bisection(f,a,b,tol=1e-8):
    """ bisection
    
    Solve equation f(x) = 0 for a <= x <= b.
    
    Args:
    
        f (function): function
        a (float): left bound
        b (float): right bound
        tol (float): tolerance on solution
        
    Returns:
    
    """
    
    # test inputs
    if f(a)*f(b) >= 0:
        print("bisection method fails.")
        return None
    
    # step 1: initialize
    a_n = a
    b_n = b
    
    # step 2-4:
    while True:
        
        # step 2: midpoint and associated value
        m_n = (a_n+b_n)/2
        f_m_n = f(m_n)
        
        # step 3: determine sub-interval
        if abs(f_m_n) < tol:
            return m_n
        elif f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        else:
            print("bisection method fails.")
            return None
        
    return (a_n + b_n)/2

result = bisection(f,0,1,1e-8)
print(f'result is {result:.3f} with f({result:.3f}) = {f(result):.16f}')