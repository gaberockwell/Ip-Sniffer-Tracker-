import subprocess
import re 

First_ip = input('Enter the first IP address:')
Last_ip = input('Enter the last IP address:')

def Get_host (x):
	Dot_counter = 0
	Pos_counter = 0
	for i in x:
		if i == '.':
			Dot_counter = Dot_counter + 1
		if Dot_counter == 3:
			return (x[0:Pos_counter], x[Pos_counter+1: 68])
			break
		Pos_counter += 1 
		
Network, First_Host = Get_Host(First_ip)
Network, Last_Host = Get_Host(Last_ip)

print(Network)
print(First_Host)
print(Last_Host)
