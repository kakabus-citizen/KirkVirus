import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg="black")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

image = Image.open("KirkSplash.png")
image = image.resize((screen_width, screen_height))

photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo, borderwidth=0)
label.pack(fill="both", expand=True)

root.after(999999, root.destroy)

root.mainloop()