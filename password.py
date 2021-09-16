import random as rndm
#importing random under the name of rndm

def shuffle(string):
    tempList = list(string)
    rndm.shuffle(tempList)
    return ''.join(tempList)
#defning shuffle as a fnction which takes 
#all the string in a list and shuffles them arounds 

ul1=chr(rndm.randint(65,90))
ul2=chr(rndm.randint(65,90))
ll1=chr(rndm.randint(97,122))
ll2=chr(rndm.randint(97,122))
d1=chr(rndm.randint(49,57))
d2=chr(rndm.randint(49,57))
s1=chr(rndm.randint(35,46))
s2=chr(rndm.randint(35,46))

password = ul1+ul2+ll1+ll2+d1+d2+s1+s2
password = shuffle(password)

print(password)
