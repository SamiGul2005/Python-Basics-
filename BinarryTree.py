#The class to store the pointers and the Value in the array
class Treenode:
    def __init__(self,rightPointer,val,leftPointer):
        self.Data=val
        self.RightPointer=rightPointer
        self.LeftPointer=leftPointer
    

    #Function to print Pointers and Value
    def printArray(self):
        return self.LeftPointer,self.Data,self.RightPointer

    
 


#FUNCTIONS

#Initialise Function to Initialise the array    
def InitialiseTree():
    global RootPointer,FreePtr,NullPointer, Tree
    RootPointer=-1 #Points to the first node of the tree
    FreePtr=0 #Points to the next available node
    NullPointer=-1
    for i in range(7):
        Tree[i].LeftPointer=i+1
    Tree[6].LeftPointer=-1    


#Print Function to print Array
def PrintArray(arr):
    for i in range(len(arr)):
        print(f"[{i}]: {arr[i].printArray()}")


def InsertNode(newNode):
    global FreePtr,RootPointer,Tree

    if FreePtr!=NullPointer: #Meaning it isnt the end of the tree

        #step1
        NewNodePtr=FreePtr #A new node Pointer which points to the next available node
        FreePtr=Tree[FreePtr].LeftPointer #A new free pointer relative to the new node pointer

        Tree[NewNodePtr].Data=newNode #The Data entered in the New Node
        Tree[NewNodePtr].LeftPointer=NullPointer
        Tree[NewNodePtr].RightPointer=NullPointer

        #step2
        if RootPointer==NullPointer: #If its the first node
            RootPointer=NewNodePtr
        else:
            thisNodePtr=RootPointer #We start with the RootPointer(The first pointer)

            #step3
            while thisNodePtr!=NullPointer:  #This condition takes us to the end of the tree
                previousNodePtr=thisNodePtr #We store the last node ptr in this variable

                if Tree[thisNodePtr].Data>newNode: #This allows us to ensure we are going in the right direction of the tree
                    turnLeft=True    #if  true, the new node will be added to the left position of the previous pointer (since, the newNode is less than thisNode, it will be towards the left)
                    thisNodePtr=Tree[thisNodePtr].LeftPointer #this variable will keep moving left till null is reached, and then the boolean variable  will help identify its direction from the prevPtr perspective
                else:
                    turnLeft=False
                    thisNodePtr=Tree[thisNodePtr].RightPointer    

            #step4
            if turnLeft==True: #If the final turn was left 
                Tree[previousNodePtr].LeftPointer=NewNodePtr #The left pointer of the new node points to freeNode
            else:
                Tree[previousNodePtr].RightPointer=NewNodePtr #The right pointer of the new node points to freeNode


def Search(num):
    global  RootPointer,FreePtr,NullPointer,Tree
    ThisNodePtr=RootPointer #We start with the first node
    while ThisNodePtr!=NullPointer and Tree[ThisNodePtr].Data!=num: #While it isnt  the end of tree and data hasnt been found, keep looping
        if Tree[ThisNodePtr].Data>num: #If data of current node greater than num
            ThisNodePtr=Tree[ThisNodePtr].LeftPointer #Current Node Pointer becomes the left pointer of the previous node
        else: #if greater
            ThisNodePtr=Tree[ThisNodePtr].RightPointer   #the current node pointer becomes the right pointer of the prev node
    #This will keep repeating until ThisNodePtr is pointing to the node with num, or the tree has ended
            
    return ThisNodePtr  #If the num ptr has been found, its returned. Else the last null value is take as ThisNodePtr and it is returned.




#Tree Traversal Techniques

#1)
#Inorder: A tree traversal which follows the Left-Root-Right pattern (LRR). 
#Meaning the left subtree is traversed first, then the root node of that subtree, 
#and finally the right subtree is traversed

#Logic: LEFT -> ROOT -> RIGHT

#            10
#          /   \
#        5      12
#      /  \
#    3     6

#Output: 3,5,6,10,12


def InOrder(root):
    global NullPointer
    if root!= NullPointer:
    
        #First recur on the left subtree
        InOrder(Tree[root].LeftPointer)

        #Now deal with the node
        print(Tree[root].Data,end=" ")

        #Then recur on the right subtree
        InOrder(Tree[root].RightPointer)


#Inorder without Recursion
def inOrder(root):
    global Tree
    current=root #We start with the first node
    stack=[] #Creake a stack to store pointers in INORDER format(accending)
    while True: 
        # Reach the left most Node of the current Node
        if current!=-1: 
            # Place pointer to a tree node on the stack 
            # before traversing the node's left subtree
            stack.append(current)
            current=Tree[current].LeftPointer
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is 
        # empty you are done
        elif(stack):
            current=stack.pop()
            print(Tree[current].Data, end=" ")

            # We have visited the node and its left 
            # subtree. Now, it's right subtree's turn
            current=Tree[current].RightPointer
        else:
            break 
    print()    

#2)
#Preorder: A tree traversal which follows the Root-Left-Right pattern(RLR). 
#Meaning the Root node of the tree(or subtree) is traversed first, then the right node of that subtree,
#and finally the left node of the subtree.

#Logic: ROOT -> LEFT -> RIGHT 

#            10
#          /   \
#        5      12
#      /  \       \
#    3     6       14
    
#Output: 10,5,3,6,12,14     

def PreOrder(root):

    if root!=-1:

        #First Print the data of node 
        print(Tree[root].Data,end=" ")

        #Then on the left child
        PreOrder(Tree[root].LeftPointer)

        #Finally recur on right child
        PreOrder(Tree[root].RightPointer)

#PreOrder Without recursion

def preOrder(root):
    if root==-1:
        return

    # create an empty stack and push root to it
    nodeStack=[]
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while len((nodeStack)>0):

        # Pop the top item from stack and print it
        node=nodeStack.pop()
        print(Tree[node].Data, end=" ")

        # Push right and left children of the popped node
        # to stack
        if Tree[node].RightPointer!=-1:
            nodeStack.append(Tree[node].RightPointer)
        if Tree[node].LeftPointer!=-1:
            nodeStack.append(Tree[node].LeftPointer)            

#3)
#PostOrder: A tree traversal which follows the Left-Right-Root pattern(LRR). 
#Meaning the left node of the tree(or subtree) is traversed first, then the right node of that subtree,
#and finally the Root node of the subtree(or tree).            

#Logic: LEFT -> RIGHT -> ROOT

#            10
#          /   \
#        5      12
#      /  \       \
#    3     6       14

#OutPut: 3,6,5,14,12,10

def PostOrder(root):
        
    if root!=-1:
        # First recur on left child
        PostOrder(Tree[root].LeftPointer)
    
        # The recur on right child
        PostOrder(Tree[root].RightPointer)
    
        # Now print the data of node
        print(Tree[root].Data, end=" ")

#PostOrder without recursion

def postOrder(root):
    Stack1=[]
    stack2=[]

    Stack1.append(root)

    while Stack1: #(Not empty)
        node=Stack1.pop()
        stack2.append(node)

        if Tree[node].LeftPointer!=-1:
            Stack1.append(Tree[node].LeftPointer)
        if Tree[node].RightPointer!=-1:
            Stack1.append(Tree[node].RightPointer)        

    while stack2: #(Not Empty)
        node=stack2.pop()
        print(Tree[node].Data, end=" ")