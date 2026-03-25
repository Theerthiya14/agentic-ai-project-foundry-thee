import random
a=input("PLAYER NAME 1")
b=input("PLAYER NAME 2")
d1=random.randint(1,25)
d2=random.randint(1,25)

s1=25
s2=25
print("__________PLAYER 1____________")
while(True):
    g=int(input("Enter your Guess"))
    s1=s1-1
    if(d1==g):
        print("your Guess Correct")
        break
    elif(d1<g):
        print("your guess is more")
    else:
        print("your guess is less")
print("__________PLAYER 2____________")
while(True):
    g=int(input("Enter your Guess"))
    s2=s2-1
    if(d2==g):
        print("your Guess Correct")
        break
    elif(d2<g):
        print("your guess is more")
    else:
        print("your guess is less")
if(s1==s2):
    print("MATCH DRAW")
elif(s1<s2):
    print("WINNER IS ",b)
else:
    print("WINNER IS ",a)
    
