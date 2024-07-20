# _____ LOOPS ______
#date10

# 1. for
# 2. while
# 3. do-while

# _ FOR _
# for i  in range(10): # 10
#     print(i+1,"Hello")

# for i  in range(0,10,2): # 10
#     print(i+1,"Hello")


# _ WHILE _
# i=1 
# while i<=10 :
#     print("hello world",i)
#     i+=1


# for i in range(100):
#     print("hello")


# condition = True
# while condition:
#     user_input = input("Do you wnat to quit this program press Y/N : ")
#     if(user_input=='Y' or user_input=='y'):
#         condition=False
#     print("Welcome")


# __break_&_continue___


# for i in range(10):
#     print(i)
#     if i == 5:
#         break # Break keyword stops the current execution of the loop


# for i in range(10):
#     if i == 5:
#         continue # Continue keyword is used to ignore the current execution
#     print(i)

# ls = [1,2,3,4,85,76,78,89,9]
# if 85 in ls:
#     print("present")
#     print(ls.index(85))
# else:
#     print("Not Present")


# count = 0
# for i in ls:
#     if i==85:
#         print(count)
#         break
#     count+=1

# ls min(),max() without min()&max()

# *
# * *
# * * *
# * * * *
# * * * * *

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# size = int(input('enter size of pattern\n'))
# for i in range(size):
#     for j in range(i+1):
#         print('*',end='')
#     print('')

# count = 0
# temp = 1
# for item in ls :
#     if item == 85 :
#         if temp == 2 :
#             print('85 is present at index:', count)
#             break
#         temp += 1
#     count += 1

# print('Total iterations taken:', count+1)