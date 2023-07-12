
with open('output.txt','r') as f:
    outputList = f.readlines()

# Define a result string variable
result = ''

# Using for loop to read line by line
for i in outputList :
    result += chr(int(i))

print("Result : ", result)
