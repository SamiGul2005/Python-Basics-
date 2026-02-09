#Factorials
def fact(num):
    if num>1:
        return num*fact(num-1)
    else:
        return 1

#print(fact(5))

#Print i - 50

    def num(i):
        if i<=50:
            print(i) 
            num(i+1)

#num(1)    

#Sum of 1 to n
def sum(n):
    if n>=1:
        return n + sum(n-1)
    else:
        return 0
#print(sum(3))    

#prints elements of list from last to first
arr=[1,2,3,4,5]

def export(lenArr):
    if lenArr>=1:
        print( arr[lenArr-1])
        export(lenArr-1)
#export(len(arr))
        
#Q5
def count(num):
    if num//10==0:
        return 1
    return 1+count(num//10)
#print(count(9876543210))

#Length of a string
def lenstr(str):
    if str!="":
        return 1+ lenstr(str[1:])
    else:
        return 0
#print(lenstr("abcd"))    

#Sum of digits of a number
def sumDigits(num):
    if num!=0:
        num=str(num)
        return int(num[:1]) + sumDigits(int(num[1:]))
#print(sumDigits(123))    
    

#Factorial of n, but also tracks number of recursive calls

def fact(n):
    global call
    call+=1
    print(f" call number {call} when n equals {n}")
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result