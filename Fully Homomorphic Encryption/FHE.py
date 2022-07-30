import numpy as np
import random
import copy

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat[0]):
            print("Can't add these two matrices!!")
            return
        C = [[0 for i in range(len(self.mat[0]))] for j in range(len(self.mat))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                C[i][j] = self.mat[i][j] + other.mat[i][j]
        return Matrix(C)

    def __mul__(self, other):
        if len(self.mat[0]) == len(other.mat):
            C = [[0 for i in range(len(other.mat[0]))] for j in range(len(self.mat))]
            for i in range(len(self.mat)):
                for j in range(len(other.mat[0])):
                    for k in range(len(self.mat[0])):
                        C[i][j] += self.mat[i][k] * other.mat[k][j]
            return Matrix(C)
        else:
            print("Can't multiply these two matrices!!")

    def negative(self):
        C = copy.deepcopy(self.mat)
        for i in range(len(C)):
            for j in range(len(C[0])):
                C[i][j] = -C[i][j]
        return Matrix(C)

    def transpose(self):
        C = [[0 for i in range(len(self.mat))] for i in range(len(self.mat[0]))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                C[j][i] = self.mat[i][j]
        return Matrix(C)

    def modulus(self, q):
        tmp = copy.deepcopy(self.mat)
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                    tmp[i][j] = self.mat[i][j] % q
        return Matrix(tmp)

    def modulus2(self, q):
        tmp = copy.deepcopy(self.mat)
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                    tmp[i][j] = self.mat[i][j] % q
                    if (tmp[i][j] >= q // 2 and q % 2 == 0) or (tmp[i][j] > q // 2):
                        tmp[i][j] -= q
        return Matrix(tmp)

    def kroneckerprod(self, B):
        res = []
        for i in range(len(self.mat)):
            for j in range(len(B.mat)):
                res.append([])
                for k in range(len(self.mat[0])):
                    res[len(B.mat)*i+j] += [self.mat[i][k] * elem for elem in B.mat[j]]
        return Matrix(res)

    def dimensions(self):
        print(str(len(self.mat)) + "x" + str(len(self.mat[0])))

def KeyGen(n, q):
    sk_bar = Matrix([np.random.randint(-q, q, n-1).tolist()])
    sk = Matrix([sk_bar.negative().mat[0] + [1]])
    return sk, sk_bar

def encrypt(bit, sk_bar, n, q):
    c_bar = Matrix([np.random.randint(-q, q, n-1).tolist()])
    e = random.randint(-q//16, q//16) * 2
    e += bit
    c_bar_t = c_bar.transpose()
    c = ((sk_bar * c_bar_t).mat[0][0] + e)
    cipher = Matrix([c_bar.mat[0] + [c]])
    return cipher

def decrypt(cipher, sk, n, q):
    cipher_t = cipher.transpose()
    e = (sk * cipher_t)
    bit = e.mat[0][0] % 2
    return bit

if __name__ == "__main__":
    n = 60
    q = 1063
    sk, sk_bar = KeyGen(n, q)
    print("n : {}".format(n))
    print("q : {}".format(q))
    print("Secret Key: {}".format(sk.mat[0]))

    ciphertext0v0 = encrypt(0, sk_bar, n, q)
    ciphertext1v0 = encrypt(1, sk_bar, n, q)
    ciphertext0v1 = encrypt(0, sk_bar, n, q)
    ciphertext1v1 = encrypt(1, sk_bar, n, q)
    # print("Ciphertext 0 v0: {}".format(ciphertext0v0.mat[0]))
    # print("Ciphertext 1 v0: {}".format(ciphertext1v0.mat[0]))
    # print("Ciphertext 0 v1: {}".format(ciphertext0v1.mat[0]))
    # print("Ciphertext 1 v1: {}".format(ciphertext1v1.mat[0]))
    bit0v0 = decrypt(ciphertext0v0, sk, n, q)
    bit1v0 = decrypt(ciphertext1v0, sk, n, q)
    bit0v1 = decrypt(ciphertext0v1, sk, n, q)
    bit1v1 = decrypt(ciphertext1v1, sk, n, q)
    print("Decryption of ciphertext 0 v0: {}".format(bit0v0))
    print("Decryption of ciphertext 1 v0: {}".format(bit1v0))
    print("Decryption of ciphertext 0 v1: {}".format(bit0v1))
    print("Decryption of ciphertext 1 v1: {}".format(bit1v1))

    ciphersum00 = ciphertext0v0 + ciphertext0v1
    ciphersum01 = ciphertext0v0 + ciphertext1v1
    ciphersum11 = ciphertext1v0 + ciphertext1v1
    # print("Ciphertext sum 00: {}".format(ciphersum00.mat[0]))
    # print("Ciphertext sum 01: {}".format(ciphersum01.mat[0]))
    # print("Ciphertext sum 11: {}".format(ciphersum11.mat[0]))
    bitsum00 = decrypt(ciphersum00, sk, n, q)
    bitsum01 = decrypt(ciphersum01, sk, n, q)
    bitsum11 = decrypt(ciphersum11, sk, n, q)
    print("Decryption of ciphertext sum 00: {}".format(bitsum00))
    print("Decryption of ciphertext sum 01: {}".format(bitsum01))
    print("Decryption of ciphertext sum 11: {}".format(bitsum11))

    cipherprod00 = ciphertext0v0.kroneckerprod(ciphertext0v1)
    cipherprod01 = ciphertext0v0.kroneckerprod(ciphertext1v1)
    cipherprod11 = ciphertext1v0.kroneckerprod(ciphertext1v1)
    # print("Ciphertext prod 00: {}".format(cipherprod00.mat[0]))
    # print("Ciphertext prod 01: {}".format(cipherprod01.mat[0]))
    # print("Ciphertext prod 11: {}".format(cipherprod11.mat[0]))
    bitprod00 = decrypt(cipherprod00, sk.kroneckerprod(sk), n, q)
    bitprod01 = decrypt(cipherprod01, sk.kroneckerprod(sk), n, q)
    bitprod11 = decrypt(cipherprod11, sk.kroneckerprod(sk), n, q)
    print("Decryption of ciphertext prod 00: {}".format(bitprod00))
    print("Decryption of ciphertext prod 01: {}".format(bitprod01))
    print("Decryption of ciphertext prod 11: {}".format(bitprod11))

