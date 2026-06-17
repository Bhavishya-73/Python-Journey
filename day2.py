# String
str1 = "this is a string \t hellow world" #gives a tab space
str2 = "this is a string \n hellow world" # starts from next line
print(str1)
print(str2)

print(str1 + str2) # concatintation of string

print(len(str1)) # lenght of string

# indexing in a string 
a = str1[3]
print(a)

# slicing in a string
b = str1[3 : 6]
print(b)

# negative indexing 

c = str1[-3 : -1]
print(c)

# string functions

print(str1.endswith("ld"))
print(str1.capitalize())
print(str1.replace("s" , "g"))
print(str1.find("o"))
print(str1.count("l"))

# Conditional statment  if , elif , else

num1 = 0
num2 = 0
num3 = 3 
num4 = 6

if(num1 == num2 and num2 == num3 and num3 == num4 ):
    print("all numbers are equal")
elif(num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("the greatest no. is ", num1)
elif(num2 >= num3 and num2 >= num4  ):
    print("the greatest no. is ", num2)
elif(num3 >= num4 ):
    print("the greatest no. is ", num3)

else:
    print("the greatest no. is ", num4)


# Nesting in conditional statment ,, 
age = 14
if( age >= 18):
    if( age >80):
        print("you are above age ")
    else:
        print("you can drive")
else:
    print("you are below age")