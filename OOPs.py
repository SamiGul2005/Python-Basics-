#OOPs Examples
#OOPs with Arrays
class Card:
    #__Number:INTEGER
    #__Colour:STRING

    def __init__(self,Pnumber,Pcolour):
        self.__Numbers=Pnumber
        self.__Colour=Pcolour 

    def GetNumber(self):
        return self.__Numbers 
    def GetColour(self):
        return self.__Colour 


class Hand():
    #__Cards:ARRAY[0:9] OF Card
    #__FirstCard:INTEGER
    #__NumberCards:INTEGER


    def __init__(self,Card1,Card2,Card3,Card4,Card5):
        self.__Cards=[]
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard=0
        self.__NumberCards=5

    def GetCard(self,index):
        return self.__Cards[index]
    
    
def calculateValue(player):
    score=0
    for i in range(5):
        Card_object=player.GetCard(i)
        num=Card_object.GetNumber()
        colour=Card_object.GetColour()
        if colour=="red":
            score+=5
        if colour=="blue":
            score+=10
        if colour=="yellow":
            score+=15
        score+=num 
    return score    

                

            

#MAIN
card1=Card(1,"red")
card2=Card(2,"red")
card3=Card(3,"red")
card4=Card(4,"red")
card5=Card(5,"red")
card6=Card(1,"blue")
card7=Card(2,"blue")
card8=Card(3,"blue")
card9=Card(4,"blue")
card10=Card(5,"blue")
card11=Card(1,"yellow")
card12=Card(2,"yellow")
card13=Card(3,"yellow")
card14=Card(4,"yellow")
card15=Card(5,"yellow")

Player1=Hand(card1,card2,card3,card4,card11)
Player2=Hand(card12,card12,card14,card15,card6) 

Player1_score=calculateValue(Player1)
Player2_score=calculateValue(Player2) 


if Player1_score>Player2_score:
    print("Player1 wins!")
elif Player2_score>Player1_score:
    print("Player2 wins!") 
else:
    print("Both have equal score so there is a Draw.")       










#OOPs with File Handling
class Character:
    #__Name:STRING
    #__XCoordinate:INTEGER
    #__YCoordinate:INTEGER
    def __init__(self,name,xCoordinate,yCoordinate):
        self.__Name=name
        self.__XCoordinate=xCoordinate
        self.__YCoordinate=yCoordinate
#b)
    def GetName(self):
        return self.__Name    
    def GetXCoordinate(self):
        return self.__XCoordinate 
    def GetYCoordinate(self):
        return self.__YCoordinate
#c)
    def ChangePosition(self,Xchange,Ychange):
        self.__XCoordinate+=Xchange
        self.__YCoordinate+=Ychange 
#d)
chr=[]
F=open("Characters.txt","r") 
for i in range(3):
    Name=F.readline().strip()
    XCoordinate=int(F.readline().strip())
    YCoordinate=int(F.readline().strip())
#    print(XCoordinate,YCoordinate)
    chr_object=Character(Name,XCoordinate,YCoordinate)
    chr.append(chr_object)

#e)
found=False 
while found==False:
    name=input("Enter: ")
    for i in range(len(chr)):
        if chr[i].GetName()==name:
            found=True 
            pos=i
if found:
    print(f"{name} Found at {pos}")                

#f)
valid=False 
while valid==False:
    letter=input("Enter letter: ")
    valid=True
    if letter=="A":
        chr[pos].ChangePosition(-1,0)
    elif letter=="D":
        chr[pos].ChangePosition(1,0)
    elif letter=="W":
        chr[pos].ChangePosition(0,1)
    elif letter=="S":
        chr[pos].ChangePosition(0,-1)
    else:
        valid=False


#g)
name=chr[pos].GetName()
X=chr[pos].GetXCoordinate()
Y=chr[pos].GetYCoordinate()
print(f"{name} has changed coordinates to X={X} and Y={Y}")