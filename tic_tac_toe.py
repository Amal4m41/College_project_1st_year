lst=[]
p=0
def check():
  a="X"
  for i in range(2):
    if(lst[0][1:]==lst[1][1:2]==lst[2][1:]==a or lst[3][1:]==lst[4][1:2]==lst[5][1:]==a or lst[6][1:]==lst[7][1:2]==lst[8][1:]==a or lst[0][1:]==lst[3][1:]==lst[6][1:]==a or lst[1][1:2]==lst[4][1:2]==lst[7][1:2]==a or lst[2][1:]==lst[5][1:]==lst[8][1:]==a or lst[0][1:]==lst[4][1:2]==lst[8][1:]==a or lst[2][1:]==lst[4][1:2]==lst[6][1:]==a):
      if(a=="X"):
        return 1
      elif(a=="0"):
        return 2
    a="0"
 
def insert():
  print("Player ",p,end=' ')
  c=int(input("enter your grid value :"))
  while(1):
    if((c==1 or c==3 or c==4 or c==6 or c==7 or c==9) and lst[c-1]=="  "):
      if(p==1):
        lst[c-1]=" X"
      else:
        lst[c-1]=" 0"
      break
    elif((c==2 or c==5 or c==8) and lst[c-1]=="| |"):
      if(p==1):
        lst[c-1]="|X|"
      else:
        lst[c-1]="|0|"
      break
    else:
      while(c not in range(1,10) or (lst[c-1]!="| |" and (c==2 or c==5 or c==8)) or (lst[c-1]!="  " and (c==1 or c==3 or c==4 or c==6 or c==7 or c==9))): 
        
        if(c not in range(1,10)):
          print("Entered invalid grid value. Try again Player ",p,end="")
        else:
          print("Grid not free,please enter a different grid value!",end="")
        
        c=int(input(" : "))



    
def display():
  for i in range(len(lst)):
    print(lst[i],end="")
    if(i==2 or i==5):
      print()
      print("-------")    
  print()

def main():
  global lst,p
  while(1):
    print('''
                                             Welcome to Tik-Tac toe
						1-Play the game
						2-Exit 
''')
    choice=int(input("Enter your choice : "))  
    if(choice==1):
      while(1):
        lst=["  ","| |","  ","  ","| |","  ","  ","| |","  "]
        display()
        for x in range(0,9):
          if(x%2==0):
            p=1
          else:
            p=2
          insert()
          display()
          ans=check()
          if(ans==1):
            print("Player 1 Wins!")
            break
          elif(ans==2):
            print("Player 2 Wins!")
            break
        else:
          print("Game Tied!")
        ch=input("Do you want to play again[Y/N] ?")
        if(ch.lower()=="n"):
          break

    elif(choice==2):
      print("Thank you!")
      break

    else:
      print("*Entered wrong choice! Please try again *")


