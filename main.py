
import tkinter as tk

def greet():
	name = entry.get()
	if name.strip():
		label.config(text=f"Hello, {name}!")
	else:
		label.config(text="Hello, World!")

root = tk.Tk()
root.title("Hello, World! App")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Greet Me!", command=greet)
button.pack(pady=5)

label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=10)

root.mainloop()


