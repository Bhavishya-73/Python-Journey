# week 1 Practise

# variable, input, data type, print statment

a = int(input("your age :"))
print("your age is", a)
print(type(a))

string, indexing, slicing , conditional nesting

b = "my name is bhavishya"
c = "i am 19 years old"

print(len(b))
print(b+c)
print(b[3])
print(b[3:6])
print(b.endswith("a"))
print(b.capitalize())
print(b.replace("m" , "k"))

# conditionals

num1 = int(input("number 1 :"))
num2 = int(input("number 2 :"))
num3 = int(input("number3 :"))
num4 = int(input("number 4 :"))
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


