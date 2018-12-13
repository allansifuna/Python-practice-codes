from tkinter import *
class calculator_app(Frame):
    def __init__(self,master):
        super(calculator_app,self).__init__(master)
        self.task= " "
        self.UserIn= StringVar()
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.user_in=Entry(self, bg = "pink", fg="green", bd = 2,width = 17,font = ("Verdana", 20, "bold"),textvariable=self.UserIn, justify = RIGHT)
        self.user_in.grid(row=0,columnspan=5)
        #Button clear
        self.buttonce=Button(self, font=("Verdana", 10, "bold"), text='CE',width=35,height=2,command=lambda: self.cleardisplay(),bg="#66ffcc",padx=3)
        self.buttonce.grid(row=1,columnspan=5)
        # Button 7
        self.button7 = Button(self, font=("Verdana", 10, "bold"), text='7', width=8, height=4,command=lambda: self.buttonclick(7), bg="green")
        self.button7.grid(row=2, column=1)
        # Button 8
        self.button8 = Button(self, font=("Verdana", 10, "bold"), text='8', width=8, height=4,command=lambda: self.buttonclick(8), bg="green")
        self.button8.grid(row=2, column=2)
        # Button 9
        self.button9 = Button(self, font=("Verdana", 10, "bold"), text='9', width=8, height=4,command=lambda: self.buttonclick(9), bg="green")
        self.button9.grid(row=2, column=3)
        # Button +
        self.buttonplus = Button(self, font=("Verdana", 10, "bold"), text='+', width=8, height=4,command=lambda: self.buttonclick('+'), bg="green")
        self.buttonplus.grid(row=2, column=4)
        # Button 4
        self.button4 = Button(self, font=("Verdana", 10, "bold"), text='4', width=8, height=4,command=lambda: self.buttonclick(4), bg="green")
        self.button4.grid(row=3, column=1)
        # Button 5
        self.button5 = Button(self, font=("Verdana", 10, "bold"), text='5', width=8, height=4,command=lambda: self.buttonclick(5), bg="green")
        self.button5.grid(row=3, column=2)
        # Button 6
        self.button6 = Button(self, font=("Verdana", 10, "bold"), text='6', width=8, height=4,command=lambda: self.buttonclick(6), bg="green")
        self.button6.grid(row=3, column=3)
        # Button -
        self.buttonminus = Button(self, font=("Verdana", 10, "bold"), text='-', width=8, height=4,command=lambda: self.buttonclick('-'), bg="green")
        self.buttonminus.grid(row=3, column=4)
        # Button 1
        self.button1 = Button(self, font=("Verdana", 10, "bold"), text='1', width=8, height=4,command=lambda: self.buttonclick(1), bg="green")
        self.button1.grid(row=4, column=1)
        # Button 2
        self.button2 = Button(self, font=("Verdana", 10, "bold"), text='2', width=8, height=4,command=lambda: self.buttonclick(2), bg="green")
        self.button2.grid(row=4, column=2)
        # Button 3
        self.button3 = Button(self, font=("Verdana", 10, "bold"), text='3', width=8, height=4,command=lambda: self.buttonclick(3), bg="green")
        self.button3.grid(row=4, column=3)
        # Button *
        self.buttontimes = Button(self, font=("Verdana", 10, "bold"), text='*', width=8, height=4,command=lambda: self.buttonclick('*'), bg="green")
        self.buttontimes.grid(row=4, column=4)
        #button 0
        self.button0 = Button(self, font=("Verdana", 10, "bold"), text='0', width=8, height=4,command=lambda: self.buttonclick(0), bg="green")
        self.button0.grid(row=5, column=1)
        # Button .
        self.buttondot = Button(self, font=("Verdana", 10, "bold"), text='.', width=8, height=4, command=lambda: self.buttonclick('.'), bg="green")
        self.buttondot.grid(row=5, column=2)
        # Button e
        self.buttone = Button(self, font=("Verdana", 10, "bold"), text='^', width=8, height=4,command=lambda: self.buttonclick('**'), bg="green")
        self.buttone.grid(row=5, column=3)
        # Button /
        self.buttondiv = Button(self, font=("Verdana", 10, "bold"), text='/', width=8, height=4,command=lambda: self.buttonclick('/'), bg="green")
        self.buttondiv.grid(row=5, column=4)
        #button equals
        self.buttonequals=Button(self, font=("Verdana", 10, "bold"), text='=',width=35,height=4,command=lambda: self.calculate(),bg="red",padx=3)
        self.buttonequals.grid(row=6,columnspan=5)
        self.buttonequals.bind("<6>",self.calculate())
    def buttonclick(self,number):
        self.task=str(self.task)+str(number)
        self.UserIn.set(self.task)
    def calculate(self):
        self.data = self.user_in.get()
        try:
            self.task = eval(self.data)
            self.displayresults(self.task)
        except SyntaxError as e:
            self.displayresults("SyntaxError")
            self.task = " "
    def displayresults(self,value):
        self.user_in.delete(0,END)
        self.user_in.insert(0,value)
    def cleardisplay(self):
        self.task=''
        self.user_in.delete(0,END)
        self.user_in.insert(0,'0')

calculator=Tk()
app=calculator_app(calculator)
calculator.title("Allan sifuna")
calculator.resizable(width=False,height=False)
calculator.mainloop()

