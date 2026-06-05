from tkinter import*


window= Tk()
window.title("Event Handler")
window.geometry("500x600")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>",handle_keypress)   

def handle_click(event):
    print("\nThe Bob the XII junior prince was crowned king!")

button=Button(text="very confidental im not joking")
button.pack()

button.bind("<Button-1>",handle_click)

window.mainloop()