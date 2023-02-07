import random

sample = ["I","l","|","!","1","[","]","||","i","j"]

def genpass():
    password = []
    rng = random.randrange(16,250)
        
    for i in range(rng):
        n = random.choice(sample)
        password.append(n)
    return ''.join(password) 

for i in range(5):
    print(genpass())
