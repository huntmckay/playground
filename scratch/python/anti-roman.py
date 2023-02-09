'''
chr() 	Converts an integer to a character
ord() 	Converts a character to an integer
len() 	Returns the length of a string
str() 	Returns a string representation of an object
'''
cipher = "MJIIH VYUWB MNOZZ MOLJLCMY"

cipher = cipher.split(" ")

def decode(cipher):
    
    r = []
    for i in cipher:
        i = i.lower()
        for x in i:
            r.append(chr((ord(x)+6)))
    return r 

print(decode(cipher))
