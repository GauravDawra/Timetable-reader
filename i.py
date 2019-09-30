import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Enter Email").grid(row=0)


e2 = tk.Entry(master)

e2.grid(row=1, column=0)


master.mainloop()


import datetime
import pickle


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

list_black_bars=[]

from PIL import Image
import numpy as np

im = Image.open('tt.png')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((5,5 ))


'''
for i in range(43,436):
	rgb_im = im.convert('RGB')
	r, g, b = rgb_im.getpixel((750,i ))

	
	print(i, r,g,b)

'''


list_bb_horizontal = [26, 42, 131, 211, 284, 347, 417]

list_bb_vetical = [55, 97, 181, 200, 381, 476, 535, 636, 719, 781, 831, 921, 1000, 1080, 1135, 1193, 1238, 1309, 1310, 1348, 1404, 1461]

M = {
	(215, 239, 244): "PIS",
	(204, 129, 28): "COM",
	(144, 178, 217): "IP",
	(33, 62, 98): "DC",
	(48, 93, 147): "M-1",
	(250, 255, 148): "Quiz"
}

'''
for i in range(26, 436):
	rgb_im = im.convert('RGB')
	r, g, b = rgb_im.getpixel(((55+97)/2, i))
'''

unit_length = 10 #half of COM

MON = [None for x in range(21)]
TUE = [None for x in range(21)]
WED = [None for x in range(21)]
THU = [None for x in range(21)]
FRI = [None for x in range(21)]
 
List_Dict = [MON, TUE, WED, THU, FRI]

def subject(r,g,b):
	if abs(r-215)<=15 and abs(g-239)<=15 and abs(b-244)<=15:
		return "PIS"
	elif abs(r-204)<=15 and abs(g-129)<=15 and abs(b-28)<=15:
		return "COM"
	elif abs(r-144)<=15 and abs(g-178)<=15 and abs(b-217)<=15:
		return "IP"
	elif abs(r-33)<=15 and abs(g-62)<=15 and abs(b-98)<=15:
		return "DC"
	elif abs(r-48)<=15 and abs(g-93)<=15 and abs(b-147)<=15:
		return "M-1"
	elif abs(r-250)<=15 and abs(g-255)<=15 and abs(b-148)<=15:
		return "Quiz"

def state_update(y):
	state = 0
	if y<=131 and y>41:
		state=1
	elif y<=211:
		state=2
	elif y<=284:
		state=3
	elif y<=347:
		state=4
	elif y<=347:
		state=5
	return state


state_weekday = 1

for i in range(40):
	if state_update(42+unit_length*i) != state_weekday:
		state_weekday = state_update(42+unit_length*i) 

	for Xindex in range(0, 20):
		rgb_im = im.convert('RGB')
		r, g, b = rgb_im.getpixel(((list_bb_vetical[Xindex]+list_bb_vetical[Xindex+1])/2, 42+unit_length*i))
		#print(subject(r,g,b),end=' ')
		if subject(r,g,b) != None:
			List_Dict[state_weekday-1][Xindex] = subject(r,g,b)
	#print()



s = ''
for i in List_Dict:
	for j in range(0, 21):
		s+=str(i[j])+' '
		print(i[j], end=' ')
	print()
	s+='\n'

master2 = tk.Tk()
tk.Label(master2, text=s).grid(row=0)



master2.mainloop()

# Code for updation in Google Calendar API

def time(index):
	a=['08:30:00-09:00', '09:00:00-09:30', '09:30:00-10:00', '10:00:00-10:30', '10:30:00-11:00', '11:00:00-11:30', '11:30:00-12:00', '12:00:00-12:30', '12:30:00-13:00', '13:00:00-13:30', '13:30:00-14:00', '14:00:00-14:30', '14:30:00-15:00', '15:00:00-15:30', '15:30:00-16:00', '16:00:00-16:30', '16:30:00-17:00', '17:00:00-17:30', '17:30:00-18:00','18:00:00-18:30','18:00:00-18:30']
	
	return a[index]	
	

"""
for i in range(5,436):
	rgb_im = im.convert('RGB')
	r, g, b = rgb_im.getpixel((91,i ))

	if(r==0 and g==0 and b==0):
		list_black_bars.append((91,i))
		print(i)

for i in range(5,1463):
	rgb_im = im.convert('RGB')
	r, g, b = rgb_im.getpixel((i,31 ))

	if(r==0 and g==0 and b==0):
		list_black_bars.append((i,31))
		print(i)

l=[]

for i in range(0,1463):
	for j in range(436):

		r, g, b = rgb_im.getpixel((i,j ))
					

		if(r in range(220,229) and g in range(179,187) and b in range(180,190)):
			
				l.append(j)			
				print(i,j)
"""		


scopes = ['iiitd.ac.in_13jcs9blivrpm5mjjd8qmp4ecc@group.calendar.google.com']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)



calendar_id = 'iiitd.ac.in_6o9mthgka11umpcif2cujn0hrk@group.calendar.google.com'


credentials = pickle.load(open("token.pkl","rb"))


service = build("calendar","v3",credentials=credentials)




today = datetime.date.today()
today + datetime.timedelta(days=-today.weekday(), weeks=1)



for i in range(len(List_Dict)):


	for x in range(len(List_Dict[i])):
		st=str(today.year)+'-'+str(today.month)+'-'+str(today.day)
		st=st+'T'+time(x)

		if(List_Dict[i][x]!=None):
						
			event = {
				 'summary': List_Dict[i][x],
				  'location': '',
				  'description':'' ,
				  'start': {
				    'dateTime': st,
				    'timeZone': 'Asia/Kolkata',
				  },
				  'end': {
				    'dateTime': st,
				    'timeZone': 'Asia/Kolkata',
				  },
				  'reminders': {
				    'useDefault': False,
				    'overrides': [
				      {'method': 'email', 'minutes': 24 * 60},
				      {'method': 'popup', 'minutes': 10},
				    ],
				  },
				}
			service.events().insert(calendarId=calendar_id, body=event).execute()
			
		'''
			calendar_id = 'bassampervez@iiitd.ac.in'
			event = {
	  		'summary': List_Dict[i][x],
	  		'location': '',
	 	 	'description': '',
	  		'start': {
	    	'dateTime': st,
	    	'timeZone': 'Asia/Kolkata',
	  		},
	  		'end': {
	   	 	'dateTime': st,
	    	'timeZone': 'Asia/Kolkata',
	  		},
	  		'reminders': {
	    	'useDefault': False,
	    	'overrides': [
	      	{'method': 'email', 'minutes': 24 * 60},
	     	 {'method': 'popup', 'minutes': 10},
	    	],
	  		},
			}
			'2019-9-28T09:00:00-07:00'
			service.events().insert(calendarId=calendar_id,body=event).execute()		
		'''
	today=today + datetime.timedelta(days=1)	
	print("Day has been updated!")
	



