import pickle



class primes(object):
    def __init__(self,m,var):
        self.number = m
        self.twin = var

    def display(self,i):
        if self.twin == True:
            print("The twin prime", self.number, " is at index", i+1)
        else:
            print("The prime number ", self.number," is at index", i+1)
    def setTwin(self,var):
        self.twin =var
            
def prime_generator(N):
    #find all prime numbers and double primes less than N
    primeslist =[]
    length_primes =2
    primeslist.append(primes(2,True))
    primeslist.append(primes(3,True))

    #This code bellow will generate the prime numbers and twin primes 
    
    for x in range(4,N):

        for i in range(length_primes):
            
            if( x%((primeslist[i]).number) ==0):
                break
            elif (i == (length_primes-1)):
                if((x-2)==(primeslist[length_primes-1].number)):
                    primeslist[length_primes-1].setTwin(True)
                    primeslist.append(primes(x,True))
                    length_primes =length_primes+1
                else:
                    primeslist.append(primes(x,False))
                    length_primes =length_primes+1
    return primeslist, length_primes

def test():
    primeslist, length_primes = prime_generator(50)
    for i in range(0,length_primes):
        primeslist[i].display(i)


primeslist, length_primes = prime_generator(50)
with open("primes.pkl", 'wb') as f:
    pickle.dump(primeslist,f)


primeslist = pickle.load(open('primes.pkl','rb'))
print(primeslist);