#1
for x in range(0, 151, 1):
    print(x)

#2
for x in range(5 , 10 , 1):
    print (x*5)

#3
for x in range( 0, 100 , 1):
  if x == 5 :
    print("Coding")
  elif x==10:
    print ("Coding Dojo")


#4
sum =0 
for x in range(0,500000, 1):
    if (x%2!=0):
        print(x)
        sum= int(sum)+int(x) 
        print(sum)



#5
for x in range(2018,-1,-4):
    if x%2==0:
        print(x)


#6

lowNum=2
highNum=9
mult=3
for x in range(lowNum, highNum +1 ,1):
    if(x%3==0):
        print(x)
