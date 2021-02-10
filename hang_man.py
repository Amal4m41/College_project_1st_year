import random
import hang_lib as lib
def random_lib():
  global word,hm,des,word_real
  hm=[]
  word_real,des=random.choice(list(d.items()))
  word=list(word_real.lower())	
  for i in range(len(word)):
    if(word[i]!=" "):
      hm.append("_")
    else:
      hm.append(" ")
  
def insert():
  global chance,wrong_tries   # word is not being assigned therefore takes the global variable only.	    
  l=input("Enter the letter/number : ")
  if(l.isalnum()):
    if(l in word):
      for i in range(len(word)):
        if(l==word[i]):
          if(i==0 or word[i-1]==" "):
            hm[i]=l.upper()
          else:
            hm[i]=l.lower()
    else:
      wrong_tries.append(l)
      chance-=1
    print("Wrong tries = ",wrong_tries," Chances left = ",chance)
  else:
    print("Invalid input!")

def display():
  for i in hm:
    print(i,end=" ")
  print()

def check():
  if(('').join(word).lower()==('').join(hm).lower()):
    return 1
  
#main()
hm=[]
word=[]
des=''
word_real=''

while(1):
  print('''
                                                       Welcome to Hang-man
                                                        1-Play the game
                                                        2-Exit
''')
  ch=int(input("Enter your choice : "))
  if(ch==1):
    while(1):
      flag=0
      wrong_tries=[]

      print("""
Enter the difficulty level : 
1-High
2-Medium
3-Easy
""")
      ch1=int(input("Enter your choice : "))
      if(ch1==1):
        chance=3
        d= lib.d1
      elif(ch1==2):
        chance=5
        d= lib.d2
      else:
        chance=7
        d= lib.d3

      random_lib()      
      display()
      while(1):
        insert()
        display()
        if(flag==0 and ((ch1==1 and chance==2) or (ch1==2 and chance==3) or (ch1==3 and chance==4))):
          print("                                                                                                (Hint will cost 1 CHANCE!)")
          h=input("Do you want hint[Y/N]?")                                                                      
          

          if(h.lower()=='y'):
            print()
            print("Hint : ",des)
            flag=1
            chance-=1
            print()
            print("Chances left =",chance)
            display()

        if(check()):
          print("You Win!")
          break
        elif(chance==0):
          print("Game over! Better luck next time....")
          print("Answer :",('').join(word_real))
          break
      choice=input("Do you want to continue[Y/N] ?")
      if(choice.lower()=='n'):
        break     

  elif(ch==2):
    print("Thank you!")
    break

  else:	
    print("Entered wrong choice! Please try again.") 

