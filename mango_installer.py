import rich, os
def display_menu():
    os.system('cls' if os.name=='nt' else 'clear')
    rich.print("[bold red]:mango: MANGO - INSTALLER :mango:[/bold red]")
    rich.print("[italic magenta]Select one of the following:[/italic magenta] \n   1.[italic][underline]Install [/underline][bold]Mango[/italic][/bold] \n   2.[italic][underline]Uninstall [/underline][bold]Mango[/italic][/bold]")
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
    display_menu()
    choice = input(" ")
    if choice == "1":
        install()
        break
    elif choice == "2":
        uninstall()
        break
    else:
        display_menu()