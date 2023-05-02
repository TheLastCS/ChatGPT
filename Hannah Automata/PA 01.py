import tkinter as tk

# Define the function to reverse the letters of each word in the string
def reverse_words(string):
    # Split the string into a list of words
    words = string.split()
    # Loop through each word in the list
    for i in range(len(words)):
        # Reverse the letters of the word and assign it back to the list
        words[i] = words[i][::-1]
    # Join the list of words back into a string
    reversed_string = " ".join(words)
    # Return the reversed string
    return reversed_string

# Create a tkinter window
window = tk.Tk()
window.title("PA 01")

# Create a label for the input prompt
input_label = tk.Label(window, text="Enter a string:")
input_label.pack(side="top", anchor="center")

# Create an entry box for the input
input_entry = tk.Entry(window)
input_entry.pack(side="top", anchor="center")

# Create a label for the output
output_label = tk.Label(window, text="Reversed string:")
output_label.pack(side="top", anchor="center")

# Create a label to display the reversed string
result_label = tk.Label(window, text="")
result_label.pack(side="top", anchor="center")

# Define the function to be executed when the button is clicked
def button_click():
    # Get the input string from the entry box
    input_string = input_entry.get()
    # Call the reverse_words function to reverse the string
    reversed_string = reverse_words(input_string)
    # Update the label to display the reversed string
    result_label.config(text=reversed_string)

# Create a button to execute the function
button = tk.Button(window, text="Reverse Words", command=button_click)
button.pack(side="top", anchor="center")

# Set window size
window.geometry("300x300")
# Run the tkinter event loop
window.mainloop()
