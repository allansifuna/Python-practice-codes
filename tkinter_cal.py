from tkinter import *
class calc(Frame):
    def __init__(self,master):
        super(calc,self).__init__(master)
        self.task=""
        self.UserIn= StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.User_input=Entry(self,textvariable=self.UserIn,width=16,justify=RIGHT)
        self.User_input.grid(columnspan=12)

        self.button1=Button(self,width=2,text=1,command=lambda: self.buttonclick(1))
        self.button1.grid(column=2, row=1)
        self.button1 = Button(self, width=2, text=2, command=lambda: self.buttonclick(2))
        self.button1.grid(column=3, row=1)
        self.button1 = Button(self, width=2, text=3, command=lambda: self.buttonclick(3))
        self.button1.grid(column=4, row=1)
        self.button1 = Button(self, width=2, text=4, command=lambda: self.buttonclick(4))
        self.button1.grid(column=5, row=1)
        self.button1 = Button(self, width=2, text='+', command=lambda: self.buttonclick('+'))
        self.button1.grid(column=2, row=2)
        self.button1 = Button(self, width=2, text='/', command=lambda: self.buttonclick('/'))
        self.button1.grid(column=3, row=2)
        self.button1 = Button(self, width=2, text='*', command=lambda: self.buttonclick('*'))
        self.button1.grid(column=4, row=2)
        self.button1 = Button(self, width=2, text="=", command=lambda: self.calculate())
        self.button1.grid(column=5, row=2)
        self.button1 = Button(self, width=10, text="Delete", command=lambda: self.clearresults())
        self.button1.grid(columnspan=5, row=3)
    def buttonclick(self,number):
        self.task=str(self.task)+str(number)
        self.UserIn.set(self.task)
    def calculate(self):
        self.data=self.User_input.get()
        try:
            self.task=eval(self.data)
            self.displayresults(self.task)
        except SyntaxError as e:
            self.displayresults("Fuck you")
            self.task = " "
    def displayresults(self,value):
        self.User_input.delete(0,END)
        self.User_input.insert(0,value)

    def clearresults(self):
        self.task=" "
        self.User_input.delete(0,END)

calculator = Tk()

calculator.title("Namasaka Allan Sifuna")
app = calc(calculator)
# Make window fixed (cannot be resized)
calculator.resizable(width = True, height = True)

calculator.mainloop()