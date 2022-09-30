# calculator


print("welcome gopal calculator world")
print("what do you want")

print("a=addtion")
print("b=subtraction")
print("c=multiplication")
print("d=division")
print("p=percentage")

c=input()

a=int(input("enter your frist number"))
b=int(input("enter your second number"))

x=a+b
y=a-b
z=a*b
v=a/b
p=(b/a)*100
if c=='a':
    print(f"the add value is{x}")
elif c=='b':
    print(f"the subtraction value is {y}")
elif c=='c':
    print(f"the multiplication value is{z}")
elif c=='d':
    print (f"the division value is {v}")
elif c=='p':
    print(f"the percentabe of two numbers is {p}")
else:
    print("wrong choose")
