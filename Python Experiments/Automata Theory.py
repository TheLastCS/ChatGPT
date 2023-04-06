import tkinter as tk
from tkinter import messagebox

class MyGUI:
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        # Set the size of the app
        app_width = 800
        app_height = 600
        
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Label of the app
        self.label = tk.Label(self.root, text="Exercise 1", font=('Arial', 18), anchor='w', justify="left")
        self.label.pack(padx=20, pady=20)
        
        self.label1 = tk.Label(self.root, text="Write a program that reverses all letters each word in a string", font=('Arial', 14), anchor='w', justify="left")
        self.label1.pack(padx=20, anchor="w")
        
        self.textboxFrame = tk.Frame(self.root)
        self.textboxFrame.columnconfigure(0, weight=1)
        self.textboxFrame.columnconfigure(1, weight=1)
        self.textboxFrame.columnconfigure(2, weight=1)
        self.textboxFrame.columnconfigure(3, weight=1)
        self.textboxFrame.rowconfigure(0, weight=1)
        self.textboxFrame.rowconfigure(1, weight=1)
        
        
        self.textbox1 = tk.Text(self.textboxFrame, height=3, font=("Arial", 16))
        self.textbox1.grid(row = 0, columnspan = 2, sticky = tk.W+tk.E)

        # self.textbox2 = tk.Text(self.textboxFrame, height=3, font=("Arial", 16))
        # self.textbox2.grid(row = 0, column = 1, sticky = tk.W+tk.E)
        # self.textbox2.config(state="disabled")
        
        # button 1
        self.button = tk.Button(self.textboxFrame, text="Enter", font=("Arial",12), command=self.reverseWords)
        self.button.grid(row=1,column=0)
        
        #button 2
        self.button = tk.Button(self.textboxFrame, text="Clear", font=("Arial",12), command=self.clearWords)
        self.button.grid(row=1,column=1)
        
        
        self.textboxFrame.pack(padx=20)
        
        #Exercise 2
        self.textboxFrame2 = tk.Frame(self.root)
        
        self.label = tk.Label(self.root, text="Exercise 2", font=('Arial', 18), anchor='w', justify="left")
        self.label.pack(padx=20, pady=20)
        
        self.label1 = tk.Label(self.root, text="Write a that accepts string containing even a's and odd b's", font=('Arial', 14), anchor='w', justify="left")
        self.label1.pack(padx=20, anchor="w")
        
        self.textboxFrame1 = tk.Frame(self.root)
        self.textboxFrame1.columnconfigure(0, weight=1)
        self.textboxFrame1.columnconfigure(1, weight=1)
        self.textboxFrame1.columnconfigure(2, weight=1)
        self.textboxFrame1.columnconfigure(3, weight=1)
        self.textboxFrame1.rowconfigure(0, weight=1)
        self.textboxFrame1.rowconfigure(1, weight=1)
        
        self.textbox2 = tk.Text(self.textboxFrame1, height=3, font=("Arial", 16))
        self.textbox2.grid(row = 0, columnspan=2, sticky = tk.W+tk.E)
        
        # button 1
        self.button = tk.Button(self.textboxFrame1, text="Enter", font=("Arial",12), command=self.checkEven)
        self.button.grid(row=1,column=0)
        
        #button 2
        self.button = tk.Button(self.textboxFrame1, text="Clear", font=("Arial",12), command=self.clearWords1)
        self.button.grid(row=1,column=1)
        
        
        self.textboxFrame1.pack(padx=20)
        
        # Calculate the x and y coordinates of the top-left corner of the app
        x = (screen_width // 2) - (app_width // 2)
        y = (screen_height // 2) - (app_height // 2)
        
        # Set the position of the app
        self.root.geometry(f"{app_width}x{app_height}+{x}+{y}")
        self.root.title("Automata Exercise")
        
        self.root.mainloop()
    
    def reverseWords(self):
        stringInput = self.textbox1.get('1.0', tk.END)
        print(stringInput)
        if stringInput =="\n":
            messagebox.showinfo(title="Error", message="No text inputted")
        else:
            # Split the string into words
            words = stringInput.split()

            # Reverse each word
            reversed_words = [word[::-1] for word in words]

            # Join the reversed words back into a string
            reversed_string = ' '.join(reversed_words)
            print(reversed_string)
            messagebox.showinfo(title="Result", message=reversed_string)
    
    def clearWords(self):
        self.textbox1.delete('1.0', tk.END)
    
    def clearWords1(self):
        self.textbox2.delete('1.0', tk.END)
        
    
    def checkEven(self):
        s = self.textbox2.get('1.0', tk.END)
        count_a = 0
        count_b = 0
        for c in s:
            if c == 'a':
                count_a += 1
            elif c == 'b':
                count_b += 1
        if count_a % 2 == 0 and count_b % 2 == 1:
            messagebox.showinfo(title="Result", message="Pass")
        else:
            messagebox.showinfo(title="Result", message="Fail")
MyGUI()