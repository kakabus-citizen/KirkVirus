import tkinter as tk
import colorsys
import ctypes

root = tk.Tk()

root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.5)
root.overrideredirect(True)

hwnd = ctypes.windll.user32.GetParent(root.winfo_id())

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 0x00000020

style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

ctypes.windll.user32.SetWindowLongW(
    hwnd,
    GWL_EXSTYLE,
    style | WS_EX_LAYERED | WS_EX_TRANSPARENT
)

hue = 0

def rainbow():
    global hue

    hue = (hue + 0.01) % 1.0

    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

    color = "#{:02x}{:02x}{:02x}".format(
        int(r * 255),
        int(g * 255),
        int(b * 255)
    )

    root.configure(bg=color)
    root.after(20, rainbow)

rainbow()

root.mainloop()