import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.overrideredirect(True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")
root.attributes("-topmost", True)

# Load PNG
original_image = Image.open("israel.ico").convert("RGBA")

# Resize PNG to 300x300
original_image = original_image.resize((290, 290), Image.Resampling.LANCZOS)

label = tk.Label(root, bg="black", borderwidth=0)
label.pack()

angle = 0

def rotate():
    global angle

    angle = (angle + 5) % 360

    rotated = original_image.rotate(
        -angle,
        resample=Image.Resampling.BICUBIC,
        expand=False
    )

    photo = ImageTk.PhotoImage(rotated)
    label.config(image=photo)
    label.image = photo

    root.after(20, rotate)


# Window size
window_width = 500
window_height = 500

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center position
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Put window in the middle
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

rotate()
root.mainloop()