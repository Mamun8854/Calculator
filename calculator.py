from tkinter import *

root = Tk()
root.title('Smart Calculator')
root.config(bg="green")
root.geometry("680x490+100+100")

entryField = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "red", "e",
                    "0", ".", "%", "=", "log10", "(", ")", "x!"]

row_value = 1
column_value = 0

for i in button_text_list:
    button = Button(root, height=2, width=5, bd=2, relief=SUNKEN, text=i, bg="green", fg='white',
                font=('arial', 18, 'bold'), activebackground='black', activeforeground='white')
    button.grid(row=row_value, column=column_value)
    column_value+=1
    if column_value > 7:
        row_value+=1
        column_value=0
root.mainloop()