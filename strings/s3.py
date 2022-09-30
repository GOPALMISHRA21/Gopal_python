#getting a slice
s='digipodium'
slice1=s[4:len(s)]
slice2=s[4:]
print(slice1)
print(slice2)


#slicing
m="journey before destination"
print(m[:7])
print(m[8:14])
print(m[-11:])

amt = '$3000'
print(int(amt[1:]))

rr = '1,143 ratings  | 347 answersd questions'
print("total answers", rr[15:])
print("no of string", rr[:12])
print(len(rr))
for i,v in enumerate(rr):
    print(f'{i}--.{v}')