with open('output.txt','r') as f:
    outputList = f.readlines()

# Define a result string variable
result = ''

# Using for loop to read line by line
for i in outputList :
    # We are using the int() function to convert the 'i' variable which is string data type to integer data type
    result += chr(int(i))

print("Result : ", result)
