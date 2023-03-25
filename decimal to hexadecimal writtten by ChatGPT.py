decimal_num = int(input()) # replace this with the decimal number you want to convert

# define a list of hexadecimal digits
hex_digits = "0123456789ABCDEF"

# initialize an empty string to store the hexadecimal equivalent
hex_num = ""

# convert the decimal number to hexadecimal
while decimal_num > 0:
    remainder = decimal_num % 16
    hex_digit = hex_digits[remainder]
    hex_num = hex_digit + hex_num
    decimal_num //= 16

print("The hexadecimal equivalent is", hex_num)
