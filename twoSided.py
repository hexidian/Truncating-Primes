#Inspired by the Numberphile video https://www.youtube.com/watch?v=azL5ehbw_24&list=UUoxcjq-8xIDTYp3uz647V5A&index=3

#NOTE: as it is this program crashed my computer which has an i7-7700K cpu that runs at 4.2 GHz

from math import sqrt

MAXLENGTH = 9

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

    ns = str(n) #simply the string verison of n

    if len(ns) < 6:#this way we only print it when we tick over the smaller numbers, which is like ticking over a big digit if that makes sense
        print "working on",n

    if len(ns) > MAXLENGTH: #for now we will only look at short ones, so that it doesn't crash my computer
        return []
        #anything that returns a [] shall indicate that there were no dead ends before the length limit
    found = []

    stupidMarkerThatShouldHaveABetterNameButImLazy = False

    for i in [1,3,7,9]:#we only need try adding odd numbers, because any number ending with an even number is going to be non-prime (obviously except for 2 itself). We also don't need to check 5 because the number will be a multiple of 5
        ns += str(i)
        for j in range(1,10):#we can't make the same simplification as before because this number is going to be appended as the most significant digit
            new = str(j)
            new += ns
            new = int(new)
            if isPrime(int(new)):
                deeperFound = expand(new)       #just creates a holder variable
                if deeperFound == None:
                    #if there are no deeper things to be found, then this number is a deadend and should be added to the list because it can no longer be expanded
                    found.append(new)
                    print "I found:",new
                    stupidMarkerThatShouldHaveABetterNameButImLazy = True
                elif deeperFound != []:
                    found.extend(deeperFound)
                    stupidMarkerThatShouldHaveABetterNameButImLazy = True
        ns = ns[:-1]    #takes off the digit we just tested on the end

    return [] if stupidMarkerThatShouldHaveABetterNameButImLazy == False else found if found != [] else None #what a python line

def main():
    found = []
    for i in [2,3,5,7]:
        found.extend(expand(i))
    print found
if __name__ == "__main__":
    main()
