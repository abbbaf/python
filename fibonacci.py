"""
Finding the nth fibonacci number:
"""

def fib_binet(n):
    if n == 0:
        return 0
    a, b = 1, 1
    for i in bin(n)[3:]:
            a, b = (a**2 + 5*b**2) >> 1, a*b
            if (i == '1'):
                c = (a + b) >> 1
                a, b = c + 2*b, c
    return b



def fib_fast_doubling(n):
    if n == 0:
        return 0

    a, b = 1, 1
    
    for i in bin(n)[3:]:
        c = a**2
        a, b = 2*a*b - c, c + b**2
        if i == '1':
            a, b = b, a + b
      
    return a



def fib_fast_doubling_recursive(n):
    if n < 3:
        return [0,1,1][n]
    else:
        if n % 2 == 0:
            f1 = fib_fast_doubling_recursive(n/2) 
            f2 = fib_fast_doubling_recursive(n/2+1)
            return f1*(2*f2-f1)
        else:
            return fib_fast_doubling_recursive((n-1)/2)**2 + fib_fast_doubling_recursive((n-1)/2+1)**2


"""
Using iterations
"""
def fib(n):
    f = [1,0]
    for i in range(n):
        f = [f[1],sum(f)]
    return f[1]




def fib_matrix_exponentiation(n):

    def mult(x,y):
        if ( len(y) == 2 ):
            return [x[0]*y[0]+x[1]*y[1] , x[2]*y[0]+x[3]*y[1] ]
        a = x[0]*y[0] + x[1]*y[2]
        b = x[0]*y[1] + x[1]*y[3]
        c = x[2]*y[0] + x[3]*y[2]
        d = x[2]*y[1] + x[3]*y[3]
        return [a,b,c,d]

    # Only works for positive powers!
    def matrix_power( x, n ):
        if ( n == 1 ):
            return x
        if ( n%2 == 0 ):
            return matrix_power( mult(x, x), n//2 )
        return mult(x, matrix_power( mult(x, x), n//2 ) )
        
    return mult(matrix_power([1,1,1,0],n-1),[1,0])[0]


"""
Calculating the sum of the first n fibonacci numbers:
"""


"""
By using the following identity:
S(n) = S(n-1) + S(n-2) + 1
"""
def fsum_recursive(n):
    return fsum_recursive(n-1)+fsum_recursive(n-2)+1 if n > 2 else n-1


def fsum(n):
    result = [-1,0]
    for i in range(n):
        result[0], result[1] = result[1], result[0]+result[1]+1
    return result[1]



"""
This function uses the following identities:

S(2n) = S(n)[2s(n+1) - S(n)] + 2S(n+1)
S(2n-1) = [S(n)-S(n-1)]^{2}+[S(n-1)+1]^{2}-1
 
"""
def fsum_fast_method(n):
    if (n == 0):
        return 0
    a, b = 1, 0
    for i in bin(n)[3:]:      
        a, b =  b*(2*a-b)+2*a, (a-b)**2 + (b+1)**2 - 1
        if i == '1':
            a, b = a+b+1, a
    return a


def fsum_fast_method_recursive(n):
    if n < 3:
        return n
    if n % 2 == 1:
        n >>= 1
        a, b = fsum(n+1), fsum(n)
        return (a-b)**2 + (b+1)**2 - 1
    else:
        n >>= 1
        a, b = fsum(n), fsum(n-1)
        return b*(2*a-b)+2*a
