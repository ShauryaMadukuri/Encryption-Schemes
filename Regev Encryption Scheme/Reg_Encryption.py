import numpy as np
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
        tmp = self.mat.copy()
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                tmp[i][j] = self.mat[i][j] % q
        return Matrix(tmp)

    def dimensions(self):
        print(str(len(self.mat)) + "x" + str(len(self.mat[0])))


def KeyGen(m, n, q):
    A_bar = Matrix([np.random.randint(0, q, size=n).tolist() for i in range(m)])
    A_bar = A_bar.transpose()
    rng = q // (m * 4)
    sk = Matrix([np.random.randint(0, q, n).tolist()])
    e = Matrix([np.random.randint(-rng+1, rng, m).tolist()])
    b = ((sk * A_bar) + e).modulus(q)
    pk = A_bar
    pk.mat.append(b.mat[0])
    return pk, sk


class regev_encryption:
    def __init__(self, m, n, q):
        self.m = m
        self.n = n
        self.q = q
        self.pk, self.sk = KeyGen(m, n, q)

    def encrypt(self, bit):
        x = Matrix([np.random.randint(2, size=self.m).tolist()])
        x = x.transpose()
        tmp = Matrix([[0 for i in range(self.n)]])
        tmp.mat[0].append(bit * int((self.q + 0.5) // 2))
        tmp = tmp.transpose()
        cipher = ((self.pk * x) + tmp).modulus(self.q)
        return cipher

    def decrypt(self,cipher):
        tmp = self.sk.negative()
        tmp.mat[0].append(1)
        decipher_mat = (tmp * cipher).modulus(self.q)
        decipher = decipher_mat.mat[0][0]
        if decipher >= -self.q//4 and decipher < self.q//4:
            return int(0)
        elif decipher >= self.q//4 and decipher < (3*self.q)//4:
            return int(1)
        else:
            print("There was some error decrypting the given ciphertext!!")



#                                                            @author: Shaurya