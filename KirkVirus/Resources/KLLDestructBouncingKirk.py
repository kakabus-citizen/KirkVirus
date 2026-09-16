import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Window size
window_width = 300
window_height = 300
root.overrideredirect(True)
root.geometry(f"{window_width}x{window_height}+0+0")
root.resizable(False, False)

# Load image
image = Image.open("kirk.ico")
image = image.resize((300, 300))

photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo, borderwidth=0)
label.pack()

label.image = photo


# Starting position
x = 0
y = 0

# Speed
dx = 18
dy = 18


def bounce_window():
    global x, y, dx, dy

    x += dx
    y += dy

    # Desktop size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Bounce from left/right
    if x <= 0 or x >= screen_width - window_width:
        dx = -dx

    # Bounce from top/bottom
    if y <= 0 or y >= screen_height - window_height:
        dy = -dy

    # Move the WHOLE WINDOW
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.after(20, bounce_window)


bounce_window()

root.mainloop()