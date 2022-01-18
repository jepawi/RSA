from math import *
import random
from FileConfiguration import FileConfiguration
import os
from generate_prime_number import getPrime

p = None
q = None

prime_length = 1000

prime_numbers = []

def getRandomPrimeNumbers2(bit):  

    global prime_length

    b1 = 10**bit
    b2 = int(str(b1),2)
    b3 = int(floor(len(str(b2))/2))
    print("     Primzahllänge: " + str(b3))
    prime_length = int(floor(b3/300*1000))

    global p
    global q
    p = getPrime(prime_length)
    q = getPrime(prime_length)
    while p == q:
        q = getPrime(prime_length)

    while 0.1<log2(p)-log2(q)<30:
        q = getPrime(prime_length)
        while p == q:
            q = getPrime(prime_length)

def enterPrimeNumbers():
    global p
    global q
    while True:
        try:
            p = int(input("     Primzahl 1:      "))
            break
        except:
            pass

    while True:
        try:
            q = int(input("     Primzahl 2:      "))
            break
        except:
            pass

def generateKey():

    while True:
        x = input("     Zufällige Primzahlen nehmen: [y/n]: ")
        if x == 'y' or x == 'n':
            if x == 'y':
                while True:
                    x2 = input("     So viele Bits soll deine Zahl haben: ")
                    try:
                        x3 = int(x2)
                        getRandomPrimeNumbers2(x3)
                        break
                    except Exception as e:
                        print(e)
                        pass
                break
            else:
                enterPrimeNumbers()
                break
        else: 
            pass


    n = p*q
    m = (p-1)*(q-1)

    c = None

    for i in range(2,1000000):
        if (m%i) != 0:
            primes = getPrimes(i)
            t = True
            for p2 in primes:
                if m%p2 == 0:
                    t = False
                    break
            if t:
                c = i
                break

    cfg = FileConfiguration('Files/public_key')
    cfg2 = FileConfiguration('Files/private_key')
    cfg.set('value.n', n)
    cfg.set('value.c', c)
    cfg.save()
    cfg2.set('value.n', n)
    cfg2.set('value.m', m)
    cfg2.set('value.c', c)
    cfg2.set('value.p', p)
    cfg2.set('value.q', q)
    cfg2.save()

def getPrimes(zahl):
    primzahlen = []
    for p2 in prime_numbers:
        if p2 <= zahl:
            primzahlen.append(p2)  
    i = 0
    primfaktoren = []
    while zahl > 1:
        try:
            while zahl % primzahlen[i] == 0:
                if zahl == 0:
                    break
                zahl = zahl%primzahlen[i]
                primfaktoren += [primzahlen[i]]
            i += 1
        except:
            pass
    return primfaktoren

def getSmallPrimeNumbers(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            prime_numbers.append(p)