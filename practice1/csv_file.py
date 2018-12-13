## start.py
print('start')

#from tkinter import *
from tkinter import *
import os
from PIL import ImageTk, Image

class MyClass:
    '''This is my class.'''

    imgpath = '/Users/user/Dropbox/Camera Uploads'
    imgfile = 'susshi.jpg'
    #imgfilepath = os.path.join(self.imgpath, self.imgfile)
    imgfilepath = os.path.join(imgpath, imgfile)


    def __init__(self,master):
        print('in __init__')

        # Create and load a frame into the tk (tkinter) window.
        frame = Frame(master)
        frame.pack()

        # Create and load two buttons in to the above-created frame.
        self.button = Button(frame, text="QUIT", fg="red", command=quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame, text="Hello", command = self.f)
        self.slogan.pack(side=RIGHT)

        # Bind a key to each button from above.
        master.bind('q', quit)
        master.bind('f', self.f)

        # Open the image, resize it...
        self.image = Image.open(self.imgfilepath)
        self.image.thumbnail((600,600))
        # Make a tkinter-friendly image object ...
        self.display_image = ImageTk.PhotoImage(self.image)
        # Make a tkinter canvas, plug in the image, and pack the canvas.
        self.canvas = Canvas(master, bg='red')
        self.canvas.create_image(0,0, image=self.display_image, anchor="nw")
        self.canvas.pack(fill=BOTH, expand=1)
        ### FIXME: Set canvas focus!

    def f(self, event=None):
        print('in f()')
        return 'hello world'

    def get_image_list(self):
        pass

    def next_image(self):
        pass

    def previous_image(self):
        pass

    def load_image(self):
        #stub
        pass

    def update_image(self):
        pass

root = Tk()
abc = MyClass(root)
root.mainloop()

print('abc has been defined')
print('"abc.f()" returns "%s"' % abc.f())
#print str(abc.f)
#print repr(abc.f)

print('end')