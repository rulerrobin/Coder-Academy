# Create a function called factor_check() that takes a non-negative integer as its argument. The function should return True if the number is divisible by 3 or 5, and false otherwise.

# E.g. factor_check(4) should return False

# E.g. factor_check(12), should return True

# E.g. factor_check(0) should return False

# MINE

def factor_check(a):
    
    while a > 0:
        if a % 3 == 0 or a % 5 == 0:
            return True
        else:
            return False
    else:
        return False


b = factor_check(0)
print (b)

# Solution
# In a Boolean expression, 0 evaluates to false.
# If not number = 0 which means if not number says if number is false which is zero in boolean after mod of 3 then return true

def factor_check(number):
    if not number:
        return False
    if not number % 3:
        return True
    if not number % 5:
        return True
    return False