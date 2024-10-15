#QUICK PASSWORD GENERATOR
import random as r
import string as str
length = r.randint(6,14)
chars = [r.choice(str.ascii_lowercase),
         r.choice(str.ascii_uppercase),
         r.choice(str.digits),
         r.choice(str.punctuation)]

remChars = str.ascii_lowercase + str.ascii_uppercase + str.digits + str.punctuation

chars += [r.choice(remChars) for x in range(length-4)]
r.shuffle(chars)
password = ''.join(chars)
print("Here is your generated password: ",password)
