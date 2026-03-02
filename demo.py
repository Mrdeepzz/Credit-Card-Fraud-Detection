
# print("first python code")

# # declaring variables

# a=10
# b=20
# name='RAJA'

# print(a)
# print(b)
# print(name)

# # checking the data type of variable
# print(type(a))
# print(type(name))

# fname='gani'
# lname="bunny"
# print(fname+" " +lname)

# #user input values

# fname='priyanka'

#Faranet to celsisus
#a = int(input("Enter the first no"))
#F = (c*9/5)+32

# #int ,float,dict,tuple,list,set,boolean,string

#list
#mylist = [1,2,3,4,5]
#print(mylist)
#print(mylist[1])
#print(mylist[-1])

#modifying list
#mylist[1] = 8
#print(mylist)

#data = ["teju",24,True]
#print(data)

#nes_list = [["teju","naveen","tejas"],[23,34,26],["BCA","BE","BSC"]]
#print(len(nes_list))
#print(nes_list[0])
#a = "Name:"+nes_list[0][1] + " Age:"+str(nes_list[1][1]) + " Qual:" + nes_list[2][1]
#print(a)

#tuple
#tup = (1,2,3,4)
#print(tup)

#tup[-1] = 8
#print(tup)

#list = list(tup)
#list[-1] = 8

#tup = tuple(list)
#print(tup)

#dict
#mydict = {1:"hello",2:"world"}
#print(mydict)

#print(mydict[1]+mydict[2])

#mydict[2] = "bestie"
#print(mydict[1] + mydict[2])

#sets
# myset = {1,2,3,4,1,2,3,4}
# print(myset)

# nums = [20,21,23,10,21,20,23]
# print(set(nums))
# print(list(set(nums)))

#conditional statements
# a = 10
# if(a<=20):
#     print("hii")

# num = int(input("Enter the number"))
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")    

#check greates of three no
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
# if((a>b) and (a>c)):
#     print("a is greatest")
# elif((b>c)):
#     print("b is greatest")
# else:
#     print("c is greatest")        

# username = input("Enter the username: ")
# password = input("Enter your password: ")
# if(username == "" and password == ""):
#     print("Enter username or password!")
# elif(username == "admin" and password == "admin"):
#     print("Login success!")    
# else:
#     print("Login Fail!")   

#looping statement
# n=2
# while(n<=50):
#     if(n%2==0):
#         print(n)
#         n=n+1
#     else:
#         n=n+1    

#for loop
# n = int(input("Enter the range: "))
# for i in range(2, n, 2):
#     print(i)

# result = ""
# fruits = ["mango","banana","grapes","orange"]
# search_inp=input("Enter the search fruit: ")
# for i in fruits:
#     # print(i)
#     if search_inp == i:
#         result = "Fruit is Present"
#         break
#     else:
#         result = "Fruit is not Present"    
# print(result) 
       
# remaining_attempts=3
# attempts = 0
# while attempts<3:
#    username = input("Enter the username: ")
#    password = input("Enter your password: ")
#    if(username == ""):
#      print("Enter username!")
#    elif(password == ""):
#      print("Enter password!")
#    elif(username == "admin" and password == "admin"):
#      print("Login Success!")  
#      break    
#    else:
#      attempts = attempts+1
#      print("Remaining attempts: ",remaining_attempts-attempts)
#      if(attempts == 3):
#        print("All attempts over! Usernmae is blocked")
#      print("Login Failed!")

# def print_name():
#     print("Function Executed")

# print_name()

# def return_ex():
#     return "Hello i am returned"

# print(return_ex())

# def addition(a,b):
#     return a+b

# def subtracrtion(a,b):
#     return a-b

# def multiplication(a,b):
#     return a*b

# def division(a,b):
#     return a/b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(addition(num1,num2))
# print(subtracrtion(num1,num2))
# print(multiplication(num1,num2))
# print(division(num1,num2))

# #register
# print("-----Register Username and Password------")
# def register(username,password):
#   regdata = {"user":username,"passd":password}
#   return regdata

# username = input("Enter the username: ")
# password = input("Enter the password: ")
# reg = register(username,password)

# #login
# print("-------Login Username amd Password------")
# remaining_attempts=3
# attempts = 0
# while attempts<3:
#    username = input("Enter the username: ")
#    password = input("Enter your password: ")
#    if(username == ""):
#      print("Enter username!")
#    elif(password == ""):
#      print("Enter password!")
#    elif(username == reg['user'] and password == reg['passd']):
#      print("Login Success!")  
#      break    
#    else:
#      attempts = attempts+1
#      print("Remaining attempts: ",remaining_attempts-attempts)
#      if(attempts == 3):
#        print("All attempts over! Usernmae is blocked")
#      print("Login Failed!")