import random

def nBitRandom(n):
    return(random.randrange(2**(n-1)+1, 2**n-1))

def getPrime(n): 
    while True: 
        prime_candidate = nBitRandom(n) 
        t = testBigNumbers(prime_candidate)
        if t:
            return prime_candidate

#Miller-Rabin-Test
def testBigNumbers(miller_rabin_candidate):
    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1
   
    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)
   
    def trialComposite(round_tester):
        if pow(round_tester, evenComponent, 
               miller_rabin_candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent,
                   miller_rabin_candidate) == miller_rabin_candidate-1:
                return False
        return True
   
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2,
                       miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    return True

