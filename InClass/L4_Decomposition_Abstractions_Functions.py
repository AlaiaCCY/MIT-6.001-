# Lecture 4 Decomposition, Abstractions, Functions
# In class Notes

# =============================================================================
# Decomposition: Different devices work together to achieve an end goal

# Abstraction: Use function specifications or docstrings to specify what input
#              codes take and produce what kind of output.

# Function: name, parameters, docstring, body, returns (need to think as coder
#           and user)
#           if there is no return statement, python will return None(NoneType)
# =============================================================================

# =============================================================================
# Variable Scope:
# 1. formal parameter(in the function definition) gets bound to the 
# value of actual parameter(actual input) when function is called.
# 2. scope means environment, scope of a function is a mini-environment other
# than main environment, after function finished, it will take only the return
# value back to the main environment.
# 3. scope is mapping of names to objects
# =============================================================================

# Function structure
# create function
def is_even(i):
    # first part is docstring
    '''
    input: i, a positive int
    Returns True if i is even, otherwise False
    '''
    # follow with body
    print('inside is_even')
    # last part is return
    return i%2 == 0

# call the function with specific input
print(is_even(2))


# Example 2
print("example 2")
def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

print(is_even_with_return(3) ) # <-  print: False

def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2

print(is_even_without_return(3) ) # <- print: None


#########################
## EXAMPLE: functions as arguments
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20func_a(%29%3A%0A%20%20%20%20print('inside%20func_a'%29%0A%0Adef%20func_b(y%29%3A%0A%20%20%20%20print('inside%20func_b'%29%0A%20%20%20%20return%20y%0A%0Adef%20func_c(z%29%3A%0A%20%20%20%20print('inside%20func_c'%29%0A%20%20%20%20return%20z(%29%0A%0Aprint(func_a(%29%29%0Aprint(5%2Bfunc_b(2%29%29%0Aprint(func_c(func_a%29%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
# Example 3
def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
# Fisrt print func_c and then func_a
# function does not run untill you call
print(func_c(func_a))


#########################
## EXAMPLE: returning function objects
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20f(%29%3A%0A%20%20%20%20def%20x(a,%20b%29%3A%0A%20%20%20%20%20%20%20%20return%20a%2Bb%0A%20%20%20%20return%20x%0A%20%20%20%20%0Aval%20%3D%20f(%29(3,4%29%0Aprint(val%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def f():
    def x(a, b):
        return a+b
    return x
    
# the first part, f(), returns a function object
# then apply that function with parameters 3 and 4
val = f()(3,4)
print(val)



#########################
## EXAMPLE: shows accessing variables outside scope
#########################
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def h(y):
    pass
    #x += 1 #leads to an error without line `global x` inside h
x = 5
h(x)
print(x)


#########################
## EXAMPLE: hader scope example from slides
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20g(x%29%3A%0A%20%20%20%20def%20h(%29%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20'abc'%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20%20print('in%20g(x%29%3A%20x%20%3D',%20x%29%0A%20%20%20%20h(%29%0A%20%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20g(x%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)


#########################
## EXAMPLE: complicated scope, test yourself!
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20f(x%29%3A%0A%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20print('in%20f(x%29%3A%20x%20%3D',%20x%29%0A%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20f(x%29%0Aprint('in%20main%20program%20scope%3A%20z%20%3D',%20z%29%0Aprint('in%20main%20program%20scope%3A%20x%20%3D',%20x%29%0A%0Adef%20g(x%29%3A%0A%20%20%20%20def%20h(x%29%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20x%2B1%0A%20%20%20%20%20%20%20%20print(%22in%20h(x%29%3A%20x%20%3D%20%22,%20x%29%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20%20print('in%20g(x%29%3A%20x%20%3D%20',%20x%29%0A%20%20%20%20h(x%29%0A%20%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20g(x%29%0Aprint('in%20main%20program%20scope%3A%20x%20%3D%20',%20x%29%0Aprint('in%20main%20program%20scope%3A%20z%20%3D%20',%20z%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)