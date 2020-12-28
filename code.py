import json
import time
#import
temp={}
if(x=='yes'):
	print('Loading master database in temp...)
	with open('master.json','r') as masteropen:
		data_load=json.load(masteropen)
	temp=data_load
	print('Loaded master database')
	print(temp)
#Functions
d=temp
def read(k):
	if k not in d:
		print("Error this key is not present")
	else:
		b=d[k]
		if b[1]!=0:
			if time.time()<b[1]:
				stri=str(k)+":"+str(b[0])
				return stri
			else:
				print("error time to live of k has expired")
		else:
			print("error")
	if(x==4):
		break
	if(x==1):
		key=input()
		value=int(input())
		create(key,value)
	if(x==2):
		key=input()
		delete(key)
		print('key deleted')
	if(x==5):
		print(d)
#saving the data

import json
temp=d
with open('temp.json','w') as fp:
	json.dump(tmep,fp)
print("your database after the operations")
print(temp)
x=input('is this first operation done')
if(x=='yes'):
	with open('master.json','w') as fp:
		json.dump(temp,fp)
	print("thank you")
	exit()
x=input('do you want to save this master dataset yes/no')
if(x=='yes'):
	data={}
	import json
	with open(master.json','r') as fp:
		data=json.load(fp)
	master=dict(data)
	master=update(temp)
	with open('master.json','w') as fp:
		json.dump(master,fp)
print("All given tasks are done thanks")
 

		
		