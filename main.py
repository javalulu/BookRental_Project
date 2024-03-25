from tkinter import *
from PIL import ImageTk
import time

window = Tk()

window.geometry('1174x680+50+20')

window.title('Book Rental Store')

backgroundImage = ImageTk.PhotoImage(file='img.png')
backgroundLabel = Label(window, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

#date and time
def clock():
    date = time.strftime('%d/%m/%y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)


datetimeLabel = Label(window, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

#Title
s = 'Book Rental Management System'
sliderLabel = Label(window, text=s, font=('arial',28,'italic bold'), width=30)
sliderLabel.place(x=200,y=0)
count=0
text=''

def slider():
    global text, count
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(100,slider)

slider()

window.mainloop()」