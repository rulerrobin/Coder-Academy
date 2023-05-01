# Numerator and denominator from the user and calculate quotient
# Try except block / try catch block will run w/e code in block and any erros will be sent to except block
# try except else finally blocks

class NegativeError(Exception):
    pass

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter denominator: "))

    q = n / d # Exception was thrown/raised on this line for ZerDivison Error

    # we want to raise an error when either n or d is negative
    if n < 0 or d < 0:
        raise Exception("Negative number error")

    print(q)

except NegativeError:
    print("No negative numbers please")

except ZeroDivisionError as e: # command after except is w/e error that will be accepted
    print ("Denominator cannot be zero")    
    print (e)
    print (type(e))

except ValueError as e: # Exception means w/e exception was raised and saved in variable e
    print ("Please type numbers only")    
    print (e)
    print (type(e))    

except Exception as e: # Exception means w/e exception was raised and saved in variable e
    print ("Something went wrong")    
    print (e)
    print (type(e))

else:
    # executed whenever try block is successfully executed without raising any exception
    print ("I am else block")

finally:
    # this runs at the end no matter if exception is raised or not
    print("i am finally block")

print ("The end of the program")

# file handling
# try:
    # open file
    # write something on it - this line may raise error
# except:
    # do something when expcetion is raised
#finally:
    # close file here instead of try so that it 100% closes instead of leaving open if expcetion is raised