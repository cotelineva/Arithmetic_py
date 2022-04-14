'''
a. Read numbers until you read 0 and show the amount of 0s in the result 
of the multiplcation of those numbers.
'''


l = []


def reading(): 

    n = int(input("n= ")) 
    l.append(n) 

    while n != 0: #we read until we get the first 0
        n = int(input("n= ")) 
        l.append(n)

    print("The sequence is: ",l)




def multiply(l):

    reading()
    p = 1 

    for el in range (len(l)-1): #we multiply each number, exept the last one (because it's 0)
        p*=l[el]

    print("Result is: ",p)

    digits = [] #we build an array of the digits of the result
    while p != 0:
        digits.append(p%10)
        p//=10

    print("Number of 0s in the result: " , digits.count(0))


produs(l)
