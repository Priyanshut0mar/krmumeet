


#import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound


################### Initialized window####################

root = Tk()
root.geometry('500x300')
root.resizable(10,10)
root.config(bg = '#FFE873')
root.title('TECHARGE - TEXT TO SPEECH')

#heading
Label(root, text = 'TEXT TO SPEECH' , font='Verdana 30 bold' , bg ='white smoke').place(x=30,y=10)
Label(root, text ='Techarge' , font ='Verdana 15 bold', bg = 'white smoke').place(x=190,y=260)
#label
Label(root, text ='Enter Text', font ='Verdana 15 bold', bg ='white smoke').place(x=30,y=70)
#text variable
Msg = StringVar()
#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=30 , y=120)
###################define function##############################

#Function to Convert Text to Speech in Python
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Techarge.mp3')
    playsound('Techarge.mp3')
    
    
#Function to Exit  
def Exit():
    root.destroy()

#Function to Reset  
def Reset():
    Msg.set("")
#Button
Button(root, text = "PLAY" , font = 'Verdana 15 bold', command = Text_to_speech, width =4).place(x=30, y=150)
Button(root,text = 'EXIT',font = 'Verdana 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=150)
Button(root, text = 'RESET', font='Verdana 15 bold', command = Reset).place(x=185 , y =150)
#infinite loop to run program
root.mainloop()
