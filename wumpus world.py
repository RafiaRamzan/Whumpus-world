w=[[1,'B',"PIT",'B'],['S',0,'B',0],["WUMPUS","BSG","PIT",'B'],['S',0,'B',"PIT"]]

row=0
#arrow=True
colum=0
arrow=1
player=True
while(player):
    print("press 1 to move right")
    print("press 2 to move up")
    print("press 3 to move down")
    print("press 4 to move left")
    print("press 5 to exit game")
    #print("press 6 to throw arrow")
    a=int(input("where you want to go"))
    #print(a)
    if(a==1):
        colum=colum+1
        #print("now you can move  right,down")
    elif(a==2):
        row=row-1
        #print("now you can move  right,up, down")
    elif(a==3):
        row=row+1
        #print("now you can move left, right,up, down")
    elif(a==4):
        colum=colum-1
        #print("now you can move left, right,down")
    elif(a==5):
        print("\nExit")
        break;
    #elif(a==6):
        #if(arrow==0):
            #print("\narrows not present")
        #else:
            #print("\narrow thrown")
            #arrow=arrow-1 
    
    if(colum>=3 or colum<0):
            print("\nmove denied\n")
            colum=colum+1

            continue;
    if(row>=3 or row<0):
            print("\nmove denied\n")
            row=row+1
            continue;
            
    if(w[row][colum]=='B'):
        print("BREEZE")
  
    if(w[row][colum]=='BSG'):
        print("\nGold found...goal accumplished")
        break;
    if(w[row][colum]=='S'):
        print("\nSmell\ndo you want to kill the wumpus\nif yes")
        b=input("where you want to throw arrow (down or right)? \n if no then press no")
        
        if(b=="down"):
            print("wumpus  killed...... 5000 points")
            arrow=arrow-1
            row=row-1
            check=1
            
        if(b=="right"):
            print("arrow wasted")
            arrow=arrow-1
            
        if(b=="no"):
             print("arrow not used")
        if(arrow==0):
            print("no more arrow not present")
    if(w[row][colum]=='WUMPUS'):
          if(check==1):
              print("whumpus already killed")
          else:
              print("whumpus")
              break;
          if(b=="no"):
              print("\nyou find whumpus....game end")
              break;
          
            
    if(w[row][colum]=='PIT'):
        print("\nYou fell in pit")
        break;
    if(w[row][colum]==0):
        print("\nYou are safe")
        

    


    
    
