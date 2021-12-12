def ask_forfolder():
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import Tk, filedialog
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_file = filedialog.askdirectory()
    return open_file

auto_delete = False

def install_module(module):
    try:
        import subprocess, os
        subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    except:
        pass
    
def fail():
    import colored
    print(colored.stylize("Fox installation failed. Please try again", colored.fg("red")))
    exit()
    

install_module('rich')
from rich.progress import Progress
with Progress() as progress:
    task1 = progress.add_task("[bold red]Installing Fox...", total=1000)
    while not progress.finished:
        try:
            import colored
        except:
            try:
                install_module('colored')
            except:
                fail()
        try:
            import requests
        except:
            try:
                install_module('requests')
            except:
                fail()
        progress.update(task1, advance = 333)
        url = "https://raw.githubusercontent.com/Just-A-Mango/fox/main/fox.py"
        r = requests.get(url, allow_redirects=True)
        progress.update(task1, advance = 333)
        folder = ask_forfolder()
        try:
            r = requests.get(url, allow_redirects=True)
            open(folder+'\\fox.py', 'wb').write(r.content)
        except:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, "Fox installation failed.", "F A I L", 1)
        progress.update(task1, advance = 334)
        progress.stop()
        import rich
        rich.print("👍 [bold red]Successfully installed Fox![/bold red] 👍")
        if auto_delete == True:
            import sys, os
            os.remove(sys.argv[0])