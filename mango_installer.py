try:
    import rich, os
except:
    import subprocess
    subprocess.call(["pip", "install", "rich"], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
    import sys
    os.system(" ".join(sys.argv))
def display_menu():
    os.system('cls' if os.name=='nt' else 'clear')
    return input("""\
        +-----------------------+
        |  🥭Mango Installer🥭  |
        +-----------------------+
        |    1.Install Mango    |
        |                       |
        |   2.Uninstall Mango   |
        +-----------------------+
            Your choice: """)
def install():
    os.system('cls' if os.name=='nt' else 'clear')
    rich.print("[bold red]:mango: MANGO - INSTALLER :mango:[/bold red]")
    rich.print("[italic]Installing [bold]:mango: Mango :mango:[/bold][/italic][white]...[/white]")
    from rich.progress import Progress
    import time
    dir = input("Enter desired installation directory: ")
    with Progress() as progress:
        task1 = progress.add_task("[red]Installing...", total=1000)
        while not progress.finished:
            progress.update(task1, advance=0.5)
            time.sleep(0.02)
def uninstall():
    os.system('cls' if os.name=='nt' else 'clear')
    rich.print("[bold red]:mango: MANGO - INSTALLER :mango:[/bold red]")
    print("Unyikes")
while True:
    choice = display_menu()
    if choice == "1":
        install()
        break
    elif choice == "2":
        uninstall()
        break
    else:
        display_menu()