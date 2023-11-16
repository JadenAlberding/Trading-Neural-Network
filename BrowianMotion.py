
#Browian motion function influenced by https://sites.me.ucsb.edu/~moehlis/APC591/tutorials/tutorial7/node2.html,
#https://scipy-cookbook.readthedocs.io/items/BrownianMotion.html, and 
#https://sites.me.ucsb.edu/~moehlis/APC591/tutorials/tutorial7/node2.html

import random
import math

def randomNum(delta, n, value, t, j):
    v = value
    count = j
    print(count)
    for i in range(n):
        v = random.gauss(v,delta)
        stock = open("Stock_Data.txt", "a")
        stock.write(str(count))
        stock.write(",")
        stock.write(str(v))
        stock.write("\n")
        stock.close()
        print(i)
        count += 1/n
        print(count)
        #print(count)
        
        #v = math.exp( (- (x **2 ))/ (2 * t )) / math.sqrt( math.pi * 2)
        #print(v)
    return v

def BrowianMotion(delta, N, dt, T, initalValue):
    value = initalValue
    for i in range(T):
        value = randomNum(delta, N, value,T, i)
        

def main():
    delta = 2  #  helps in the scale and standard deviation
    T = 30  #Total amount of iterations
    N = 100 # Number of steps per iteration
    initialPrice = 10 

    dt = T/N
    #randomNum(delta,N,initialPrice, T)
    BrownianMotion(delta, N, dt, T, initialPrice )

if __name__ == "__main__":
    main()
        