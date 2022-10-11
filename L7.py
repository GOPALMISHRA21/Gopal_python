names=['Raymond','Cynthia','David','Jenifer','Clatyon','Mike']
frist_letters=[]
last_letters=[]
for name in names:
    frist_letters.append(name[0])
    last_letters.append(name[-1])
print(name)
print(frist_letters)
print(last_letters)


name=['Project Manager','Central Processing Unit','Graphics Processing Unit',
       'Random Acess Memory','Input Output']
for name in names:
    p1,p2=name.split('.')
    frist_letters.append(name[0])
    last_letters.append(name[-1])
short_names=[frist]