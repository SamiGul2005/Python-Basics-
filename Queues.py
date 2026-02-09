#Fist-in-first-out
queue=[0 for i in range(10)]
frontPointer=0 #points to the first item in the queue
rearpointer=-1 #Points to the last item in the 
queueFull=len(queue) #total length of queue
queueLength=0 #Number of indexes occupied

def enQueue(item):
    global rearpointer
    global queueFull
    global queueLength
    if  queueLength<queueFull:
        if rearpointer<len(queue)-1:
            rearpointer+=1
        else:
            rearpointer=0
        queueLength=queueLength+1
        queue[rearpointer]=item
    else:
        print("Queuse is full")  

def deQueue():
    global queueLength,frontPointer,item
    if queueLength==0:
        print("Queue is empty, cant dequeue")
    else:
        item=queue[frontPointer]                
        if frontPointer==len(queue)-1:
            frontPointer=0
        else:
            frontPointer+=1
    queueLength-=1               