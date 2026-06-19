# Dictionary
my_dict = {
    "name" : "bhavishya",
    "age" : 19,
    "hobby" : "programing",
    "sports":{                                      # nesting in a dictionary
        "online" : ("free fire" , "minecraft"),
        "offline" : "cricket",
    }
}
print(my_dict)
print(type(my_dict))
print(my_dict["name"])
my_dict["name"] = "Tushar"     #assigns value of a key 
print(my_dict)
print(my_dict["sports"]["online"]) # printing value through nesting

#dictionary methods

print(my_dict.keys())   #print all keys name
print(my_dict.values())   #print all values
print(my_dict.items())     #give all key: valur pairs
print(my_dict.get("name"))  #give value of key

#adding items to dictionary

my_dict.update({"studyy" : "lpu"})
print(my_dict)



# Sets (imutable)

num = {2,3,1,2,}
print(num)      #only unique values come in a set
a = set()       #for making empty set
print(a)  

# set methods

num.add(34)  # adds an eliment to set
print(num)

num.remove(34)
print(num)

num.pop() # removes a random element from list
print(num)

num2 = {4,5,2,1,3,}

print(num.union(num2))  # combines two set with union
 
print(num.intersection(num2))     #combines two set with intrsection
