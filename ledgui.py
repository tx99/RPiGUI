import RPi.GPIO as GPIO
from Tkinter import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT) #green
GPIO.setup(16, GPIO.OUT) #red
GPIO.setup(22, GPIO.OUT) #blue

window = Tk()
window.title("LED Control")

window.geometry('300x240')

def green():
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)

def red():
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)

def blue():
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)

rad1 = Radiobutton(window,text="Green", value=1,command=green)
rad2 = Radiobutton(window,text="Red", value=2,command=red)
rad3 = Radiobutton(window,text="Blue",value=3,command=blue)

rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)


window.mainloop()
