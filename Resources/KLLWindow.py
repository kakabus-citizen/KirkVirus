import tkinter as tk
from tkinter import ttk
import random
import subprocess
import os

#window funkce
root = tk.Tk()
root.title("Kirk Library Launcher")
root.geometry("590x400")
root.resizable(width=False, height=False)
root.iconbitmap("kirk.ico")

label1 = tk.Label(root, text="KIRK LIBRARY")
label1.pack()

label2 = tk.Label(root, text="DISCLAIMER: This Is ScareWare it May Crash Your Pc")
label2.pack()

print("Initializing")

# progress funkce
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate",
    maximum=100
)
progress.pack(pady=30)

label = tk.Label(root, text="0%")
label.pack()

#button = tk.Button(
#    root,
#    text="Continue",
#    command=lambda: subprocess.Popen(["python", "KLLDestruct.py"]) 
#)

button = tk.Button(
    root,
    text="Launch",
    command=lambda: (
        subprocess.Popen(["python", "KLLDestructLibrary.py"]),
        root.destroy()
    )
)

value = 0

def fake_loading():
    global value

    if value < 67:
        # udela to ze se posune a nekdy ne
        if random.randint(1, 3) != 1:
            value += 1

        progress["value"] = value
        label.config(text=f"{value}%")

        # random zpomaleni
        delay = random.randint(100, 800)

        root.after(delay, fake_loading)

    else:
        # ukaze na 67
        button.pack(pady=15)


fake_loading()


#end
root.mainloop()