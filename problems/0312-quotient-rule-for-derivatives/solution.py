import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    Dgx = 0
    gx = 0
    ng = len(g_coeffs) - 1

    for coef in g_coeffs:
        gx += coef * x**ng

        if ng > 0:
            Dgx += ng * coef * x**(ng-1)

        ng -= 1

    Dhx = 0
    hx = 0
    nh = len(h_coeffs) - 1

    for coef in h_coeffs:
        hx += coef * x**nh

        if nh > 0:
            Dhx += nh * coef * x**(nh - 1)

        nh -= 1

    return (Dgx * hx - gx * Dhx) / hx**2
    
    
