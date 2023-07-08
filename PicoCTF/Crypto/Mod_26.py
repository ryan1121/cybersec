
import string

# String to decode
str_decode = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"

strlist = string.ascii_uppercase
for i in range(13):
    print("'%s' : '%s', "%(strlist[i+13], strlist[i]))

# Create a mapping dictionary
rot13_map = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'A' : 'N',
    'B' : 'O',
    'C' : 'P',
    'D' : 'Q',
    'E' : 'R',
    'F' : 'S',
    'G' : 'T',
    'H' : 'U',
    'I' : 'V',
    'J' : 'W',
    'K' : 'X',
    'L' : 'Y',
    'M' : 'Z',
    'n' : 'a',
    'o' : 'b',
    'p' : 'c',
    'q' : 'd',
    'r' : 'e',
    's' : 'f',
    't' : 'g',
    'u' : 'h',
    'v' : 'i',
    'w' : 'j',
    'x' : 'k',
    'y' : 'l',
    'z' : 'm',
    'N' : 'A',
    'O' : 'B',
    'P' : 'C',
    'Q' : 'D',
    'R' : 'E',
    'S' : 'F',
    'T' : 'G',
    'U' : 'H',
    'V' : 'I',
    'W' : 'J',
    'X' : 'K',
    'Y' : 'L',
    'Z' : 'M'
}

for i in str_decode :
    try :
        print(rot13_map[i], end='')
    except :
        print(i, end='')