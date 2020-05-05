from tkinter import *
import tkinter.font as TheFont
from gpiozero import LED
import RPi.GPIO as GPIO

#Initialise pins
GPIO.setmode(GPIO.BCM)
Red = LED(2)
Green = LED(3)
Blue = LED(4)
#sit size of window
win = Tk()
var = IntVar()
win.title("LED Lights")
win.geometry('800x500')
#The font
myFont = TheFont.Font(family = 'Calibri', size = 12, weight = "bold")
#The function to toggle the light
def ledToggle():
    #Red
    if var.get()==1:
        Red.on()
        Green.off()
        Blue.off()
    #Green
    if var.get()==2:
        Green.on()
        Blue.off()
        Red.off()
    #Blue
    if var.get()==3:
        Blue.on()
        Green.off()
        Red.off()
#Function to exit the program
def exitProgram():
    GPIO.cleanup()
    win.destroy()
#Create the exit button
exitButton = Button (win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM)
#Create the radio button for LEDs
L1 = Radiobutton(win, text = "Red", font = myFont, variable=var, value=1, command = ledToggle)
L1.pack(anchor=W)

L2 = Radiobutton(win, text = "Green", font = myFont, variable=var, value=2, command = ledToggle)
L2.pack(anchor=W)

L3 = Radiobutton(win, text = "Blue", font = myFont, variable=var, value=3, command = ledToggle)
L3.pack(anchor=W)
#Run the program
mainloop()