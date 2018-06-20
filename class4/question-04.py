#extraction of month from time
import time
t=time.gmtime()
print("the current day is:" , t[6])
x=t[6]
if x==0:
	print('monday')
elif x==1:
	print('tuesday')
elif x==2:
	print('wednesday')
elif x==3:
	print('thursday')
elif x==4:
	print('friday')
elif x==5:
	print('satday')
elif x==6:
	print('sunday')
print(x)


