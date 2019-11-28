from tkinter import *

def mouse_move(event):
    print("Mouse Move", event.x, event.y)
    global x ,y
    canvas.create_line(x, y, event.x, event.y, fill="blue")
    x = (event.x)
    y = (event.y)
    

def button_pressed(event):
    print("Button Pressed", event.x, event.y)
    global x ,y
    x = (event.x)
    y = (event.y)    

def button_released(event):
    print("Button Release", event.x, event.y)
    global x ,y
    x = (event.x)
    y = (event.y) 

    
def reset_paint():
    canvas.delete("all")
    print("reset_paint()")

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<Button-1>", button_pressed)
canvas.bind("<ButtonRelease-1>", button_released)
button = Button(window, text="리셋", command=reset_paint)
button.pack()

window.mainloop()