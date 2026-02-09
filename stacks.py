#Stack explained
#Follows Last-in-First-Out 

stack=[0 for i in range(10)] 

basePointer=0 #Refers to the first index of the Array
topPointer=-1 #Refers to the last item entered in the array. For an empty stack, it is declared to -1
stackFull=len(stack) #Lenght of stack


#Functions to Push(or add) items into the Stack
#Basic Stack
def Push(item):
    global topPointer
    if topPointer<stackFull-1: #This condition checks if the stack has space for more elements. The stackfull is subtracted because the topPointer points to the last item entered, and the  highest index for a 10 index array is 9(stackfull-1)
        topPointer+=1 
        stack[topPointer]=item #if it does, the topPointer is incremented and the item is added to the intex of the new topPointer 
    else:
        print("Stack is full, cant push!")   #if it doesnt, a message is displayed
    print(stack)
num=int(input("num: "))
Push(num)

#Efficient Stack
#This stack is more efficient
#Reason, instead of writng the "push()" 10 times you can just make a list of all the 
# elemnts you need to add the the array, and add them in together. 
def push(item):
    global topPointer
    for n in range(len(item)): #This for loop Counts the number of elements in the list of items
        if topPointer<stackFull-1: #This condition ensures if the stack still has space for more elements
            topPointer+=1
            stack[topPointer]=item[n] #if it does, the nth item is added to the next topPointer in the array 
        else:
            print("Stack is full, cant push!")  #if it doesnt, a message is displayed 
    print(stack)
item=[3,343,46,12,34,123,2,33,12,32] 
#push(item) #instead occupying 10 lines to push 10 elements, a list of 10 elements is created and pushed into the array(stack)


#Function to Pop(or remove) items from the stack
def pop(): #Removes the last item entered into the stack
    global topPointer
    if topPointer==basePointer-1: #This is to ensure the stack isnt empty
        print("The stack is empty")
    else:
        item=stack[topPointer] #The last item indexed is identified
        topPointer-=1 #the top pointer is decremented
        #Instead of actually removing the item, we decrement the top item. This allows it to be overwritten when a new item is pushed in.
        print(f"The item deleted is {item}") #the deleted item is declared 
#pop()        