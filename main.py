import tkinter as tk


class UndefinedNumeralError(Exception):
    pass

class RomanNumeralSyntaxError(Exception):
    pass

def base_numeral_conversions(roman_numeral):
    match roman_numeral:
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


def roman_to_arabic_numeral():
    number = 0
    red_flag= False
    wrong_list = ["I"*4, "V"*4, "X"*4, "L"*4, "C"*4, "D"*4]
    roman_numeral= romanNumeralInput.get().upper()

    for element in wrong_list:
        if element in roman_numeral:
            red_flag = True

    if red_flag:
        raise RomanNumeralSyntaxError("A roman numeral cannot have 4 consecutive same numerals except 'M'.")
    else:
        for i in range(len(roman_numeral)):
            if max(range(len(roman_numeral))) >= i+1:
                if base_numeral_conversions(roman_numeral[i]) >= base_numeral_conversions(roman_numeral[i + 1]):
                    number += base_numeral_conversions(roman_numeral[i])
                else:
                    number -= base_numeral_conversions(roman_numeral[i])
            else:
                number += base_numeral_conversions(roman_numeral[i])

        outputNumberLabel.config(text=str(number))

#### TKINTER INTERFACE ####

window = tk.Tk()
window.title("Roman to Arabic Numeral Converter")
window.minsize(300, 500)
window.config(background="light green")


inputTextLabel = tk.Label(window, text="Enter A Roman Numeral",bg="light green",fg="black", font="bold",pady=10)
inputTextLabel.pack()

romanNumeralInput = tk.Entry(width=20)
romanNumeralInput.pack()

submitButton = tk.Button(text="Convert", height=1, command=roman_to_arabic_numeral)
submitButton.pack()

outputNumberLabel = tk.Label(window, text="",bg="light green",fg="black", font="bold", pady=10)
outputNumberLabel.pack()

window.mainloop()