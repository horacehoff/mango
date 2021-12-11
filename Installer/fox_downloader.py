from ctypes import sizeof
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
auto_delete = True
def ask_forfolder():
    from tkinter import filedialog

    from tkinter import Tk, filedialog

    root = Tk()
    root.withdraw()

    root.attributes('-topmost', True)

    open_file = filedialog.askdirectory()
    return open_file

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        import sys
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def fixBadZipfile(zipFile):  
 f = open(zipFile, 'r+b')  
 data = f.read()  
 pos = data.find('\x50\x4b\x05\x06') # End of central directory signature  
 if (pos > 0):  
     f.seek(pos + 22)   # size of 'ZIP end of central directory record' 
     f.truncate()  
     f.close()  

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
        shutil.rmtree(os.getcwd()+'\\theme\\')
        os.remove(os.getcwd()+'\\sun-valley.tcl')
        os.remove(os.getcwd()+'\\theme.zip')
        os.remove(os.getcwd()+'\\icon.ico')
        shutil.rmtree(os.getcwd()+'\\Sun-Valley-ttk-theme-1.0\\')
        import sys
        if auto_delete == True:
            os.remove(sys.argv[0])
    except:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "Fox installation failed.", "F A I L", 1)
        

window = tk.Tk()
window.title("Fox Installer")
window.geometry("250x200")
url = "https://github.com/rdbende/Sun-Valley-ttk-theme/archive/refs/tags/v1.0.zip"
import requests, os
r = requests.get(url, allow_redirects=True)
with open(os.getcwd()+'\\theme.zip', 'wb') as f:
    f.write(r.content)
    f.close()
url = "https://github.com/Just-A-Mango/just-a-mango.github.io/raw/main/images/output-onlinepngtools.ico"
import requests, os
r = requests.get(url, allow_redirects=True)
with open(os.getcwd()+'\\icon.ico', 'wb') as f:
    f.write(r.content)
    f.close()
window.iconbitmap(os.getcwd()+'\\icon.ico')
import shutil
shutil.unpack_archive('theme.zip', os.getcwd())
shutil.move(os.getcwd()+'\\Sun-Valley-ttk-theme-1.0\\sun-valley.tcl', os.getcwd()+'\\sun-valley.tcl')
shutil.move(os.getcwd()+'\\Sun-Valley-ttk-theme-1.0\\theme\\', os.getcwd()+'\\theme\\')
window.tk.call("source", os.getcwd()+"\\sun-valley.tcl")
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
button.pack(pady=45)
window.update()
import time
MyLab['text'] = "<\*"
window.update()
time.sleep(0.22)
MyLab['text'] = "<O^"
window.update()
time.sleep(0.22)
MyLab['text'] = ">OX"
window.update()
time.sleep(0.22)
MyLab['text'] = "FOX"
window.update()
window.mainloop()