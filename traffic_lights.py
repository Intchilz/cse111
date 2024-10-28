'''
    This is a simple traffic light program.
    Modules;
        1. tkinter
        2. time
    I have also written test functions in
    another python file 'test_traffic_lights' 
'''
from tkinter import *
import time


# Here I define the main window
traffic_lights = Tk()
traffic_lights.title('Traffic Lights')
traffic_lights.geometry('300x400+300+150')
traffic_lights.resizable(False, False)
traffic_lights.iconbitmap('traffic icon.ico')
traffic_lights.config(bg='#4ea6a1')

def main():
    #Here, I define the widgets
    myCanvas = Canvas(traffic_lights, height=400, width=300, bg="White")
    myCanvas.pack()

    myCanvas.create_rectangle(100,50,200,350, fill='#4ea6a1',width=2)
    
    a = 10
    
    while True:
    
        green(myCanvas, a)
        greenb(myCanvas, a)
        orange(myCanvas, a)
        orangeb(myCanvas, a)
        red(myCanvas, a)
        redb(myCanvas, a)
        
        
# Here, I define 6 functions.
# red, redb, orange, orangeb, green and greenbs   
def red(canvas, a):
    try:
        for i in range(a):
            green = canvas.create_oval(100,250,200,350, fill='Red', width=2)
            traffic_lights.update()
            time.sleep(0.09)
    except TclError as tk_error:
        print(tk_error)    

def redb(canvas, a):
    try:
        for i in range(a):
            green = canvas.create_oval(100,250,200,350, fill='Black', width=2)
            traffic_lights.update()
            time.sleep(0.00001)
    except TclError as tk_error:
        print(tk_error)
        
def orange(canvas, a):
    try:
        for i in range(a):
            green = canvas.create_oval(100,150,200,250, fill='Orange', width=2)
            traffic_lights.update()
            time.sleep(0.05)
    except TclError as tk_error:
        print(tk_error)

def orangeb(canvas, a):
    try:
        for i in range(a):
            green = canvas.create_oval(100,150,200,250, fill='Black', width=2)
            traffic_lights.update()
            time.sleep(0.00001)
    except TclError as tk_error:
        print(tk_error)
        
def green(canvas, a):
    try:
        for i in range(a):
            green = canvas.create_oval(100,50,200,150, fill='Green', width=2)
            traffic_lights.update()
            time.sleep(0.50)
    except TclError as tk_error:
        print(tk_error)
        
def greenb(myCanvas, a):
    try:
        for i in range(a):
            green = myCanvas.create_oval(100,50,200,150, fill='Black', width=2)
            traffic_lights.update()
            time.sleep(0.00001)
    except TclError as tk_error:
        print(tk_error)    

# A call to main function to run the program
if __name__ == '__main__':
    main()