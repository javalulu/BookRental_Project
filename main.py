from tkinter import *
from PIL import ImageTk
import time
from tkinter import ttk

window = Tk()

window.geometry('1280x720+50+20')

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


datetimeLabel = Label(window, font=('times new roman', 7, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

#Title
s = 'Book Rental Management System'
sliderLabel = Label(window, text=s, font=('arial',14,'italic bold'), width=30)
sliderLabel.place(x=400,y=0)
count=0
text=''

def slider():
    global text, count
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(100,slider)

slider()

#Left Frame
leftFrame = Frame(window, bg='gray')
leftFrame.place(x=50,y=80, width=175, height=450)
#(logo)
logo_image=PhotoImage(file='logo.png')
logoLabel=Label(leftFrame, image=logo_image)
logoLabel.grid(row=0, column=0, pady=10)
#(buttons)
addButton_PlaceOrder=Button(leftFrame,text='Place Order')
addButton_PlaceOrder.grid(row=1, column=0, pady=10)

addButton_ReturnBooks=Button(leftFrame,text='Return Books')
addButton_ReturnBooks.grid(row=2, column=0, pady=10)

addButton_Viewall=Button(leftFrame,text='View All Available Books')
addButton_Viewall.grid(row=3, column=0, pady=10)

addButton_Search=Button(leftFrame,text='Search')
addButton_Search.grid(row=4, column=0, pady=10)

addButton_Overdue=Button(leftFrame,text='Overdue Orders')
addButton_Overdue.grid(row=5, column=0, pady=10)

addButton_add=Button(leftFrame,text='Add New Books')
addButton_add.grid(row=6, column=0, pady=10)

addButton_del=Button(leftFrame,text='Delete Books')
addButton_del.grid(row=7, column=0, pady=10)


#Right Frame
rigthFrame=Frame(window)
rigthFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rigthFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rigthFrame,orient=VERTICAL)

bookTable=ttk.Treeview(rigthFrame,columns=('CustomerID', 'Name', 'Email', 'Phone Number', 'Address', 'RentalID',
                                           'Rental Starts Date', 'Due Date', 'Return Date', 'Rental Fee', 'ISBN Code', 'Title',
                                           'Author', 'Publisher', 'Publish Year', 'Copies Available', 'Rental Price'),
                       xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=bookTable.xview)
scrollBarY.config(command=bookTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

bookTable.pack(fill=BOTH, expand=1)

bookTable.heading('CustomerID',text='CustomerID')
bookTable.heading('Name',text='Name')
bookTable.heading('Email',text='Email')
bookTable.heading('Phone Number',text='Phone Number')
bookTable.heading('Address',text='Address')
bookTable.heading('RentalID',text='RentalID')
bookTable.heading('Rental Starts Date',text='Rental Starts Date')
bookTable.heading('Due Date',text='Due Date')
bookTable.heading('Return Date',text='Return Date')
bookTable.heading('Rental Fee',text='Rental Fee')
bookTable.heading('ISBN Code',text='ISBN Code')
bookTable.heading('Title',text='Title')
bookTable.heading('Author',text='Author')
bookTable.heading('Publisher',text='Publisher')
bookTable.heading('Publish Year',text='Pubilsh Year')
bookTable.heading('Copies Available',text='Copies Available')
bookTable.heading('Rental Price',text='Rental Price')


bookTable.config(show='headings')


window.mainloop()