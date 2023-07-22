
import string

the_numbers = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

alp_list = string.ascii_lowercase
print(alp_list)

result = ""

for i in range(len(the_numbers)):
    result += alp_list[the_numbers[i]-1]

    if i == 6 :
        result += "{"
    elif i ==(len(the_numbers)-1):
        result += "}"

print(result)

