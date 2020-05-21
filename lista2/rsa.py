import argparse
import sys
import random
import hashlib
import math
import miller_rabin




# Generate big prime numbers with given size(in bits).
# To check if number is prime when number fits into 64-bit unsigned,
# program use deterministic variant, otherwise program uses Miller-Rabin nondeterministic 
# algorithm with probability of incorrectness much smaller than 4^(-32).
class BigPrime:
    @staticmethod
    def gen_prime_candidate(size):
        p = random.getrandbits(size)

        #make sure that MSB and LSB is equivalent to 1
        correction = 1 << (size-1) | 1
        return p | correction
    
    
    @staticmethod
    def is_prime(p):
        #Perform Miller-Rabin primality test on the arbitrary precision int.
        #A deterministic variant is auto-selected if n fits into 64-bit unsigned;
        #otherwise, the probablistic variant is used, and k determines the number of
        #test rounds to perform.
        return miller_rabin.miller_rabin(p, 32)


    @staticmethod
    def gen_prime(size):
        p = BigPrime.gen_prime_candidate(size)
        while not BigPrime.is_prime(p):
            p = BigPrime.gen_prime_candidate(size)
        return p




# Mathematic function wchich i couldn't find in math module.
class Utils:
    @staticmethod
    def lcm(a, b):
        return (a*b) // math.gcd(a, b)


    @staticmethod
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = Utils.egcd(b % a, a)
            return g, x - (b // a) * y, y


    @staticmethod
    def mod_inv(a, m):
        g, x, y = Utils.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m




# Generate public and private key with given length.
# Decrypt and encrypt files with RSA algorithm.
class RSA:
    @staticmethod
    def write_key(path, n, x):
        try:
            with open (path, "w") as file:
                file.write(str(n) + '\n' + str(x))
        except:
            print("Can't find file: ", path)
            sys.exit(1)


    @staticmethod
    def read_key(path):
        try:
            with open (path, "r") as file:
                splited = file.read().split('\n')
                return int(splited[0]), int(splited[1])
        except:
            print("Can't find file: ", path)
            sys.exit(1)


    @staticmethod
    def gen_keys(size):
        e = 65537

        p = BigPrime.gen_prime(size//2)
        q = BigPrime.gen_prime(size//2)
        phi = Utils.lcm(p-1, q-1)

        while math.gcd(e, phi) != 1 or abs(p-q) >> (size//16) == 0:
            p = BigPrime.gen_prime(size//2)
            q = BigPrime.gen_prime(size//2)
            phi = Utils.lcm(p-1, q-1)

        n = p*q
        d = Utils.mod_inv(e, phi)

        RSA.write_key("key.pub", n, e)
        RSA.write_key("key.prv", n, d)
        

    @staticmethod
    def encrypt(plain_text):
        n, e = RSA.read_key("key.pub")
        encrypted = ''.join(str(pow(ord(char), e, n))+"." for char in plain_text)
        print(encrypted[:len(encrypted)-1])


    @staticmethod
    def decrypt(plain_text):
        n, d = RSA.read_key("key.prv")
        try:
            decrypted = ''.join(str(chr(pow(int(char), d, n))) for char in plain_text.split("."))
            print(decrypted)
        except:
            print("Can't encrypt a file, key.prv doesn't match.")
            sys.exit(1)




def main():
    parser = argparse.ArgumentParser(description='Program lets you generate private and public keys with given length (in bits) and encrpyt or decrypt a file.')
    parser.add_argument('--gen-keys', choices=[64, 128, 256, 512, 1024, 2048, 3072, 4096], type=int, help='Genreate private and public key with given length.')
    parser.add_argument('--encrypt', type=str, help='Encrypt a file  with public key.')
    parser.add_argument('--decrypt', type=str, help='Decrypt a file  with private key.')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        if(args.gen_keys):
            RSA.gen_keys(args.gen_keys)
        if(args.encrypt):
            RSA.encrypt(args.encrypt)
        if(args.decrypt):
            RSA.decrypt(args.decrypt)
    else:
        parser.parse_args(["--help"])




if __name__ == '__main__':
    main()