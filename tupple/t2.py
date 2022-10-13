x= 1,2,3,4,5,6,77,65,43
print(x)
print(type(x))
#assignment

a,b = 10,20  # two values are strore in two variable
print(a,b)
a=10,20   # @ values are packed in variable as tupple
print(a,type(a))


#special case
x,*y=1,2,3,4,5,6,7,8   # 1 value stotred in x  and rest in y as a list 
print(x,y)
print(type(x),type(y))