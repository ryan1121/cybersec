
import string

# cipher text
cip = 'FXE{Pnrfne_Pvcure_Qrpbqre}'

# turn all cipher text into lowercases
cip = cip.lower()

# get a alphabet list
alp = string.ascii_lowercase

# result
res = ''

# Do ROT13 decryption
for i in range(len(cip)) :
	f = alp.find(cip[i])
	
	if f != -1 :
		ind = f+13
		if ind >= 26 :
			ind -= 26
		res += alp[ind]
	else :
		res += cip[i]
	
	
# Print out the result
print(res)
	

