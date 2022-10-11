colors=['red','green','blue','black','purple',
        'brown','white','gray','pink']

colors_with_a=[]
colors_with_n=[]

for color in colors:
    if 'a' in color:
        colors_with_a.append(color)
    if color.endswith('n'):
        colors_with_n.append(color)
print(colors_with_a)
print(colors_with_n)