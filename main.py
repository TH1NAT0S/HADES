from rich.console import Console
import pyfiglet
import sys
# Init the TUI bitch
console = Console()

ascii_banner = pyfiglet.figlet_format("HADES", font="Bloody")
console.print(f"[bold red]{ascii_banner}[/bold red]")

def show_menu():
    console.print("\n[bold red][1] START HADES (Enable AI)[/bold red]")
    console.print("[bold red][2] STAND-ALONE TOOLS[/bold red]")
    console.print("[bold red][3] EXIT[/bold red]\n")


while True:
    show_menu()
    choice = console.input("[bold red]Select an option: [/bold red]")

    if choice == "1":
        console.print("[bold red]>> Starting HADES AI...[/bold red]")
        # Add AI shit here to fucking tired to do ts rn
    elif choice == "2":
        console.print("[bold red]>> Opening Stand-Alone Tools...[/bold red]")
        # Add the whole tool menu shit here why am I doing ts at 1:47
    elif choice == "3":
        console.print("[bold red]>> Exiting...[/bold red]")
        sys.exit()
    else:
        console.print("[bold red]Invalid selection! Try again.[/bold red]")





