def ask_forfolder():
    import tkinter as tk
    from tkinter import filedialog

    from tkinter import Tk, filedialog

    root = Tk()
    root.withdraw()

    root.attributes('-topmost', True)

    open_file = filedialog.askdirectory()
    return open_file

def install_module(module):
    try:
        import subprocess
        subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    except:
        pass
    
def fail():
    import colored
    print(colored.stylize("Fox installation failed. Please try again", colored.fg("red")))

try:
    from rich.progress import Progress
except:
    try:
        install_module('rich')
    except:
        fail()

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
        gif_url = 'https://media.giphy.com/media/3ornk57KwDXf81rjWM/giphy.gif'
        r = requests.get(url, allow_redirects=True)
        rtwo = requests.get(gif_url, allow_redirects=True)
        progress.update(task1, advance = 333)
        folder = ask_forfolder()
        try:
            r = requests.get(url, allow_redirects=True)
            open(folder+'\\fox.py', 'wb').write(r.content)
        except:
            fail()
            
        open(folder+'\\hmm.gif', 'wb').write(rtwo.content)
        progress.update(task1, advance = 334)
        progress.stop()
        import rich
        rich.print("👍 [bold red]Successfully installed Fox![/bold red] 👍")