#Inspired by the Numberphile video https://www.youtube.com/watch?v=azL5ehbw_24&list=UUoxcjq-8xIDTYp3uz647V5A&index=3

#NOTE: as it is this program crashed my computer which has an i7-7700K cpu that runs at 4.2 GHz

from math import sqrt

def isPrime(n):
    #a pretty rudamentary prime checking function. It's O(sqrt(n)), so it works pretty well.
    if n < 2:
        return False
    if n%2==0:
        return True if (n==2) else False
    for i in range(3, int(sqrt(n)+1), 2):
        if n%i==0:
            return False
    return True

def expand(n):#this is the core function of this program. It is recursive.

    ns = str(n)

    print "working on",n

    found = []

    for i in range(1,10,2):
        ns += str(i)
        for j in range(1,10):
            new = str(j)
            new += ns
            new = int(new)
            if isPrime(int(new)):
                deeperFound = expand(new)       #just creates a holder variable
                if deeperFound == None:
                    #if there are no deeper things to be found, then this number is a deadend and should be added to the list because it can no longer be expanded
                    found.append(new)
                    print "I found:",new
                else:
                    found.expand(deeperFound)
        ns = ns[:-1]    #takes off the digit we just tested on the end

    return (found if found != [] else None)

def main():
    expand(5)#just a test number. The program should run with a non-prime number, but the results will only be meaningful if the seed is prime.

if __name__ == "__main__":
    main()
