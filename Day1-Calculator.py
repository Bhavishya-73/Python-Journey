num1 = float(input("Enter Your Number 1 : "))
num2 = float(input("Enter Your Number 2 : "))
what = input("what operation you want : ")
if(what == "+" or what=="add" ):
    print("Answer = " , num1+num2)
elif(what == "-" or what == "sub" ):
    print("Answer = " ,num1-num2)
elif(what== "*" or what=="mul" ):
    print("Answer = " ,num1*num2)
elif(what== "/" or what=="div"  ):
    if(num2 == 0):
        print("not defined")
    else:
        print(num1/num2)
elif(what== "%" or what== "rem" ):
    print("Answer = " ,num1%num2)
elif(what == "**" or what == "power to "):
    print("Answer = " ,num1**num2)
else:
    print("ERROR")