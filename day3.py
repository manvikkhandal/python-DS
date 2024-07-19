#BOOLEAN 
# var1 = True
# var2 = False
# print(var1,var2)
# print(type(var1),type(var2))

#LIST
#array

# ls = [25,41,36,75,25.2,21.,30,1,'upflqirs',True]
# print(ls)
# print(type(ls))

# ls = [10,12,13,14,14,16]
# #print(ls[1])
# print(ls[1:4])

#ls = [5,10,13,14,'upflair',100]
# x=ls[4]
# print(x[4:7])

#mutable = changeble(list)
#imutable = unchangeble(list)
#insert,remove,manipulate

#student_name = ['taniya','yash','prerna','yash','ruchika','aditya','kalika']
#student_name[0]="tanya"
#print(student_name) 
#maipulation or updation

#student_name.append('jugnu') #insert
#student_name.append('ritu') #at the last position

#student_name.pop() #remove the item from last position
 
#student_name.insert(1,'gurpreet')
#student_name.remove('prerna')
#del student_name[2]
#print(student_name)

#print(student_name.count('yash'))

# ls1 = ['A','B','C','D','E']
# ls2 = [85,4,5,6,9,87,63]
# print(ls1.reverse()) #ls1[::-1]
# ls2.sort() #ascending order
#ls2.sort(reverse=True)
#ls1.sort()
#print(min(ls2))
#print(ls1)
# print(max(ls2))
# print(sum(ls2))

# ls1 = ['A','B','C','D','E']
# ls2 = ['F','G','H']
# full_list = ls1+ls2
# #print(ls1+ls2)
# #print(full_list)
# #ls1.append(ls2)
# # ls1.extend(ls2)
# # print(ls1)
# ls1.clear()
# print(ls1.index('c'))

# ls2 = [10,20,3.1,'upflairs pvt ltd',500,400]
# # ls2[2]=100
# # print(ls2)
# # x=ls2[3]
# # print(x[0:8])
# ls2[ls2.index('upflairs pvt ltd')]="flipkart pvt ltd"
# print(ls2)

#TUPLE
#imutable = unchangeable are tuple
# tpl = (25,41,63,96,'upflairs',True,25.2)
# #print(tpl[4])
# #print(type(tpl))
# tpl.count()
# tpl.index()
# ls = []

#SET
#st = {52,1,63,56,54,786,44,56,3,86,56}
#print(st)
#print(type(st))
#st.add(500) #insertion
#st.remove(54) #remove item must be present 
#st.discard(54) #if item isn't present still there will be no error
#print(st)
# st1 = {52,41,63,96,78,54}
# st2 = {52,41,65,55,22}
# #st1.update(st2)
# #print(st1)
# print(st1.intersection(st2)) #common elements
# #print(st1+st2) error

#DICTIONARY 
#pairs = (key:value)
# marks = {'mohit':52,'rohit':56,'rocky':53,'mohit':54}
# print(marks)
# print(type(marks))

st="hello welcome to upflairs."
# print(st[17:25])
# print(len(st))
print(st.replace("upflairs","flipkart"))
