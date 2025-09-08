


import tkinter as tk
import requests
import json

def get_joke():
	category = entry.get().strip().lower()
	if not category:
		category = "general"
	url = f"https://official-joke-api.appspot.com/jokes/{category}/random"
	try:
		response = requests.get(url)
		response.raise_for_status()
		jokes = response.json()
		if isinstance(jokes, list) and jokes:
			joke = jokes[0]
			setup = joke.get('setup', '')
			punchline = joke.get('punchline', '')
			label.config(text=f"{setup}\n{punchline}")
		else:
			if category != "general":
				label.config(text=f"No jokes found for category '{category}'. Try 'programming' or leave empty for general jokes.")
			else:
				label.config(text="No jokes available at the moment.")
	except Exception as e:
		label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Random Joke App")

tk.Label(root, text="Joke Category (try 'programming' or leave empty):").pack(pady=(10,0))
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Get Joke", command=get_joke)
button.pack(pady=5)

label = tk.Label(root, text="Click 'Get Joke' for a random joke!", wraplength=400, justify="left", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()


