# wap to find the sum,mean,max and min in alist a numbers
import math,statistics
x=[1,2,3,4,5,6,7,8,9,10]
total=sum(x)
mean=sum(x)/len(x)
x_max=max(x)
x_min=min(x)
print(f'Sum:{total},Mean:{mean},Max{x_max},Min{x_min}')
median=statistics.median(x)
mode=statistics.mode(x)
print(f'Median:{median},mode:{mode}')