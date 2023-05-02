import tkinter as tk

def is_even_a_odd_b(s):
    # Initialize counters for a's and b's
    count_a = 0
    count_b = 0
    
    # Loop through each character in the string
    for c in s:
        if c == 'a':
            count_a += 1
        elif c == 'b':
            count_b += 1
    
    # Check if the string has even a's and odd b's
    if count_a % 2 == 0 and count_b % 2 == 1:
        return "YES"
    else:
        return "NO"

# Create a function to handle button click event
def handle_click():
    # Get the input string from the entry widget
    s = entry.get()

    # Check if the input string is in the language L
    result = is_even_a_odd_b(s)

    # Update the label text with the result
    label.config(text=result)

# Create the GUI
root = tk.Tk()
root.title("PA 02")
root.geometry("400x150")

# Create the input label and entry widget
input_label = tk.Label(root, text="Enter a string containing even a's and odd b's:")
input_label.pack(pady=(20, 5))
entry = tk.Entry(root)
entry.pack(pady=5)

# Create the button widget
button = tk.Button(root, text="Check", command=handle_click)
button.pack(pady=5)

# Create the result label
label = tk.Label(root, text="")
label.pack()

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

# Start the main event loop
root.mainloop()
