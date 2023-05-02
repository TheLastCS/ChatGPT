import tkinter as tk

def octal_to_binary():
    octal_num = octal_input.get()
    # convert octal to binary
    binary_num = bin(int(octal_num, 8))[2:]
    binary_output.config(state='normal')
    binary_output.delete(0, tk.END)
    binary_output.insert(0, binary_num)
    binary_output.config(state='readonly')

# Create a tkinter window
window = tk.Tk()
window.title("PA 04")
window.geometry("400x200")
window.resizable(False, False)
# Create input label and entry
octal_label = tk.Label(window, text="Enter an octal number:")
octal_label.pack(pady=(20,5))
octal_input = tk.Entry(window)
octal_input.pack()
# Create output label and entry
binary_label = tk.Label(window, text="Binary equivalent:")
binary_label.pack(pady=5)
binary_output = tk.Entry(window, state='readonly')
binary_output.pack()
# Create convert button
convert_button = tk.Button(window, text="Convert", command=octal_to_binary)
convert_button.pack(pady=10)
# Center all elements
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Run the tkinter event loop
window.mainloop()
