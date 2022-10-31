a={'Ram','Shyam','Hari','Gita','Sita'}
b={'Alex','Mark','Eliza','Benny','Sunny'}
c={'Ram','Alex','Gita','Tanya','Sergi'}

# union 
ab=a|b
print("union=>",ab)
# or
ab=a.union(b)
print("union", ab)
#intersection

ac=a & c  #a.intersection(C) also works
print('intersection=>',ac)

abi=a&b
print('intersection',abi)   # no common icon in those set

#diffrence
ac=a-c,
print('difrence=>',ac)

#symetric diffrence
ac=a^c 
ac=a.symmetric_difference(c)   #a.symetric_ diffrence(c)also works
print('symetric diffrence->',ac)

