from tkinter import *
import tkinter as tk
import requests
import time
from datetime import *
import json
# import tktable
 
window = Tk()
 
window.title("Issues Count")
 
window.geometry('650x300')
 
lbl = Label(window, text="Github URL")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=20)
 
txt.grid(column=1, row=0)



# mainloop()
 
def clicked():
 
    
    repourl = txt.get()
    root = Tk()
    scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox = Listbox(root)
    listbox.pack()
    spliturl = repourl.split('/')
    org = spliturl[3]
    repo = spliturl[4] 
    openRequestURL = 'https://api.github.com/search/issues?q=repo:' + org + '/' + repo + '+type:issue+state:open'
    last24hourTimeStamp = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
    last7DaysTimeStamp = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')
    last24HourOpenRequestURL = openRequestURL + '+created:>' + last24hourTimeStamp
    last7DaysOpenRequestURL = openRequestURL + '+created:>' + last24hourTimeStamp
    response = requests.get(openRequestURL)
    totalOpenRequests = json.loads(response.content)['total_count']
    response = requests.get(last24HourOpenRequestURL)
    last24HourOpenRequests = json.loads(response.content)['total_count']
    response = requests.get(last7DaysOpenRequestURL)
    last7DaysOpenRequests = json.loads(response.content)['total_count']
    listbox.insert(END, 'Total')
    listbox.insert(END, totalOpenRequests)
    listbox.insert(END, '< 24 Hours')
    listbox.insert(END, last24HourOpenRequests)
    listbox.insert(END, '> 24 Hours < 7 Days')
    listbox.insert(END, last7DaysOpenRequests - last24HourOpenRequests)
    listbox.insert(END, '> 7 Days')
    listbox.insert(END, totalOpenRequests - last7DaysOpenRequests)

    # for i in range(100):
    #     listbox.insert(END, i)
    
    # bind listbox to scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # lbl.configure(text= res)
 

btn = Button(window, text="Submit", command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()