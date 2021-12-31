def install_module(module):
    import subprocess, os
    subprocess.call(["pip", "install", module], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
try:
    import requests
except:
    install_module('requests')

def show_menu():
    import os, rich
    os.system('cls' if os.name=='nt' else 'clear')
    print('\033[1m\33[92mFOX - Installer\033[0m')
    print("---------------")
    print(' 1. Download & Install Fox')
    print(' 2. Uninstall Fox')
    print("----")
    index = int(input('>> '))
    if index == 1:
        import os
        os.system('cls' if os.name=='nt' else 'clear')
        print("\033[91mDownloading & Installing Fox...\033[0m |          |")
        from pathlib import Path
        Path("C:/Fox/").mkdir(parents=True, exist_ok=True)
        url = 'https://github.com/just-a-mango/fox/raw/main/fox.py'
        r = requests.get(url, allow_redirects=True)
        try:
            os.remove('C:/Fox/fox.exe')
        except:
            pass
        os.system('cls' if os.name=='nt' else 'clear')
        print("\033[91mDownloading & Installing Fox...\033[0m |██        |")
        open('C:/Fox/fox.exe','wb').write(r.content)
        os.system('cls' if os.name=='nt' else 'clear')
        print("\033[91mDownloading & Installing Fox...\033[0m |████      |")
        import sys
        sys.path.append('C:/Fox/')
        os.system('cls' if os.name=='nt' else 'clear')
        print("\033[91mDownloading & Installing Fox...\033[0m |████████  |")
        os.system('cls' if os.name=='nt' else 'clear')
        print("\033[91mDownloading & Installing Fox...\033[0m |██████████|")
        print('\033[1m\033[91mSuccessfully downloaded and installed \33[92mFox\x1B[3m\033[0m')
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