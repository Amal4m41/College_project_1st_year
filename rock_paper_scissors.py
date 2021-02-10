import random as r
import getpass as gp

def check():
  global points,points_bot,value,n
  if((value==1 and n==2) or (value==2 and n==3) or (value==3 and n==1)):
    points+=1
  elif((value==2 and n==1) or (value==3 and n==2) or (value==1 and n==3)):
    points_bot+=1

  value=0
  n=0

def display(*values):
  for i in values:
    if(i==1):
      print('''
					    	     000000000000
					           0000000000000000
					         00000000000000000000
					      00000000000000000000000000
					    000000000000000000000000000000
					    000000000000000000000000000000
					    000000000000000000000000000000
					    000000000000000000000000000000
					      00000000000000000000000000
					         00000000000000000000
					           0000000000000000
					             000000000000
''')
    elif(i==2):
      print('''  
					        00000000000000000000000
				         	00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
					        00000000000000000000000
				                00000000000000000000000
					        00000000000000000000000
				        	00000000000000000000000
				                00000000000000000000000
''')
    else:
      print('''
                                                    01            10
                                                     01          10
                                                      01        10
                                                       01      10
                                                        01    10
                                                         01  10
                                                         000000
                                                        00000000
                                                   0000000    0000000
                                                   00   00    00   00
                                                   00   00    00   00
                                                   00   00    00   00
                                                   0000000    0000000
    
''')

#void main()
while(1):
  mode=total=points=points_bot=0
  value=n=0
  ch=int(input("""
-------------------------------------------Welcome to Rock Paper Scissors-------------------------------------------------------- 
                                                  1-Play Game
                                                  2-Exit

Enter your choice : """))
  if(ch==1):
    while(mode not in (1,2)):
      mode=int(input('''
Choose Mode :
1-Multiplayer
2-Play with Computer

-->'''))
      if(mode not in (1,2)):
        print("                            *Invalid choice! Please try again*")
    while(total==0):
      c=input('''
Choose the level:
A-->7 points
B-->5 points
c-->3 points

-->''')
      if(c.lower()=='a'):
        total=7
      elif(c.lower()=='b'):
        total=5
      elif(c.lower()=='c'):
        total=3
      else:
        print("                       *Entered invalid choice ! Please try again.*")
    while(1):  
      print('''
1-Rock
2-Paper
3-Scissor
''')  
      if(mode==1):
        p2=" Player 2: "
        while(value not in (1,2,3)):
          value=int(gp.getpass("Enter your choice (1,2 or 3) Player 1: "))
          if(value not in (1,2,3)):
            print("                            *Invalid entry! Please try again*")

      elif(mode==2):
        p2=' :'
        value=r.randint(1,3)

      while(n not in (1,2,3)):
        n=int(input("Enter your choice (1,2 or 3)"+p2))
        if(n not in (1,2,3)):
            print("                            *Invalid choice! Please try again*")
      
      display(value,n)
      check()

      if(mode==2):
        print('Bot:',points_bot,'                                                                          ','Player:',points)

        if(points==total):
          print()
          print("Player Wins!")
          break
        elif(points_bot==total):
          print()
          print('Comp Wins!')
          break
      else:
        print('Player-1:',points_bot,'                                                                          ','Player-2:',points)
        if(points==total):
          print()
          print("Player-2 Wins!")
          break
        elif(points_bot==total):
          print()
          print('Player-1 Wins!')
          break
              
  elif(ch==2):
    print("Thank you!")
    break

  else:
    print("Entered invalid choice! Please try again")







