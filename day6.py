# Functions 

def sum(a , b):              # parameters
    sum1 = a +b
    print(sum1)
    return sum1

sum(1 , 2)   # function call (arguments1 , argument 2)

x = sum(2,4) # using return we can store value in variable to use later
print(x)

# function with default parameter

def sum(a=1,b=2):
    print(a+b)
sum()           # if no argument is given ,a=1 and b=2 are default values(if we give default value to onlly one , start from giving right for eg (a,b=2))

#function without parameters

def name():
    print("Bhavishya")

                   
name()     

x = name()         
print(x)             #have no output




# built-in function

print("hellow" , end =" ")          #by default end func is \n but its a space now
print("world")


