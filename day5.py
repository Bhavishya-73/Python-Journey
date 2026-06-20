# Loops

# while loops
 
a = 1 
while a<= 10:       # loops until the condition becomes false
    print(a ,"hellow")
    a +=1

# Break in while loop,, used to terminate loop when encountred

b = 1 
while b<= 10:
    if(b == 5):         #loop breaks when b = 5
        break
    print("hellow")
    b +=1

# continue in while loop

c = 1
while c <=10 :
    if(c==5):
        c += 1
        continue        #when c = 5 , loop continues again and skips no. 5 to print
    print(c)
    c +=1

# for loop ,,used for sequentional printing of values of lists, string , tuples etc

q = (1,2,3,55,6,7,4,)
for index in q:
    print(index)
else:           # this works when for loop completes
    print("completed")

# finding a no. in tuple
a = [1,4,9,16,25,36,49,64,81,100]
x = int(input("no."))
idx = 0
for num in a:
    if(num == x):
        print("found at indx ", idx)
    idx +=1


# Range , starting from zero by default with step size 1 by default
#range(starting, ending, stepsize)

for i in range(0 , 100 ,10):
    print(i)

#pass statement ,, used when we want no work to be done in it

for i in range(50):
    pass
print("done")
