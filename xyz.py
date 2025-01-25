# import everything from tkinter module
import turtle
from tkinter import *

turtle.Screen()
def level1():
    turtle.Screen()
    import level1
def level2():
    turtle.Screen()
    import level2
def level3():
    turtle.Screen()
    import level3
def level4():
    turtle.Screen()
    import level4
def Help():
    turtle.Screen()
    import help
def About():
    print ("This is a simple example of a menu")
      
# create a tkinter window 
root = Tk()               
root.title('Game menu')

# Open window having dimension 300x300 
root.geometry('300x200')  
  
# Create a Button
btn = Button(root, text = 'MAIN MENU\n LEVELS',fg='red')
btn.pack()
#button 1
btn = Button(root, text = 'level-1 !', bd = '5', fg='blue',command = level1)
btn.pack()

#button 2
btn = Button(root, text = 'level-2 !', bd = '5', fg='green',command = level2)
btn.pack()

#button 3
btn = Button(root, text = 'level-3 !', bd = '5', fg='orange',command = level3)
btn.pack()

#button 4
btn = Button(root, text = 'level-4 !', bd = '5', fg='black',command = level4)
btn.pack()

#button 1
btn = Button(root, text = 'Help !', bd = '5', fg='blue',command = Help)
btn.pack(side=LEFT)

#button 5 for exit
btn = Button(root, text = 'Exit !', bd = '5',fg='red', command = root.destroy)     
btn.pack(side=RIGHT)     
  
root.mainloop() 
