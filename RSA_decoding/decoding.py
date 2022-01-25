import math
import sys
from Power_Pow import power_pow

class Decoding:
    def __init__(self):
        pass
    
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv2(self, c, m):
        g, x, y = self.egcd(c, m)
        if g != 1:
            raise Exception('   Modular inverse does not exist')
        else:
            return x % m

    def decode_message(self, c, n, y, m):
        d = self.modinv2(c,m)
        x = power_pow(y, d, n)      

        return x

