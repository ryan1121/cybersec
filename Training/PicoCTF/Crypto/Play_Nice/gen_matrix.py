
alp = '0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q'

# Create a 6x6 matrix
for i in range(6) : 
	ind = 6*i
	print(list(alp[ind:ind+6]))

# Create cipher pairs to decrypt
cip = 'herfayo7oqxrz7jwxx15ie20p40u1i'
cip_list = [cip[j*2:(j*2)+2] for j in range(15)]
print(cip_list)
