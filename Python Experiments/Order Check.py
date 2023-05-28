import tkinter as tk

# Define a function to check whether the given string follows the format a before b and b before c
def check_string(input_str):
    a_index = input_str.find('a')
    b_index = input_str.find('b')
    c_index = input_str.find('c')

    # Check if the string contains all the required characters in the correct order
    if a_index != -1 and b_index != -1 and c_index != -1 and a_index < b_index < c_index:
        return 'YES'
    else:
        return 'NO'

# Define a function to handle button click event
def on_click():
    # Get the input text from the entry widget
    input_text = entry.get()

    # Call the check_string function to check the input text
    result = check_string(input_text)

    # Update the result label with the output
    result_label.config(text=result)

# Create a tkinter window
root = tk.Tk()
root.title('String Checker')
root.geometry('300x150')
root.resizable(False, False)

# Create a label for the input text
label = tk.Label(root, text='Enter a string:')
label.pack(pady=10)

# Create an entry widget for the input text
entry = tk.Entry(root, width=30)
entry.pack()

# Create a button to trigger the checking
button = tk.Button(root, text='Check', command=on_click)
button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text='')
result_label.pack()

# Start the tkinter main loop
root.mainloop()
