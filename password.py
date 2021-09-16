import random as rndm
#importing random under the name of rndm as i just like to

def shuffle(string):
    tempList = list(string)
    rndm.shuffle(tempList)
    return ''.join(tempList)
#shuffle function 

ul1=chr(rndm.randint(65,90))
ul2=chr(rndm.randint(65,90))
#Uppercase characters
ll1=chr(rndm.randint(97,122))
ll2=chr(rndm.randint(97,122))
#Lowercase characters
d1=chr(rndm.randint(49,57))
d2=chr(rndm.randint(49,57))
#numbers
s1=chr(rndm.randint(35,46))
s2=chr(rndm.randint(35,46))
#symbols

password = ul1+ul2+ll1+ll2+d1+d2+s1+s2
#puts the together
password = shuffle(password)
#shuffles them

print(password)
