import tkinter as tk

def even_a_odd_b(string):
    count_a = 0
    count_b = 0
    for i in range(len(string)):
        if string[i] == 'a':
            count_a += 1
        elif string[i] == 'b':
            count_b += 1
    if count_a % 2 == 0 and count_b % 2 == 1:
        return "String contains even letter 'a' and odd letter 'b'"
    else:
        return "String does not contain even letter 'a' and odd letter 'b'"

def check_string():
    string = entry.get()
    result = even_a_odd_b(string)
    output.config(text=result)

# Create GUI
root = tk.Tk()
root.title("Even Letter 'a' and Odd Letter 'b' Checker")

# Create input box and button
entry = tk.Entry(root)
entry.pack(padx=20, pady=20)
button = tk.Button(root, text="Check", command=check_string)
button.pack(padx=20, pady=20)

# Create output label
output = tk.Label(root, text="")
output.pack()

# Start GUI
root.geometry("600x400")
root.mainloop()
