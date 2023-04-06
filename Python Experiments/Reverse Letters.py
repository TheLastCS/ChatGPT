import tkinter as tk

def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def reverse_text():
    text = input_text.get('1.0', 'end-1c')
    reversed_text = reverse_words(text)
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', reversed_text)

root = tk.Tk()
root.title("Word Reverser")

input_label = tk.Label(root, text="Enter text:")
input_label.pack(padx=20, pady=20)

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

reverse_button = tk.Button(root, text="Reverse Words", command=reverse_text)
reverse_button.pack(padx=20, pady=20)

output_label = tk.Label(root, text="Reversed text:")
output_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.geometry("600x400")
root.mainloop()
