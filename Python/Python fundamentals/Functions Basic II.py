#1

def countdown(num):
    newlist= []
    for x in range ( num , 0 , -1):
        newlist.append(x)
      

    return print(newlist)


#2
def print_and_return(list):    
    for x in list:
        print (x)
        return (x + 1)


#3

def first_plus_length(num):
    sum = 0;
    sum = num[0] + len(num)
    return sum

#5

def length_and_value(size , value):
    newlist=[]
    for x in range (0 , size ,1):
        newlist.append(value)
    return newlist
