import random

sample = ["I","l","|","!","1","[","]","||","i","j"]

password = []
rng = random.randrange(1,99)

for i in range(rng):
    n = random.choice(sample)
    password.append(n)
    
print(''.join(password))
