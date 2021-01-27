import random
from tkinter import *
from graphics import*

def setUpWindow():
    #set graphics window + background color
    win=GraphWin("Foreign Flash Cards", 800,600)
    win.setCoords(0,0,10,10)
    win.setBackground("light blue")
    
    message=Text(Point(5,9.3),"¡Hola! Let’s Study Spanish!")
    message.setFace("arial")
    message.setStyle("bold italic")
    message.setSize(36)
    message.setFill("white")
    message.draw(win)

    img=Image(Point(5,5),"flag.jpg")
    img.draw(win)

    #draw text entry box for entering name
    nameDisplay=Text(Point(2.8,8),"Enter your name")
    nameDisplay.setFace("arial")
    nameDisplay.setStyle("bold")
    nameDisplay.setSize(22)
    nameDisplay.setFill("white")
    nameDisplay.draw(win)

    #setting name of input box
    nameInput=Entry(Point(5,8),9)
    nameInput.setFace("arial")
    nameInput.setSize(27)
    nameInput.setTextColor("pink")
    nameInput.draw(win)

    #make a fake button for clicking for next page
    button=Rectangle(Point(6.3,7.7),Point(7.4,8.3))
    button.setFill("lightgray")
    button.draw(win)
        
    enterButton1=Text(Point(6.85,8),"Enter")
    enterButton1.setFace("courier")
    enterButton1.setStyle("bold")
    enterButton1.draw(win)

    output = Text(Point(2,1),"")
    output.draw(win)

    kgBox=Entry(Point(3.3, 5.5), 10)
    kgBox.setText("0.0") 
    kgBox.draw(win)
    
    win.getMouse() 
    kg=float(kgBox.getText())
    poundsdisplay.setText()

        
def main():
    count = 0
    score = 0
    #input output files
    file1 = open('English.txt', 'r')
    file2 = open('Spanish.txt', 'r')

    f1content = file1.readlines()
    f2content = file2.readlines()
    
    win=setUpWindow()
main()




