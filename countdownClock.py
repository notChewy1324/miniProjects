from tkinter import *
from turtle import position
from playsound import playsound
import time

positionX = 800
positionY = 600

root = Tk()
root.geometry(f'{positionX}x{positionY}')
root.resizable(0,0)
root.config(bg="black")
root.title('Countdown Clock')
Label(root, text = 'Countdown Clock and Timer' , font = 'arial 20 bold',  bg ='white').pack()

Label(root, font ='arial 15 bold', text = 'current time :', bg = 'white').place(x = (positionX/2) ,y = (positionY/2))

def clock():
    clockTime = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clockTime)
    curr_time.after(1000,clock)
    
curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='white')
curr_time.place(x = (positionX/2) , y = 70)
clock()

sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=(positionY/2))
sec.set('00')
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=(positionY/2))
mins.set('00')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=(positionY/2))
hrs.set('00')
        
def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
   
        root.update()
        time.sleep(1)
        if(times == 0):
            playsound('Loud_Alarm_Clock_Buzzer.mp3')
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
        

Label(root, font ='arial 15 bold', text = 'set the time',   bg ='white').place(x = (positionX/2) ,y = 150)
Button(root, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold').place(x=(positionX/2), y=210)
 
root.mainloop()


# TODO: update looks