elements=['Hydrogen','Hellium','Lithium']
print(elements)
print('Individaul elements:')
print(elements[0])
print(elements[1])
print(elements[2])


# changing a list elements (mutabilty)
elements[1]='Carbon'
print(elements)


elements.insert(1,'Chlorine')


#List of strings
list1=["Nikhlesh","aman",'Rahul','Devansh','Rishabh']


#list of numbers
list2=[1,2,3,4,5,23,100]

#misxed data list
list3=['Ravi',90,102,93,29,44,"B",False,5.786]


#list Nested list
list4=[1,2,3]

print(list1,list2,list3,list4,sep="\n")
m=(list1,list2,list3,list4)
for sublist in m:
    print(sublist)


    #getting a list slice
    i=[10,20,30,40,50,600,700,800,900,100]
    slice=i[3:-2]
    print(slice)



    #append for adding any function in end of the list

fruits=[]
fruits.append("apple")
fruits.append("Banana")
fruits.append("Cherry")
fruits.append("Gauva")
print(fruits)

#insert function
fruits=['applke','banana','cherry']
fruits.insert(1,"orange")
print(fruits)

nobel_metals=['Gold','Silver','Platinum']
elements.append(nobel_metals)
print(elements)
elements.extend(nobel_metals)     #adds multiple elements to end of the list
print(elements)

fruits=['applle','banana','cherry','Gauva']
dry_fruits=["Almond",'Cashew','Walnut']
fruits.append(dry_fruits)
print(fruits)