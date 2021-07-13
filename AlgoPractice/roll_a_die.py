import random
import math
def roll_die(counter):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    while counter>0 and counter<2000:
        if  die1==die2:
            counter=-1
            print("doubled") 
            print(counter)
            break
        else:
            print(counter)
            counter=counter+1
            #roll_die(2)
roll_die(1)