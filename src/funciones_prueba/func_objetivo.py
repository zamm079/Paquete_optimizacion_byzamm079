import numpy as np

def ackley_function(X):
    x=X[0]
    y=X[1]
    term1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2*np.pi * x) + np.cos(2*np.pi * y)))+ 20 + np.exp(1)
    return term1

def beale_function(X):
    x=X[0]
    y=X[1]
    r = (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
    return r

def booth_function(x):
    X=x[0]
    Y=x[1]
    r = (X + 2*Y - 7)**2 + (2*X + Y - 5)**2
    return r

def bukin_functionN6(X):
    x=X[0]
    y=X[1]
    r = 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)
    return r

def Crossintray_function(X):
    x=X[0]
    y=X[1]
    term1 = np.sin(x) * np.sin(y)
    term2 = np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))
    r = -0.0001 * (np.abs(term1 * term2) + 1)**0.1
    return r

def Easom_function(X):
    x=X[0]
    y=X[1]
    r = -np.cos(x)*np.cos(y)*np.exp(-((x-np.pi)**2 + (y-np.pi)**2))
    return r

def Eggholder_function(x):
    X=x[0]
    Y=x[1]
    term1 = -(Y + 47) * np.sin(np.sqrt(np.abs(X/2 + (Y + 47))))
    term2 = -X * np.sin(np.sqrt(np.abs(X - (Y + 47))))
    return term1 + term2

def goldstein_price_function(X):
    x=X[0]
    y=X[1]
    part1 = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))
    part2 = (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    r = part1 * part2
    return r

def Himmelblaus_function(X):
    x=X[0]
    y=X[1]
    r = (x**2 + y - 11)**2 + (x + y**2 -7)**2
    return r

def Holder_table_function(X):
    x=X[0]
    y=X[1]
    term1 = -np.abs(np.sin(x)*np.cos(y))
    term2 = np.exp(np.abs(1 - np.sqrt(x**2 + y**2)/np.pi))
    r = term1*term2
    return r

def Levi_functionN13(X):
    x=X[0]
    y=X[1]
    term1 = np.sin(3 * np.pi * x)**2
    term2 = (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2)
    term3 = (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2)
    r = term1 + term2 + term3
    return r

def matyas_function(X):
    x=X[0]
    y=X[1]
    r = 0.26 * (x**2 + y**2) - 0.48*x*y
    return r

def McCormick_function(X):
    x=X[0]
    y=X[1]
    r = np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1
    return r

def rastrigin(X):
    A = 10
    n = len(X)
    r = A * n + np.sum(X**2 - A * np.cos(2 * np.pi * X),axis=0)
    return r

def rosenbrock_funt(x):
    X=x[0]
    Y=x[1]
    r = (100 * (Y - X**2)**2) + (1 - X)**2 
    return r

def Schaffer_functionN2(X):
    x=X[0]
    y=X[1]
    term1 = np.sin(x**2 - y**2)**2 - 0.5
    term2 = (1 + 0.001 * (x**2 + y**2))**2
    r = 0.5 + term1 / term2
    return r

def Schaffer_functionN4(x):
    X=x[0]
    Y=x[1]
    numerator = np.cos(np.sin(np.abs(X**2 - Y**2)))**2 - 0.5
    denominator = (1 + 0.001 * (X**2 + Y**2))**2
    return 0.5 + numerator / denominator

def shekel(x, a=None, c=None):
    if a is None:
        a = np.array([
            [4.0, 4.0, 4.0, 4.0],
            [1.0, 1.0, 1.0, 1.0],
            [8.0, 8.0, 8.0, 8.0],
            [6.0, 6.0, 6.0, 6.0],
            [3.0, 7.0, 3.0, 7.0],
            [2.0, 9.0, 2.0, 9.0],
            [5.0, 5.0, 3.0, 3.0],
            [8.0, 1.0, 8.0, 1.0],
            [6.0, 2.0, 6.0, 2.0],
            [7.0, 3.6, 7.0, 3.6]
        ])
    if c is None:
        c = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    
    m = len(c)
    s = 0
    for i in range(m):
        s -= 1 / (np.dot(x - a[i, :2], x - a[i, :2]) + c[i])
    return s

def sphere_function(X):
    r = np.sum(X**2,axis=0)
    return r

def StyblinskiTang_function(X):
    r = np.sum(X**4 - 16*X**2 + 5*X,axis=0 )
    return r

def Three_hump_camel_function(x):
    X=x[0]
    Y=x[1]
    r  = 2*X**2 - 1.05*X**4 + (X**6)/6 + X*Y + Y**2
    return r




if __name__ == "__main__":
    puntox = np.array([1.0,2.0])
    print("prueba ackley_function: ",ackley_function(X=puntox))
    print("prueba beale_function: ",beale_function(X=puntox))
    print("prueba booth_function: ",booth_function(x=puntox))
    print("prueba bukin_functionN6: ",bukin_functionN6(X=puntox))
    print("prueba Crossintray_function: ",Crossintray_function(X=puntox))
    print("prueba Easom_function: ",Easom_function(X=puntox))
    print("prueba Eggholder_function: ",Eggholder_function(x=puntox))
    print("prueba goldstein_price_function: ",goldstein_price_function(X=puntox))
    print("prueba Himmelblaus_function: ",Himmelblaus_function(X=puntox))
    print("prueba Holder_table_function: ",Holder_table_function(X=puntox))
    print("prueba Levi_functionN13: ",Levi_functionN13(X=puntox))
    print("prueba matyas_function: ",matyas_function(X=puntox))
    print("prueba McCormick_function: ",McCormick_function(X=puntox))
    print("prueba rastrigin: ",rastrigin(X=puntox))
    print("prueba rosenbrock_funt: ",rosenbrock_funt(x=puntox))
    print("prueba Schaffer_functionN2: ",Schaffer_functionN2(X=puntox))
    print("prueba Schaffer_functionN4: ",Schaffer_functionN4(x=puntox))
    print("prueba shekel: ",shekel(x=puntox))
    print("prueba sphere_function: ",sphere_function(X=puntox))
    print("prueba StyblinskiTang_function: ",StyblinskiTang_function(X=puntox))
    print("prueba Three_hump_camel_function: ",Three_hump_camel_function(x=puntox))