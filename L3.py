x = [3,2,2,2,2,2,2,2,4,5,6,6,6,6,6,6,7,8,9,0,1,2,3,2,4,5,6,7]

print(x.index(3))
print(x.index(6))
print(x.index(1))
z=x    # not a good idea
y=x.copy()
z.append(10)
y.append(20)

print(x is z)
print(x is y)
print(x)
print(y)
print(z)