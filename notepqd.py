from tkinter import*
from tkinter.filedialog import asksaveasfilename, askopenfilename

window= Tk()
window.title("Bob's  text editor")
window.geometry("600x600")
window.rowconfigure(0, weight=1,minsize=800)
window.columnconfigure(1, weight=1,minsize=800)
