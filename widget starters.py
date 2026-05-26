import tkinter as tk

# create window
window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x250")
window.configure(bg="#d9e6f2")   # light blue background (you can change this)

# description label
desc_label = tk.Label(window, text="This app multiplies two numbers.",
                      bg="#d9e6f2", font=("Arial", 12))
desc_label.pack(pady=5)

# first number label + entry
label1 = tk.Label(window, text="Enter first number:", bg="#d9e6f2")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

# second number label + entry
label2 = tk.Label(window, text="Enter second number:", bg="#d9e6f2")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")

# button
calc_button = tk.Button(window, text="Calculate Product",
                        command=calculate_product, bg="#b3cde0")
calc_button.pack(pady=5)

# result text box
result_box = tk.Text(window, height=3, width=30)
result_box.pack(pady=5)

window.mainloop()