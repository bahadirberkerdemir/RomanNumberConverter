class UndefinedNumeralError(Exception):
    pass

class RomanNumeralSyntaxError(Exception):
    pass

def one_digit(str):
    match str:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case _:
            raise UndefinedNumeralError("Please enter a roman numeral. (I V X L C D M) ")

"""
one_digit_roman= input("Enter a roman numeral: ")
print(one_digit(one_digit_roman))
"""

def sum_sub_numerals(str):
    number = 0
    red_flag= False
    wrong_list = ["I"*4, "V"*4, "X"*4, "L"*4, "C"*4, "D"*4]

    for element in wrong_list:
        if element in str:
            red_flag = True

    if red_flag:
        raise RomanNumeralSyntaxError("A roman numeral cannot have 4 consecutive same numerals except 'M'.")
    else:
        for i in range(len(str)):
            if max(range(len(str))) >= i+1:
                if one_digit(str[i]) >= one_digit(str[i+1]):
                    number += one_digit(str[i])
                else:
                    number -= one_digit(str[i])
            else:
                number += one_digit(str[i])

        return number


two_digit_roman= input("Enter a roman numeral: ")
print(sum_sub_numerals(two_digit_roman))
