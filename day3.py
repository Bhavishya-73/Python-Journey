# lists ,, ARE MUTABLE

a = [ 31 , 34, 45.6]
print(a[2])         #print 2nd index element

a.append(4)         # adds element at last
print(a)

a.sort()            # makes list in assending order
print(a)

a.sort(reverse=True  )   # makes list in desending order
print(a)

a.reverse()         # starts list from last 
print(a)

a[2] = 55       # assigning a value to list element
print(a)

print(a[1:3])       # slicing in list

a.insert(2,67)      # inserting an element at given index
print(a)

a.remove(4)     # removes the first occurance of element
print(a)

a.pop(2)        #removes the element at given index
print(a)

b = a.copy()
print(b)


# Tuples ,, THESE ARE IMUTABLE

c = ( )     # empty tuple

d = (1,)  # one element tuple

e = ( 1.43,43, 4,3)

print(e.index(43))  # gives index of element

print(e.count(43))  #no. of occurance of element

# tuples are imutable

e[2] = 23
print(e)
