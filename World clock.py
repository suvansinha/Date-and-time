from datetime import datetime
import pytz
from tkinter import *
import time

root=Tk()
root.geometry("300x250")


def times():
    home=pytz.timezone('Asia/Kolkata')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    print(current_time)
    clock.config(text=current_time)
    name.config(text="India")
    
    
    home=pytz.timezone('Europe/London')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    print(current_time)
    clock1.config(text=current_time)
    name1.config(text="London")
    
    
    home=pytz.timezone('America/New_York')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    print(current_time)
    clock2.config(text=current_time)
    name2.config(text="New York")

    
    home=pytz.timezone('Australia/Sydney')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    print(current_time)
    clock3.config(text=current_time)
    name3.config(text="Sydney")
    
    clock.after(200,times)
    
name=Label(root,font=("times",20,"bold"))
name.place(x=30,y=5)
clock=Label(root,font=("times",25,"bold"))
clock.place(x=10, y=40)
nota=Label(root,text="Hours  minutes  seconds",font="times 10 bold")
nota.place(x=10, y=80)

name1=Label(root,font=("times",20,"bold"))
name1.place(x=330,y=5)
clock1=Label(root,font=("times",25,"bold"))
clock1.place(x=310, y=40)
nota1=Label(root,text="Hours  minutes  seconds",font="times 10 bold")
nota1.place(x=310, y=80)

name2=Label(root,font=("times",20,"bold"))
name2.place(x=30,y=105)
clock2=Label(root,font=("times",25,"bold"))
clock2.place(x=10, y=140)
nota2=Label(root,text="Hours  minutes  seconds",font="times 10 bold")
nota2.place(x=10, y=180)

name3=Label(root,font=("times",20,"bold"))
name3.place(x=330,y=105)
clock3=Label(root,font=("times",25,"bold"))
clock3.place(x=310, y=140)
nota3=Label(root,text="Hours  minutes  seconds",font="times 10 bold")
nota3.place(x=310, y=180)

times()

root.mainloop()







