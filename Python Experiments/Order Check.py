import tkinter as tk

def check_language(input_str):
    stack = []
    for char in input_str:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if not stack or stack[-1] != 'a':
                return 'NO'
            stack.pop()
        elif char == 'c':
            if not stack or stack[-1] != 'b':
                return 'NO'
            stack.pop()
        else:
            return 'NO'
    if not stack:
        return 'YES'
    else:
        return 'NO'

def on_submit():
    input_str = input_entry.get()
    result_label.config(text=check_language(input_str))

root = tk.Tk()
root.title("Language L Checker")

input_label = tk.Label(root, text="Enter input string:")
input_label.pack(padx=20, pady=20)

input_entry = tk.Entry(root)
input_entry.pack(padx=20, pady=20)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(padx=20, pady=20)

result_label = tk.Label(root, text="")
result_label.pack(padx=20, pady=20)

root.geometry("600x400")
root.mainloop()
