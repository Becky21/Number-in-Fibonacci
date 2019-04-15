# This Program checks whether Number n is in fibonacci sequence or not..

def inFibonacci(n):
    # Returns True if n is in fibonacci sequence
    # else 
    # Returns False

    a = 1 # First Number
    b = 0 # Second Number

    c = a + b # sum of a and b

    while n > c:    
        # keep looping till sum of a and b becomes greater than n
        c = a + b
        if c == n:
            return True
        a = b
        b = c

    return False

n = 2 # number to be checked

result = inFibonacci(n) # stores result in boolean

if result is True:
    print("{} is in fibonacci sequence.".format(n))
else:
    print("{} is not in fibonacci sequence.".format(n))