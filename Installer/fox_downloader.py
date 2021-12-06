from ctypes import sizeof
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label


def ask_forfolder():
    from tkinter import filedialog

    from tkinter import Tk, filedialog

    root = Tk()
    root.withdraw()

    root.attributes('-topmost', True)

    open_file = filedialog.askdirectory()
    return open_file

def download_and_install():
    try:
        import requests
        url = "https://raw.githubusercontent.com/Just-A-Mango/fox/main/fox.py"
        folder = ask_forfolder()
        r = requests.get(url, allow_redirects=True)
        open(folder+'\\fox.py', 'wb').write(r.content)
        label = Label(window, text='Successfully downloaded and installed Fox! 😀')
        label.pack()
        import ctypes  # An included library with Python install.
        ctypes.windll.user32.MessageBoxW(0, "Fox was successfully installed 😀!", "SUCCESS!", 0)
        window.quit()
    except:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "Fox installation failed.", "F A I L", 1)
        

window = tk.Tk()
window.title("Fox Installer")
window.geometry("250x200")
window.tk.call("source", "sun-valley.tcl")
window.tk.call("set_theme", "dark")
window.style = ttk.Style()
MyLab = Label(window, text="FOX", font=("Poppins",50))
MyLab.pack()
import time
time.sleep(1)
MyLab['text'] = "FOX"
button = ttk.Button(
    text="Download Fox",
    command=lambda: download_and_install(),
    style="Accent.TButton"
    )
button.pack(pady=40)
window.update()
import time
MyLab['text'] = "</*"
window.update()
time.sleep(0.22)
MyLab['text'] = "<O*"
window.update()
time.sleep(0.22)
MyLab['text'] = ">OX"
window.update()
time.sleep(0.22)
MyLab['text'] = "FOX"
window.update()
window.mainloop()