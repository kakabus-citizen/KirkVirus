import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.overrideredirect(True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")
root.attributes("-topmost", True)

# Load image
original_image = Image.open("zuck.ico").convert("RGBA")

# Resize to 300x300
original_image = original_image.resize(
    (300, 300),
    Image.Resampling.LANCZOS
)

label = tk.Label(root, bg="black", borderwidth=0)
label.pack()

angle = 0

def rotate():
    global angle

    angle = (angle + 9) % 360

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
window_width = 390
window_height = 390

# Get screen size
screen_width = root.winfo_screenwidth()

# TOP RIGHT
x = screen_width - window_width
y = 0

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

rotate()

root.mainloop()