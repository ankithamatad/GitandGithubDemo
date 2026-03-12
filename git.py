import random
rand=random.randint(1,20)
turns=5
print("welcome to guess my number: ")

while turns>0:
    num=int(input("enter a number: "))
    if num>rand:
        print("too high")
        
    elif num<rand:
        print("too low")
    
    elif num==rand:
        print("you won")
        
    else:
        print("you lose")
        break
    turns-=1
    print("remaining turns ",turns)
if turns==0:
    print("game over")
print("the random number is :",rand)
