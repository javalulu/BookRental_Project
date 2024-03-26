from tkinter import *
from PIL import ImageTk
import time
from tkinter import ttk, messagebox
import pymysql

def view_all():
  query='select * from books'
  mycursor.execute(query)
  bookTable.delete(*bookTable.get_children())
  fetched_data=mycursor.fetchall()
  for data in fetched_data:
      bookTable.insert('', END, values=data)

def search_book():

    def search_data():
        query='select * from books where ISBN = %s'
        mycursor.execute(query, (isbnEntry.get()))
        bookTable.delete(*bookTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            bookTable.insert('', END, values=data)


    search_window = Toplevel()
    search_window.title('Search Book')
    search_window.grab_set()

    isbnLabel = Label(search_window, text='ISBN', font=('times new roman', 20, 'bold'))
    isbnLabel.grid(padx=30, pady=15)
    isbnEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    isbnEntry.grid(row=0, column=1, padx=10, pady=15)

    titleLabel = Label(search_window, text='Title', font=('times new roman', 20, 'bold'))
    titleLabel.grid(padx=30, pady=15)
    titleEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    titleEntry.grid(row=1, column=1, padx=10, pady=15)

    authorLabel = Label(search_window, text='Author', font=('times new roman', 20, 'bold'))
    authorLabel.grid(padx=30, pady=15)
    authorEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    authorEntry.grid(row=2, column=1, padx=10, pady=15)

    PubLabel = Label(search_window, text='Publisher', font=('times new roman', 20, 'bold'))
    PubLabel.grid(padx=30, pady=15)
    PubEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    PubEntry.grid(row=3, column=1, padx=10, pady=15)

    PubyLabel = Label(search_window, text='Publish Year', font=('times new roman', 20, 'bold'))
    PubyLabel.grid(padx=30, pady=15)
    PubyEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    PubyEntry.grid(row=4, column=1, padx=10, pady=15)

    CopiesLabel = Label(search_window, text='Number of Copies', font=('times new roman', 20, 'bold'))
    CopiesLabel.grid(padx=30, pady=15)
    CopiesEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    CopiesEntry.grid(row=5, column=1, padx=10, pady=15)

    RentLabel = Label(search_window, text='Rental Price', font=('times new roman', 20, 'bold'))
    RentLabel.grid(padx=30, pady=15)
    RentEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    RentEntry.grid(row=6, column=1, padx=10, pady=15)

    PayLabel = Label(search_window, text='Actual Price', font=('times new roman', 20, 'bold'))
    PayLabel.grid(padx=30, pady=15)
    PayEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    PayEntry.grid(row=7, column=1, padx=10, pady=15)

    search_book_button = Button(search_window, text='Search', command=search_data)
    search_book_button.grid(row=8, columnspan=2, pady=15)

def add_book():

    def add_data():
        if isbnEntry.get()=='' or titleEntry.get()=='' or authorEntry.get()=='' or PubEntry.get()=='' or PubyEntry.get()=='' or CopiesEntry.get()=='' or RentEntry.get()=='' or PayEntry.get()=='':
            messagebox.showerror('Error', 'All Fields are required', parent=add_window)
        else:
            try:
                query='insert into books values(%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(isbnEntry.get(), titleEntry.get(), authorEntry.get(), PubEntry.get(), PubyEntry.get(), CopiesEntry.get(), RentEntry.get(), PayEntry.get()))
                con.commit()
                result=messagebox.askyesno('Data added successfully. Do you want to clear the form', parent=add_window)
                if result:
                    isbnEntry.delete(0,END)
                    titleEntry.delete(0, END)
                    authorEntry.delete(0, END)
                    PubEntry.delete(0, END)
                    PubyEntry.delete(0, END)
                    CopiesEntry.delete(0, END)
                    RentEntry.delete(0, END)
                    PayEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'ISBN Code cannot be repeated', parent=add_window)
                return

            query='select * from books'
            mycursor.execute(query)
            fetchedData=mycursor.fetchall()
            bookTable.delete(*bookTable.get_children())
            for data in fetchedData:
                bookTable.insert('', END, values=data)

    add_window=Toplevel()
    add_window.grab_set()

    isbnLabel=Label(add_window, text='ISBN', font=('times new roman', 20, 'bold'))
    isbnLabel.grid(padx=30, pady=15)
    isbnEntry=Entry(add_window,font=('roman', 15, 'bold'), width=24)
    isbnEntry.grid(row=0, column=1,padx=10, pady=15)

    titleLabel = Label(add_window, text='Title', font=('times new roman', 20, 'bold'))
    titleLabel.grid(padx=30, pady=15)
    titleEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    titleEntry.grid(row=1, column=1, padx=10, pady=15)

    authorLabel = Label(add_window, text='Author', font=('times new roman', 20, 'bold'))
    authorLabel.grid(padx=30, pady=15)
    authorEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    authorEntry.grid(row=2, column=1, padx=10, pady=15)

    PubLabel = Label(add_window, text='Publisher', font=('times new roman', 20, 'bold'))
    PubLabel.grid(padx=30, pady=15)
    PubEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    PubEntry.grid(row=3, column=1, padx=10, pady=15)

    PubyLabel = Label(add_window, text='Publish Year', font=('times new roman', 20, 'bold'))
    PubyLabel.grid(padx=30, pady=15)
    PubyEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    PubyEntry.grid(row=4, column=1, padx=10, pady=15)

    CopiesLabel = Label(add_window, text='Number of Copies', font=('times new roman', 20, 'bold'))
    CopiesLabel.grid(padx=30, pady=15)
    CopiesEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    CopiesEntry.grid(row=5, column=1, padx=10, pady=15)

    RentLabel = Label(add_window, text='Rental Price', font=('times new roman', 20, 'bold'))
    RentLabel.grid(padx=30, pady=15)
    RentEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    RentEntry.grid(row=6, column=1, padx=10, pady=15)

    PayLabel = Label(add_window, text='Actual Price', font=('times new roman', 20, 'bold'))
    PayLabel.grid(padx=30, pady=15)
    PayEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    PayEntry.grid(row=7, column=1, padx=10, pady=15)

    add_book_button=Button(add_window, text='Add Book', command=add_data)
    add_book_button.grid(row=8,columnspan=2,pady=15)

def del_book():
  def del_data():
    if isbnEntry.get() == '' or CopiesEntry.get() == '':
      messagebox.showerror('Error', 'All Fields are required', parent=add_window)
    else:
      try:
        # Check if the book with the given ISBN exists
        query_select = 'SELECT * FROM books WHERE ISBNCode = %s'
        mycursor.execute(query_select, (isbnEntry.get(),))
        book = mycursor.fetchone()
        if book is None:
          messagebox.showerror('Error', 'Book not found with provided ISBN', parent=add_window)
        else:
          # Update the number of copies available
          new_copies = int(book[5]) - int(CopiesEntry.get())  # Subtracting the copies to delete
          if new_copies < 0:
            messagebox.showerror('Error', 'Number of copies to delete exceeds available copies', parent=add_window)
            return

          query_update = 'UPDATE books SET CopiesAvailable = %s WHERE ISBNCode = %s'
          mycursor.execute(query_update, (new_copies, isbnEntry.get()))
          con.commit()
          result = messagebox.askyesno('Data deleted successfully. Do you want to clear the form', parent=add_window)
          if result:
            isbnEntry.delete(0, END)
            CopiesEntry.delete(0, END)
          else:
            pass

        # Refresh the book table display
        query = 'select * from books'
        mycursor.execute(query)
        fetchedData = mycursor.fetchall()
        bookTable.delete(*bookTable.get_children())
        for data in fetchedData:
          datalist = list(data)
          bookTable.insert('', END, values=datalist)

      except Exception as e:
        messagebox.showerror('Error', str(e), parent=add_window)

  add_window = Toplevel()
  add_window.grab_set()

  isbnLabel = Label(add_window, text='ISBN', font=('times new roman', 20, 'bold'))
  isbnLabel.grid(padx=30, pady=15)
  isbnEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
  isbnEntry.grid(row=0, column=1, padx=10, pady=15)

  CopiesLabel = Label(add_window, text='Copies', font=('times new roman', 20, 'bold'))
  CopiesLabel.grid(padx=30, pady=15)
  CopiesEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
  CopiesEntry.grid(row=1, column=1, padx=10, pady=15)

  del_book_button = Button(add_window, text='Delete Book', command=del_data)
  del_book_button.grid(row=2, columnspan=2, pady=15)

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
sliderLabel.place(x=250,y=0)
count=0
text=''

def slider():
    global text, count
    if count<len(s):
        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
    sliderLabel.after(100,slider)



slider()

#Left Frame
leftFrame = Frame(window, bg='gray')
leftFrame.place(x=50,y=80, width=400, height=600)

#(logo)
logo_image=PhotoImage(file='logo.png')
logoLabel=Label(leftFrame, image=logo_image)
logoLabel.grid(row=0, column=0)

#(buttons)
addButton_PlaceOrder=Button(leftFrame, text='Place Order', cursor='hand2', state=DISABLED)
addButton_PlaceOrder.grid(row=1, column=0, padx=100, pady=20)

addButton_ReturnBooks=Button(leftFrame, text='Return Books', cursor='hand2', state=DISABLED)
addButton_ReturnBooks.grid(row=2, column=0, pady=20)

addButton_Viewall=Button(leftFrame, text='View All Available Books', cursor='hand2', state=DISABLED)
addButton_Viewall.grid(row=3, column=0, pady=20)

addButton_Search=Button(leftFrame, text='Search', cursor='hand2', state=DISABLED)
addButton_Search.grid(row=4, column=0, pady=20)

addButton_Overdue=Button(leftFrame, text='Overdue Orders', cursor='hand2', state=DISABLED)
addButton_Overdue.grid(row=5, column=0, pady=20)

addButton_add=Button(leftFrame, text='Add New Books', cursor='hand2', command=add_book, state=DISABLED)
addButton_add.grid(row=6, column=0, pady=20)

addButton_del=Button(leftFrame, text='Delete Books', command=del_book, cursor='hand2', state=DISABLED)
addButton_del.grid(row=7, column=0, pady=20)

#Right Frame
rigthFrame=Frame(window)
rigthFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rigthFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rigthFrame,orient=VERTICAL)

bookTable=ttk.Treeview(rigthFrame,columns=('CustomerID', 'Name', 'Email', 'Phone Number', 'Address', 'RentalID',
                                           'Rental Starts Date', 'Due Date', 'Return Date', 'Rental Fee', 'ISBN Code', 'Title',
                                           'Author', 'Publisher', 'Publish Year', 'Copies Available', 'Rental Price', 'Actual Price'),
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
bookTable.heading('Actual Price',text='Actual Price')

bookTable.config(show='headings')

#Login Buttom
def connect_database():

    #Login_command
    def login():
        global mycursor,con
        try:
            con=pymysql.connect(user=usernameEntry.get(), password=passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo('Success', 'LOGGED IN')
            connectWindow.destroy()
            addButton_PlaceOrder.config(state=NORMAL)
            addButton_ReturnBooks.config(state=NORMAL)
            addButton_Viewall.config(state=NORMAL)
            addButton_Search.config(state=NORMAL)
            addButton_Overdue.config(state=NORMAL)
            addButton_add.config(state=NORMAL)
            addButton_del.config(state=NORMAL)
        except:
            messagebox.showerror('Error', 'Please enter the correct username or password', parent=connectWindow)

        query = 'use book_rental_shop_database'
        mycursor.execute(query)



    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x200+530+230')
    connectWindow.title('Login To Database')
    connectWindow.resizable(0,0)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=0, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=0, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=1, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=1, column=1, padx=40, pady=20)

    connectButtom = ttk.Button(connectWindow, text='LOGIN', cursor='hand2', command=login)
    connectButtom.grid(row=5, columnspan=2)

connectButtom = Button(window, text='Login', command=connect_database, width=8, height=2, fg='white',
                       bg = 'cornflowerblue', activebackground='cornflowerblue', activeforeground='white',
                       cursor='hand2')
connectButtom.place(x=1050, y=30)


window.mainloop()