from tkinter import *

root = Tk()
root.title('Smart Calculator')
root.config(bg="green")
root.geometry("550x450+100+100")

entryField = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white')
entryField.grid(row=0, column=0)

root.mainloop()