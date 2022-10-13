my_tuple=(1,2,3,4,5,6,7,8,9,10)
print(my_tuple)
print(type(my_tuple))
print(f'Seize=>{len(my_tuple)}')

#indexing
print(f'Index 0=>{my_tuple[:3]}')
print(f'Index 1=>{my_tuple[:3]}')
print(f'Last Index =>{my_tuple[:3]}')

#slicing
print(f'Frist 3 =>{my_tuple[:3]}')
print(f'Last 3 =>{my_tuple[-3:]}')

# tupple are imutable values does not change  (gives eroor when try to chnage)
my_tuple[0]=100     #(error)