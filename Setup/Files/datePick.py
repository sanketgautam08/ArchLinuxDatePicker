#!/usr/bin/python

from tkinter import *
from tkcalendar import *
import os

root = Tk()
root.title('Pick Date')
root.geometry("700x500")

cal = Calendar(root, selectmode="day", year=2021, month=7, day=30)
cal.pack(pady=20, fill="both", expand=True)

enterTime = Label(root, text = "Enter Time(24hr Format)", font=("Helvetica", 16))
enterTime.pack(pady=5)


# timeTxtBox = Text(root,width =20, height=4)
# timeTxtBox.pack(padx=20) 

v = StringVar()
entryBox = Entry(root, textvariable = v, bg = "white", fg = "black", bd = 5, justify = "center", font =("Arial", 20) , width = 10)
entryBox.pack(pady= 5)

timeExample = Label(root, text = "For eg. 15:34", font=("Helvetica", 12))
timeExample.pack(pady=5)

def getDate():
	dateLabel.config(text=cal.get_date())

	dateExtract = dateLabel.cget("text")
	print(f'Date: {dateExtract}')

	splitDate = dateExtract.split("/")
	day = splitDate[1]
	year = int(splitDate[2]) +2000
	month = int(splitDate[0])
	monthStr = ""

	# print(splitDate[0])

	if month == 1:
		monthStr = "JAN"
	elif month == 2:
		monthStr = "FEB"
	elif month == 3:
		monthStr = "MAR"
	elif month == 4:
		monthStr = "APR"
	elif month == 5:
		monthStr = "MAY"
	elif month == 6:
		monthStr = "JUN"
	elif month == 7:
		monthStr = "JUL"
	elif month == 8:
		monthStr = "AUG"
	elif month == 9:
		monthStr = "SEP"
	elif month == 10:
		monthStr = "OCT"
	elif month == 11:
		monthStr = "NOV"
	elif month == 12:
		monthStr = "DEC"

	# def retrieve_input():
	# 	input = entryBox.get()

    
	# timeExtracted = retrieve_input()
	# print (timeExtracted)

	timeExtracted = v.get()
	print (f'Time: {timeExtracted}')

	timeFormatted = f'{timeExtracted}:00'

	dateFormatted = f'sudo date --set="{day} {monthStr} {year} {timeFormatted}"'
	# sudo date --set="27 JUL 2021 10:49:00"
	dateforLabel.config(text=dateFormatted)
	# print(dateFormatted)
	root.destroy()
	command = f"cd ~ && {dateFormatted}"
	print (f'Your Date: {dateFormatted}')
	os.system(dateFormatted)
	exit()
	# os.system("konsole -e 'bash -c \""+dateFormatted+";bash\"'")




enterTime = Label(root, text = "Enter time(HH:MM)")

btn = Button(root, text= "Set Date And Time", command = getDate)
btn.pack(pady=40)

dateLabel = Label(root, text="")
dateLabel.pack(pady=20)

dateforLabel = Label(root, text="")
dateforLabel.pack(pady=20)


root.mainloop()




enterTime = Label(root, text = "Enter time(24hr Format)", font=("Helvetica", 16))
enterTime.pack(pady=5)