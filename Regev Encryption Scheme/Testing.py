import Reg_Encryption
from Reg_Encryption import *

## bit inputs:
#for scheme 1:
bit1_1=0
bit1_2=1

#for scheme 2:
bit2_1=0
bit2_2=1



scheme1=regev_encryption(76,23,503)

print("Encrypted bit1: {}".format(bit1_1))
print("Encrypted bit2: {}".format(bit1_2))
# print("Public Key: {}".format(scheme1.pk.mat))
print("Secret Key: {}".format(scheme1.sk.mat))

ciphertext1 = scheme1.encrypt(bit1_1)
ciphertext2 = scheme1.encrypt(bit1_2)

print("Ciphertext 1: {}".format(ciphertext1.transpose().mat[0]))
print("Ciphertext 2: {}".format(ciphertext2.transpose().mat[0]))

bit1 = scheme1.decrypt(ciphertext1)
bit2 = scheme1.decrypt(ciphertext2)
print("Decryption of ciphertext1 : {}".format(bit1))
print("Decryption of ciphertext2 : {}".format(bit2))
print('\n')



#another:
scheme2=regev_encryption(76,23,503)


print("Encrypted bit1: {}".format(bit2_1))
print("Encrypted bit2: {}".format(bit2_2))
# print("Public Key: {}".format(scheme1.pk.mat))
print("Secret Key: {}".format(scheme2.sk.mat))

ciphertext1 = scheme2.encrypt(bit2_1)
ciphertext2 = scheme2.encrypt(bit2_2)

print("Ciphertext 1: {}".format(ciphertext1.transpose().mat[0]))
print("Ciphertext 2: {}".format(ciphertext2.transpose().mat[0]))

bit1 = scheme2.decrypt(ciphertext1)
bit2 = scheme2.decrypt(ciphertext2)
print("Decryption of ciphertext1 : {}".format(bit1))
print("Decryption of ciphertext2 : {}".format(bit2))