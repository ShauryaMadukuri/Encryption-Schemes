# Cryptography
```text
Here we use the term cryptography to refer to the study of encrypting and decrypting data.
In this module, I have implemented couple od encryption and decryption schemes levraging hard computation problems.
```

## Regev Encryption and Decryption:

-> This is based off Learing with errors problem(LWE)(*hard computation problem*) and is a scheme that is used to encrypt data.
-> The idea is to encrypt a single bit using a random key and a random noise.
-> This is one of popular public-key encryption schemes.

File:
1. The Regev Encryption scheme is implemented in the file `Reg_Encryption.py` in the `Regev Encryption Scheme` folder.
1. This is pacakged object orientedly.
1. run the file `Testing.py` to test the encryption and decryption.

**Observation:**
- we can see the at each run the public, secret key and the ciphertext are different.
- But the encrypted and decrypted bits are the same.


## Fully Homomporphic Encryption(FHE):

-> This Ecncription scheme allows us to have arthematics done on the cipher text  instead directly on plain text.
-> This scheme allows the safe trasfer of data between two parties.

File:
1. The FHE scheme is implemented in the file `FHE.py` in the `Fully Homomorphic Encryption` folder.
1. run this file to test the encryption, arthematic operations on cipher text and decryption of the result.

**Obervation:**
- The secret key and the cipher text are different at each run.
- This is because we input a  random noise for the geration of cipher text.


***References***
- A Decade of Lattice Cryptography by *Chris Peikert*
- The Learning with Errors Problem by *Oded Regev*
- Lattice Cryptography: an introduction by *Daniele Micciancio*


***acknowledgements***
- Venkata Koppula, Assistant Professor, IIT Delhi