
#1 

def biggieSize(arr):
    for  i in range (len(arr)):
        if (arr[i] > 0):
            arr[i] = 'big'
        
    
    return arr

#2

def count_positives(num):
    cont=0
    for x in range(len(num)):
        if (num[x]>0):
            cont += 1
            num[len(num)-1]= cont
    print(num)


#3

def sumtotal(list):
  total = 0
  for val in list:
    total = total + val
  return total



#4

def returnlen(leng):
    for val in leng:
        leng1 = len(leng)
    
    return leng1

#5 

def findMin(arr):
    min = arr[0]
    for  i in range (len(arr)):
        if (arr[i] < min):
            min = arr[i]
        
    
    return min

#6


def findMax(arr):
    max = arr[0]
    for  i in range (len(arr)):
        if (arr[i] > max):
            max = arr[i]
        
    
    return max


#7

def findAverage(arr):
    sum = 0
    for  i in range (len(arr)):
        sum += arr[i]
    
    return sum/len(arr)



#8
def UltimateAnalysis(list_dict):
    obj = {"length" : returnlen(list_dict) ,
        "sum" : sumtotal(list_dict) ,
        "max" : findMax(list_dict) ,
        "min" : findMin(list_dict) ,
        "avarage" : findAverage(list_dict) ,
        }

    return obj

#9

def reversnum(numbers):
    L = len(numbers)
    for i in range(int(L/2)):
        n = numbers[i]
        numbers[i] = numbers[L-i-1]
        numbers[L-i-1] = n
    return numbers

