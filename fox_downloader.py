def install_module(module):
    import subprocess, os
    subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
try:
    import rich,colored,requests
except:
    install_module('rich')
    install_module('colored')
    install_module('requests')

def show_menu():
    import os, rich
    os.system('cls' if os.name=='nt' else 'clear')
    rich.print('[bold green]FOX - Installer[/bold green]')
    print("---------------")
    print(' 1. Download & Install Fox')
    print(' 2. Uninstall Fox')
    print("----")
    index = int(input('>> '))
    if index == 1:
        import os

        from rich.progress import Progress

        with Progress() as progress:
            os.system('cls' if os.name=='nt' else 'clear')
            task1 = progress.add_task("[red]Downloading & Installing Fox...", total=1000)

            while not progress.finished:
                from pathlib import Path
                Path("C:/Fox/").mkdir(parents=True, exist_ok=True)
                url = 'https://github.com/just-a-mango/fox/raw/main/fox.py'
                r = requests.get(url, allow_redirects=True)
                try:
                    os.remove('C:/Fox/fox.exe')
                except:
                    pass
                open('C:/Fox/fox.exe','wb').write(r.content)
                progress.update(task1, advance=500)
                import sys
                sys.path.append('C:/Fox/')
                progress.update(task1, advance=500)
        os.system('cls' if os.name=='nt' else 'clear')
        rich.print('[bold red]Successfully downloaded and installed [italic green]Fox[/italic green][/bold red]')
        from msvcrt import getch
        print("Press any key to quit...")
        junk = getch()
    elif index == 2:
        import shutil
        shutil.rmtree('C:/Fox/')
        os.system('cls' if os.name=='nt' else 'clear')
    else:
        pass
    
show_menu()