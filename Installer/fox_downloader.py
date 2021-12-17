def ask_forfolder():
    try:
        import os
    except:
        fail()
    try:
        os.mkdir('C:/Fox')
    except:
        pass
    open_file = 'C:/Fox'
    return open_file

def prompt():
    #Import the tkinter library
    from tkinter import Tk
    from tkinter import Label
    from tkinter import messagebox
    #Create an instance of Tkinter frame
    win= Tk()
    #Define the geometry of the function
    win.geometry("750x250")
    answer = messagebox.askyesno("Question","Do you like Python Tkinter?")
    #Create a Label
    Label(win, text=answer, font= ('Georgia 20 bold')).pack()
    win.mainloop()

auto_delete = False
def install_module(module):
    import subprocess, os
    subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    
def fail():
    try:
        import colored
    except:
        install_module('colored')
        import colored
    print(colored.stylize("Fox installation failed. Please try again", colored.fg("red")))
    exit()

try:
    from rich.progress import Progress
except:
    install_module('rich')
    from rich.progress import Progress
with Progress() as progress:
    task1 = progress.add_task("[bold red]Installing Fox...", total=1000)
    while not progress.finished:
        try:
            import colored
        except:
            install_module('colored')
            import colored
        try:
            import requests
        except:
            install_module('requests')
            import requests
        progress.update(task1, advance = 333)
        url = "https://raw.githubusercontent.com/Just-A-Mango/fox/main/fox.py"
        r = requests.get(url, allow_redirects=True)
        progress.update(task1, advance = 333)
        folder = ask_forfolder()
        try:
            r = requests.get(url, allow_redirects=True)
            open(folder+'\\fox.py', 'wb').write(r.content)
        except:
            fail()
        progress.update(task1, advance = 334)
        progress.stop()
        import rich
        rich.print("👍 [bold red]Successfully installed Fox![/bold red] 👍")
        if auto_delete == True:
            import sys, os
            os.remove(sys.argv[0])