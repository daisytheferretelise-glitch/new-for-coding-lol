from tkinter import*
from datetime import date

root= Tk()
root.title("getting started with aliens")
root.geometry("400x300")

lb1 = Label(text ="Hey there",fg="black",bg="purple",height=1,width =300)

name_lb1= Label(text="Fullname",bg="lightblue")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="welcome to the BOB application! \nTodays BOBS date is   :"
    greet="Hello"+ name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height =3)
btn=Button(text="Press Me!",command =display,height=1,bg="pink",fg="yellow")
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()