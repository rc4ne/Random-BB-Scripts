import itertools

string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=\|~`?/><,.' #characters to be included, generally will be in hex string format
file = open('brutedb.txt', 'w') #file where it will be stored
for p in itertools.product(string, repeat=4): #repeat will be the length of tokens 
	writing = ''.join(p) + '\n'
	file.write(writing)
file.close()
