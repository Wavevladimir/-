def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator"""
    return value * mult
mult_by_factor(5)

def print_number_info(num):
    """Prints whether number is even pr odd 

    Args:
        num (int): Number to be evaluted
    """
    if (num % 2) == 0:
        print('Nun is even')
    else:
        print('Num is odd')

print_number_info(20)
