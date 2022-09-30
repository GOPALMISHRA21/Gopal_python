evens = 0
odds = 0
while True:
    num = input("enter a number")
    if not num:
        break
    if not num.isnumeric():
        continue
    num = int(num)
    if num % 2 ==0:
        evens += num
        
    else:
        odds += num 
        

print(f"even values added =>{evens}")
print(f"odd values added=>{odds}")