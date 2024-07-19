#variable
var = 20
print(var)
print(type(var))

#1. A-Z, a-z, 0-9, _ only these characters
#2. variable name cannot start with a number
#3. case sensitive 

manvik = 10
print(manvik)

#reserved keywords cannot be used as a variable name
# print = 10
# print(print)

# var1 = 10
# var2 = 10
# sum(var1+var2)
# sum = 20

_ = 25
print(_)

st = "upflair pvt itd 2345"
print(st) # upflair pvt itd 2345
print(type(st)) # to check the datatype of the st

# Slicing of the String in python
st = 'upflairs'
print(st[4])
print(st[4:6+1])
# [starting : stoping : jump]
print(st[4:6+1:1])
print(st[-4])
print(st[4])
print(st[2:])
print(st[:4])
print(st[::1]) #upflairs
print(st[::2]) #ufar
print(st[::3]) #ulr
print(st[-4:-1]) #air
print(st[::-1])

st = "upflairs pvt ltd jaipur rajasthan"
st2 = "UPFLAIRS PVT LTD JAIPUR"
# jaipur
print(st[-16:-10])
print(st[17:23])
print(len(st)) #total no of characters = 33
print(st[20-len(st):27-len(st)])

print(st.count("j"))
print(st.count("jaipur"))
print(st.count("ja"))
print(st)
print(st.upper())
print(st.lower())

print(st2.title())
print(st2.capitalize())

print(st.replace("upflairs", "flipkart"))
print(st.replace("upflairs",""))

st= "upflairs"
# print(st.find("p"))

# print(st.endwith())
# print(st.startswith())
# print(st.split())
# print(st.strip())
# print(st.center())
