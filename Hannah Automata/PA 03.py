import tkinter as tk

# Define a function to check whether the given string follows the format a before b and b before c
def check_string(input_text):
    a_index = input_text.find('a')
    b_index = input_text.find('b')
    c_index = input_text.find('c')

    # Check if the string contains all the required characters in the correct order
    if a_index != -1 and b_index != -1 and c_index != -1 and a_index < b_index < c_index:
        return 'YES'
    else:
        return 'NO'

# Define a function to handle button click event
def on_click():
    # Get the input text from the entry widget
    input_text = entry.get()

    # Validate the input text
    if set(input_text) == set('abc'):
        # Call the check_string function to check the input text
        result = check_string(input_text)

        # Update the result label with the output
        result_label.config(text=result)
    else:
        result_label.config(text='Invalid input')

# Create a tkinter window
root = tk.Tk()
root.title('PA 03')
root.geometry('400x200')
root.resizable(False, False)

# Create a label for the title
title_label = tk.Label(root, text='PA 03', font=('Arial', 18, 'bold'), pady=10)
title_label.pack()

# Create a label for the input text
input_label = tk.Label(root, text='Enter a string (contains a, b, and c only):', font=('Arial', 12))
input_label.pack()

# Create an entry widget for the input text
entry = tk.Entry(root, width=30, font=('Arial', 12))
entry.pack()

# Create a button to trigger the checking
check_button = tk.Button(root, text='Check', font=('Arial', 12), command=on_click)
check_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text='', font=('Arial', 14, 'bold'), fg='red')
result_label.pack()

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))

# Start the tkinter main loop
root.mainloop()
