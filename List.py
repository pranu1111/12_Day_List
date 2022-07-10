my_List=["a ","b","c","d"]
# print(type(my_List))

this_List=["banana","mango","straberry","banana","mango"]
# print(this_List)
# print(len(this_List))
# print(len(my_List))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3,"apple",1.33]
list3 = [True, False, False,"true", 1,1.8]
# print(list1)
# print(list2)
# print(list3)

list111=list(("a",1,"b",1.1,.1,555))
# print(type(list111))

# Accecceing list items.............
# print(list111[0])
# print(list111[1])
# print(list111[2])
# print(list111[3])
# print(list2[3])
# print(my_List[1])
# print(list2[2])
# print(list3[0])
# print(this_List[-2])
# print(this_List[-3])
# print(this_List[-1])

l1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(l1[2:5])
# print(l1[0:4])
# print(l1[:6])
# print(l1[2:])
# print(l1[:0])
# print(l1[:])
# print(l1[0:-1])
# print(l1[0:-2])
# print(l1[-5:-2])
# print(l1[-6:-3])

# if "apple" in l1:
#     print("YES! apple is in list")
# else:
#     peint("NO! apple is not in list")

# l1[1]="watermelon"
# print(l1)
# l1[6]="grapes"
# print(l1)
# l1[3]="carrot"
# print(l1)
# l1[2:3]=["banana","sweetpotato"]
# print(l1)
# l1[-6:-2]=["corn","potato","tomato","onion"]
# print(l1)

# l2= ["apple", "banana", "cherry"]
# l2[1:2] = ["blackcurrant", "watermelon"]
# print(l2)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon","ahgdjg","ukhawkh"]
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# print(thislist)
# thislist.append("orange")
# print(thislist)
# thislist.append("apple")
# print(thislist)

aa=["a","b","c","d"]
bb=["e","f","g"]
# aa.extend(bb)
# aa.extend(thislist)
# print(aa)..............['a', 'b', 'c', 'd', 'e', 'f', 'g', 'apple', 'banana', 'cherry']



#remove items...........

# aa.remove("cherry")
# print(aa)

# Remove Specified Index...........
# aa.pop(1)
# print(aa)
# bb.pop(1)
# print(bb)
# aa.pop(0)
# print(aa)

p=[1,111,6,5,44,88,2,11,3]
# del p[2]
# print(p)
# p.clear()
# print(p)
# # del p
# print(len(p))
# del p

# for i in range(len(p)):
#     print(p[i])
    
# i=0
# while i < len(p):
#     print(p[i])
#     i=i+1

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# p.sort()
# print(p)
# p.sort(reverse=True)
# # print(p)
p2=p.copy()
# # print(p2)
p3=p2.copy()
# print(p3)

p4=list(p)
# print(p4)

p5=p4+p
# print(p5)

# for x in p:
#     p5.append(x)
#     print(p)
pp=p.index(111)
print(pp) 
print(p.index(6))
print(p.count(11))


