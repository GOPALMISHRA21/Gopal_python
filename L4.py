# wap to add number in a list by user input
num=[]
for i in range(10):
    data = input("Enter a number")
    if data.isnumeric():
        num.append(int(data))
print("your data =.",num)
