import random
def randInt(min , max ):
    newList = []
    for x in range(min+1,max):
        newList.append(x)
    for min in range (len(newList)):
        return(random.choice(newList))

print(randInt(0 , 100))  
print(randInt(0,50)) 	    
print(randInt(50 ,100)) 	  
print(randInt(min=50, max=500))    