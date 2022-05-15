# Lecture 4 Tuples, Lists, Aliasing, Mutability, Cloning
# In class Notes

# =============================================================================
# Coumpound data types: Tuples & Lists
# Tuples: 
#    sequance of elements, can mix element types
#    cannot caange element values, immutable
#    represented with parentheses name = ("a", "b")
#    access by name[index] where index start with 0
# Lists:
#    ordered sequence of information
#    accessible by index, name[index] start from 0
#    a list is denoted by square brakets, name = ["a", 2]
#    a list contains elements (could be mix type but not usual)
#    list elements can be changed so a list is mutable
# =============================================================================

# =============================================================================
# Tuple section:
# =============================================================================

# empty tuples
te = ()
t = (2, "mit", 3)
print(t[0])
print(t + (5,6)) # -> (2, 'mit', 3, 5, 6)
print(t[1:2]) # -> ('mit',) comment means it is tuples with one element
len(t) # how many element inside tuples
# t[1] = 4 gets error because tuples are immutable

# This does not works
print("Example 1")
x=1
y=2
# x = y
# y = x
# But this works
(x,y) = (y,x) # value of y assign to x, value of x assign to y
print(x,y)

# Tuples could be return for multiple objects
#########################
## EXAMPLE: returning a tuple
#########################
print("Example 2")
def quotient_and_remainder(x, y):
    q = x // y # // is integer division
    r = x % y
    return (q, r)
    
(quot, rem) = quotient_and_remainder(5,3)
print(quot)
print(rem)

#########################
## EXAMPLE: iterating over tuples
#########################
print("Example 3")
def get_data(aTuple):
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)   
        # only add words haven't added before
        if t[1] not in words:   
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print("a:",a,"b:",b,"c:",c)

# apply to any data you want!
tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))    
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
        "Taylor Swift wrote songs about", num_people, "people!")

    
# =============================================================================
# List section:
#    ListName.append(element) add element at the end of the list
#    ListA + ListB new list of all list A followed by list B
#    ListName.extend(ListName) add list at the end of the list
#    del(L[index]) delete element at a pecific index
#    L.pop() remove the last element in the list
#    L.remove(element) remove element in the list(only remove the first occur)
# =============================================================================
print("List section:")
alist = []
L = [1, 'a', 4, [1,2]]
print(len(L))
print(L[0])

# Change element
print("Example 4")
L = [1,2,3]
L[1] = 5
print(L) # <- [1, 5, 3] only modify the second element not reassign a new list

#########################
## EXAMPLE: sum of elements in a list
#########################
print("Example 5")
def sum_elem_method1(L):
  total = 0 
  for i in range(len(L)): # iterate each element by index
      total += L[i] 
  return total

# Prefer this function because it is more clear
def sum_elem_method2(L):
    total = 0 
    for i in L: # iterate each element
        total += i 
    return total

print(sum_elem_method1([1,2,3,4]))
print(sum_elem_method2([1,2,3,4]))

#########################
## EXAMPLE: various list operations
## put print(L) at different locations to see how it gets mutated
#########################
print("Example 6")
L1 = [2,1,3]
L2 = [4,5,6]
# add things to list
L3 = L1 + L2 # <- [2,1,3,4,5,6]
L1.extend([0,6]) # L1 <- [2,1,3,0,6]

# delete things to list
L = [2,1,3,6,3,7,0]
L.remove(2) # -> [1,3,6,3,7,0]
L.remove(3) # -> [1,6,3,7,0]
del(L[1]) # -> [1,3,7,0]
print(L.pop()) # -> [1,3,7]

# Split the list
s = "I<3 cs"
print(list(s))
print(s.split('<'))
# Join the list
L = ['a', 'b', 'c']
print(''.join(L))
print('_'.join(L))
# Sort the list
L=[9,6,0,3]
print(sorted(L)) # returns sorted list and does not change L
L.sort() # returns None, change L
L.reverse() # returns None, change L

#########################
## EXAMPLE: aliasing
#########################
print("Example 7")
a = 1
b = a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)

#########################
## EXAMPLE: cloning
## Make a new copy of the list which does not change when the list change
#########################
cool = ['blue', 'green', 'grey']
chill = cool[:] # copy each element and assign chill list
chill.append('black')
print(chill)
print(cool)

#########################
## EXAMPLE: sorting with/without mutation
#########################
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort() # returns None, and change the original object
print(warm)
print(sortedwarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool) # return sorted list, does not change original object
print(cool)
print(sortedcool)

#########################
## EXAMPLE: lists of lists of lists...
## Lists of list is the indicator to the element list
#########################
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors) # [['yellow', 'orange'], ['red']]
hot.append('pink')
print(hot) # ['red', 'pink']
print(brightcolors) # [['yellow', 'orange'], ['red', 'pink']]


###############################
## EXAMPLE: mutating a list while iterating over it
###############################
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
      
def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print(L1, L2)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1, L2)

###############################
## EXERCISE: Test yourself by predicting what the output is and 
##           what gets mutated then check with the Python Tutor
###############################
cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool)
print(warm)

colors1 = [cool]
print(colors1)
colors1.append(warm)
print('colors1 = ', colors1)

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2)

warm.remove('red') 
print('colors1 = ', colors1)
print('colors2 =', colors2)

for e in colors1:
    print('e =', e)

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1)
    else:
        print(e)

flat = cool + warm
print('flat =', flat)

print(flat.sort())
print('flat =', flat)

new_flat = sorted(flat, reverse = True)
print('flat =', flat)
print('new_flat =', new_flat)

cool[1] = 'black'
print(cool)
print(colors1)




