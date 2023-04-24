import tkinter as tk

def convert_octal_to_binary():
    octal_num = octal_entry.get()
    # Remove any leading zeros from the input string
    octal_num = octal_num.lstrip('0')
    # Convert the octal string to binary
    binary_num = bin(int(octal_num, 8))[2:]
    # Update the result label
    result_label.config(text=binary_num)

# Create the tkinter window
window = tk.Tk()
window.title("Octal to Binary Converter")

# Create the input label and entry field
input_label = tk.Label(window, text="Enter an octal number:")
input_label.pack(padx=20, pady=20)
octal_entry = tk.Entry(window)
octal_entry.pack(padx=20, pady=20)

# Create the convert button
convert_button = tk.Button(window, text="Convert", command=convert_octal_to_binary)
convert_button.pack(padx=20, pady=20)

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack(padx=20, pady=20)

# Run the tkinter event loop
window.geometry("600x400")
window.mainloop()
