# Lecture 2 Branching and Iteration
# In class Notes

# =============================================================================
# clear all (clear all the console)
# %reset -f (clear all the variables)
# =============================================================================

# =============================================================================
# Srting and concatenation strings
# =============================================================================
hi = "hi there"
name = "ana"
greet = hi + name
greeting = hi + ' ' + name
print('+ does not add space:', greet)
print(greeting)
print("* number can repeat number of times:", (greeting + " ") * 3)

# =============================================================================
# print(): use , python will add a space(does not need to be string)
#          use + python will not add a space(every object need to be string)
#          \n is turn to next line in ""
# =============================================================================
x = 1
print(x)
x_str = str(x)
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
print("my fav number is" + x_str + "." + "x=" + x_str)

# =============================================================================
# Input & Output
# Input is going to be string, But we can cast to other
# =============================================================================
# text = input("Type anything")
# print(text * 5)

# num = int(input('Type number'))
# print(num * 5)

# =============================================================================
# Comparison operation on int, float, string(needs to be same object)
# >, >=, <, <=, ==, !=
# and, or could be used in the comparison also
# =============================================================================
i = "a"
j = "b"
print(i > j)
print(i <= j)
print(i == j)

# =============================================================================
# if <condition>:
# elif <condition>:
# else:
# =============================================================================
#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))
#if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
#elif x < y:
#    print("x is smaller")
#elif x > y:
#    print("y is smaller")
#print("thanks!")

# =============================================================================
# while <condition>: 
# break statement immediatelt exits while loop, skips remaining expressions
# for n in range(number):
# range(x) is from 0 to x-1
# =============================================================================
print("example 1:")
n = 0
while n < 5:
    print(n)
    n = n+1

print("example 2:")
for n in range(5):
    print(n)

print("example 3:")
mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)

print("example 4: stop when number is 5 even though is less than 10")
n = 0
while n < 10:
    print(n)
    if n == 5:
        break
    n = n+1