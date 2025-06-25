class Error(Exception):
    """base class for other expressions"""
    pass
class ValueTooSmallError(Error):
    """raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """raised when the input value is too large"""
    pass
number=10
while True:
    try:
        i_num=int(input("enter a number:"))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("this value is too small try again!")
        print()
    except ValueTooLargeError:
        print("this value is too large try again!")
print()
print("congratulations! you guessed it correctly.")
            
    

    
    
