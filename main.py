import tkinter as tk


def main():
  """
      Creates and runs a simple Tkinter 'Hello, World!' application.
          """
  # Create the main application window
  root = tk.Tk()

  # Set the title of the window
  root.title("Hello Tkinter")

  # Create a label widget with the text "Hello, World!"
  label = tk.Label(root, text="Hello, World!")

  # Use the pack geometry manager to add the label to the window
  # and add some padding around it.
  label.pack(padx=20, pady=20)

  # Start the Tkinter event loop to display the window
  root.mainloop()


if __name__ == "__main__":
  main()
