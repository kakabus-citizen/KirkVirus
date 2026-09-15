import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Loading")
root.geometry("400x250")

# Show ICO image
icon_image = tk.PhotoImage(file="kirk.ico")
icon_label = tk.Label(root, image=icon_image)
icon_label.pack(pady=10)


progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate",
    maximum=100
)
progress.pack(pady=20)

label = tk.Label(root, text="0%")
label.pack()

button = tk.Button(
    root,
    text="Continue",
    command=lambda: print("Button clicked")
)

value = 0

def fake_loading():
    global value

    if value < 67:
        if random.randint(1, 3) != 1:
            value += 1

        progress["value"] = value
        label.config(text=f"{value}%")

        delay = random.randint(500, 1500)
        root.after(delay, fake_loading)

    else:
        button.pack(pady=15)


fake_loading()

root.mainloop()