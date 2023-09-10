from tkinter import *

root = Tk()
root.title('Smart Calculator')
root.config(bg="green")
root.geometry("680x490+100+100")

entryField = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0)
button = Button(root, height=2, width=5, bd=2, relief=SUNKEN, text='C', bg="green", fg='white')
button.grid(row=1, column=0)
root.mainloop()