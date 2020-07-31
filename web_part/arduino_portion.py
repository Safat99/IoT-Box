# from arduino_offline import *
from route import dashboard
print(dashboard.buttons)

off()
# relays={'r1':relay1,'r2':relay2, 'r3':relay3, 'r4':relay4 }
relays=relay1,relay2,relay3,relay4

# for i,j in relays.items():
# 	print(i,j)
# 	if  j != '1':
# 		del relays[i]
 
for i in range(relays):
	if i !='1':
		del(switches[i])

on(switches)
sleep(20)
off()




