name=input("enter your name")
email=input("enter your email")
mobile=input("enter your number")
city=input("enter city")

#nested if-else
if len(name)>1:
    if'@'in email and len(email)>11:
        if len(mobile)==10 and mobile.isnumeric():
            if city in["lucknow","delhi","noida"]:
             print("your data is saved","thankyou")
        else:print("invalid mobile niumber")
    else:print("invalid email")
else:print("ye kay naam ?")

