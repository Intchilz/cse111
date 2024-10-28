from tkinter import *
import time


# define main window

traffic_lights = Tk()
traffic_lights.title('Traffic Lights')
traffic_lights.geometry('300x400+300+150')
traffic_lights.resizable(False, False)
traffic_lights.iconbitmap('traffic icon.ico')
traffic_lights.config(bg='#4ea6a1')

# define widgets
myCanvas = Canvas(traffic_lights, height=400, width=300, bg="White")
myCanvas.pack()

myCanvas.create_rectangle(100,50,200,350, fill='#4ea6a1',width=2)

# define functions
a = 10

while True:
    
    def green():
        try:
            for i in range(a):
                green = myCanvas.create_oval(100,50,200,150, fill='Green', width=2)
                traffic_lights.update()
                time.sleep(0.50)
        except TclError as tk_error:
            green = myCanvas.create_oval
            
    def greenb():
        for i in range(a):
            green = myCanvas.create_oval(100,50,200,150, fill='Black', width=2)
            traffic_lights.update()
            time.sleep(0.0001)
            
    def orange():
        for i in range(a):
            green = myCanvas.create_oval(100,150,200,250, fill='Orange', width=2)
            traffic_lights.update()
            time.sleep(0.05)
            
    def orangeb():
        for i in range(a):
            green = myCanvas.create_oval(100,150,200,250, fill='Black', width=2)
            traffic_lights.update()
            time.sleep(0.00001)
    
    def red():
        for i in range(a):
            green = myCanvas.create_oval(100,250,200,350, fill='Red', width=2)
            traffic_lights.update()
            time.sleep(0.05)    
            
    def redb():
        for i in range(a):
            green = myCanvas.create_oval(100,250,200,350, fill='Black', width=2)
            traffic_lights.update()
            time.sleep(0.00001)

#its not about how I call them          
    green()
    greenb()
    orange()
    orangeb()
    red()
    redb()

# looping main window
traffic_lights.mainloop()