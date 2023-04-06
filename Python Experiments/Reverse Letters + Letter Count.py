import tkinter as tk

def reverse_words(string):
    words = string.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

def check_letters(string):
    a_count = 0
    b_count = 0
    for letter in string:
        if letter == 'a':
            a_count += 1
        elif letter == 'b':
            b_count += 1
    if a_count % 2 == 0 and b_count % 2 == 1:
        return 'The string contains an even number of letter "a" and an odd number of letter "b".'
    else:
        return 'The string does not meet the requirements.'

def on_button_click():
    input_string = entry.get()
    reversed_string = reverse_words(input_string)
    result_text.set(reversed_string + '\n\n' + check_letters(input_string))

# GUI
window = tk.Tk()
window.title('Reverse Words and Check Letters')

input_label = tk.Label(window, text='ENTER A STRING:')
input_label.pack(padx=20, pady=20)

entry = tk.Entry(window, width=50)
entry.pack(padx=20, pady=20)

button = tk.Button(window, text='Reverse Words and Check Letters', command=on_button_click)
button.pack(padx=20, pady=20)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

window.geometry("600x400")
window.mainloop()
