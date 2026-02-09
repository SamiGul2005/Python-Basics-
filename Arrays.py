NumArray=[]

def initialise():
    for i in range(10):
        Num=int(input("Enter Number: "))
        NumArray.append(Num)

def OutputArray():
    print(NumArray)



def sum():
    total=0
    for i in range(10):
        total=total+NumArray[i]
    return total




def BubbleSort():
    upper=len(NumArray)-1  #upper will be one below the len of the array because we use arr[i+1] later, if upper=len(array) then it will go out of range
    low=0
    swap=True  #we set swap to true
    while swap==True: #and upper>=low: #We make a conditional loop that if swap remains true and the upper value is above, or equal to, lower, then the loop continues
        swap=False #we set the swap to False first thing in the loop, so incase it doesnt get changed later in the loop, the loop breaks
        for i in range(upper): #we make a count controlled for loop for all the values of the array, so we can check all of them 
            if NumArray[i]>NumArray[i+1]: #we put a condition to see if a value is greater than the one infront of it. This is where the "len(array)-1" is needed, so we dont go out of range
                NumArray[i],NumArray[i+1]=NumArray[i+1],NumArray[i] #if the contional applies, we swap value
                swap=True # and we set swap to true, implying that the loop should continue
        upper-=1 #we decrement upper to imply that a portion of the array has been sorted already.

#note: The "swap=False" in the start and then "swap=True" in the middle are to check if the array has been sorted completely or not. 
# If the array is completely sorted, the "swap= True" wont be executed, and the swap would remain False. Thereby breaking the loop. 
                

def insertion():
    global NumArray

    upper=len(NumArray)
    lower=0
    
    #Upper value is the length of thew array and the lower value is a constant zero

    for index in range(lower+1, upper): #the loop is taken from 1 to len(arr), because later in the code we will use the previos val of the index. SO to avoid out of range errors
        key=NumArray[index] # The key is the index of the loop
        place=index-1 #place is the index before the current one. This is why we use one val above the lowest one.
        if NumArray[place]>key: # we compare the index value of place, a value below the indexed value, and the indexed value
            while place>=lower and NumArray[place]>key: # we out a conditional loop, so as long as place is greater than lower and array of value of place is greater than the key, the value above, the loop keep s executing
                NumArray[place],NumArray[place+1]=NumArray[place+1],NumArray[place] # the value of place and key are swappped 
                place-=1 #place is decremented, so it eventually reached lower
                #this loop check all indexes beneath place to ensure they are not above the key value, and if they are, they get swapped for the value above. 


def Insertion():
    global NumArray
    NumberOfItems=len(NumArray) #Number of items in the Array
    lower=0 #The First Element of the array
    for pointer in range(lower+1, NumberOfItems): #Looping from the second element till the end of Array, and picking up each element one at a time
        ItemToBeInserted=NumArray[pointer] #Picking up the element at the pointer index
        CurrentItem=pointer-1 #Current item is pointing to the last elment of the sorted list
        while (CurrentItem>=lower) and (NumArray[CurrentItem]>ItemToBeInserted): #
                NumArray[CurrentItem+1]=NumArray[CurrentItem]
                CurrentItem-=1
        NumArray[CurrentItem+1]=ItemToBeInserted                



#Linear Search
def search(num):
    found=False
    i=0
    while i<10 and found==False:
        if NumArray[i]==num:
            found=True
        i=i+1
    return found        


#Binary Search 
def BinarySearch(SearchItem):
    found=False
    SearchFailed=False
    first=0
    last=len(NumArray)-1     #set boundaries of search area
    while not found and not SearchFailed:
        middle=(first+last)//2     #the middle current of search area
        if NumArray[middle]==SearchItem:
            found=True 
        else:
            if first>=last:       #No search area left
                SearchFailed=True
            else:
                if NumArray[middle]>SearchItem:   #So it must be in the first half
                    last=middle-1  #move upper boundary
                else:    #must be in the second half
                    first=middle+1    
    if found==True:
        print(middle)
    else:
        print("Item not present in array")                    



#Assigning a 2D array
NumArray2=[[0 for j in range(5)] for i in range(2)]
#                     (Coloumns)           (rows)

#initialising an Array
def Initialise():
    for i in range(2): #rows
        for j in range(5): #coloumns
            Num=int(input("Enter a number: "))
            NumArray2[i][j]=Num 
    print(NumArray2) 

# Initialise() 

#Sum of the 2D array
def sum():
    total=0
    for i in range(2):
        for j in range(5):
           total=NumArray2[i][j]+total
    print("the total is ", total)
# sum()           

# Linear Search in 2D arrays
def search():
    num=int(input("Enter a number: "))
    found=False
    for i in range(2):
        for j in range(5):
            if NumArray2[i][j]==num:
                found=True
    return found            
# print(search())

#LinearSearch Efficient
def searchEfficient():
    num=int(input("Num: "))
    found=False
    i=0
    while i<5 and found==False:
        j=0
        while j<2 and found==False:
            if NumArray2[i][j]==num:
                found=True
            else:    
                j+=1
        i+=1        
    return found             

#BubbleSort in 2D array
def BubbleSort():
    cycles=5
    NoMoreSwaps=False
    while NoMoreSwaps==False:
        NoMoreSwaps=True
        for i in range(cycles-1):
            if NumArray2[0][i]>NumArray2[0][i+1]:
                
                temp=NumArray2[0][i]
                NumArray2[0][i]=NumArray2[0][i+1]
                NumArray2[0][i+1]=temp
                
                temp=NumArray2[1][i]
                NumArray2[1][i]=NumArray2[1][i+1]
                NumArray2[1][i+1]=temp
                NoMoreSwaps=False 
        cycles-=1