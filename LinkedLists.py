class node:
    def __init__(self,data,pointer):
        self.data=data #the content of the array
        self.pointer=pointer #the pointer to the next node

linkedlist=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
NullPointer=-1 #CONSTANT
FreeListPointer=5 # next available node
startPointer=0

#What does the initialise() do?
#It initialises all the nodes of the list, so they point to the next node until the last one which points to Null(-1)


def initialise():
    global NullPointer
    global startPointer
    global FreeListPointer

    startPointer=NullPointer 
    FreeListPointer=0 #Points to the next available node
    for i in range(5):
        linkedlist[i].pointer=i+1
    linkedlist[5].pointer=NullPointer

def InsertNode(NewItem):
    global FreeListPointer, startPointer, linkedlist
    #Pointers introduced: NewNodeptr, ThisNodePointer, PreviousNodePointer
    
    if FreeListPointer!=NullPointer:  #Meaning there is space in the array
  
        #New Data item is inserted in the free list position
        NewNodeptr=FreeListPointer #NewNode pointer is a new local pointer which will point on the new node data 
        linkedlist[NewNodeptr].data=NewItem #The data is inserted in the new node pointer position
        FreeListPointer=linkedlist[FreeListPointer].pointer #The freelist moves on to the next available node
        
        #Finding the insertion point 
        ThisNodePointer=startPointer #ThisNodePointer goes forward
        PreviousNodePointer=NullPointer #PrevioussNodePointer goes behind
        #This Loop will keep repeating till the insertion point is found
        while (ThisNodePointer!=NullPointer): #and (linkedlist[ThisNodePointer].data<NewItem): #(incase if sorted list)
            PreviousNodePointer=ThisNodePointer #Prev pointer takes position of this node Pointer
            ThisNodePointer=linkedlist[ThisNodePointer].pointer #and ThisNodePointer points to the next one

        #Incase of un-ordered list, the element has to be added at the end of the linked list. So the while loop will keep repeating 
        #until this node pointer reaches -1, and previous node pointer will be pointing to the last node in the linked list
            
        #In case of ordered list, the element has to be added in between the linked list so the while loop will keep repeating until 
        #this pointer is pointing to the node which is greater than the NewItem, and previous pointer is going to point to the item which 
        #is less than the NewItem.

        #These statements are for adjusting the pointers
        if ThisNodePointer==startPointer:
            linkedlist[NewNodeptr].pointer=startPointer 
            startPointer=NewNodeptr
            #Checking if the item to be added is at the first position
        else:
            linkedlist[NewNodeptr].pointer=linkedlist[PreviousNodePointer].pointer
            linkedlist[PreviousNodePointer].pointer=NewNodeptr    
            #Putting the Node in the middle of the array
            #The NewNode Becomes the last node(-1)
            #The previous last node becomes 2nd last node, by changin pointer to the index of last node


def  DeleteNode(num):
    global startPointer,linkedlist,FreeListPointer
    thisPointer=startPointer #Current Pointer
    previousNodePointer=NullPointer

    #Linear search for the node
    while linkedlist[thisPointer].data!=num and thisPointer!=NullPointer: #Till the pointer with data has not been found inn the list, the pointers keep changing
        previousNodePointer=thisPointer
        thisPointer=linkedlist[thisPointer].pointer
 
    if thisPointer==NullPointer: #Checking if item exists in the list
        print("Not found")
    
    else: #if it does,
        if thisPointer==startPointer: #checking if the node to be deleted is the first node
            startPointer=linkedlist[thisPointer].pointer #Start pointer changed
        else:    
            #Adjust Pointers
            linkedlist[previousNodePointer].pointer=linkedlist[thisPointer].pointer

        #Adjusting Pointers to add node to the FreeList (Making the deleted node available)    
        linkedlist[thisPointer].pointer=FreeListPointer
        FreeListPointer=thisPointer
        

def SearchNode(num):
    global startPointer,FreeListPointer,linkedlist
    currentPointer=startPointer #Same as thisNodePointer 
    found=False
    while  currentPointer!=NullPointer and not found: #While it isnt the end of the list or the item hasnt been found, the loop keeps repeating  
        if linkedlist[currentPointer].data==num: #
            print(f"Found at {currentPointer}") #Note: This refers to the index of the Item in the list 
            found=True
        else:
            currentPointer=linkedlist[currentPointer].pointer  #If not found the CurrentPointer is Adjusted
    return found

def outputNodes(startPointer,linkedlist):
    CurrentPointer=startPointer #CurrentPOinter set to the start of the list
    if CurrentPointer!=NullPointer: #Check for the end of list. This is the Base Case for the recursive Function
        print(str(linkedlist[CurrentPointer].data), end=" ") #Print the data in the currentPointer
        CurrentPointer=linkedlist[CurrentPointer].pointer #CurrentPointer adjusted 
        outputNodes(CurrentPointer, linkedlist) #The New currentPointer sent back to function recursively 
