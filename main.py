from rich.console import Console
from rich.panel import Panel
import pyfiglet
import sys
import subprocess  # <-- This lets us start NYX
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize Console and AI Model
console = Console()
model = OllamaLLM(model="llama3")
template = """
Answer the question below.

Here is the conversation history:
{context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def show_cover_art():
    art = """
        (\__/)
        (•ㅅ•)  <-- Evil eyes glowing red
        / \\🩸
    """
    console.print(Panel.fit(f"[bold red]{art}[/bold red]", title="[bold red]WELCOME TO HADES[/bold red]"))

def show_title():
    ascii_banner = pyfiglet.figlet_format("HADES", font="Bloody")
    console.print(f"[bold red]{ascii_banner}[/bold red]")

def show_main_menu():
    console.print("\n[bold red][1] START HADES AI[/bold red]")
    console.print("[bold red][2] STAND-ALONE TOOLS[/bold red]")
    console.print("[bold red][3] SETTINGS[/bold red]")
    console.print("[bold red][4] EXIT[/bold red]\n")

def start_nyx():
    """Starts NYX as a separate process"""
    console.print("\n[bold red]>> Starting NYX AI...[/bold red]")
    subprocess.Popen(["python3", "nyx.py"])  # Runs NYX in the background
    console.print("[bold red]>> NYX is now running![/bold red]\n")

def tools_menu():
    console.print("\n[bold red]>> Stand-Alone Tools Menu[/bold red]")
    console.print("[bold red][1] DNS Sinkhole[/bold red]")
    console.print("[bold red][2] Port Scanner[/bold red]")
    console.print("[bold red][3] Return to Main Menu[/bold red]\n")
    choice = console.input("[bold red]Select a tool: [/bold red]")
    if choice == "1":
        console.print("[bold red]>> DNS Sinkhole Activated (Placeholder)[/bold red]")
    elif choice == "2":
        console.print("[bold red]>> Port Scanner Activated (Placeholder)[/bold red]")
    elif choice == "3":
        return
    else:
        console.print("[bold red]Invalid selection! Returning to tools menu.[/bold red]")

def settings_menu():
    console.print("\n[bold red]>> Settings (Placeholder)[/bold red]")
    console.input("[bold red]Press Enter to return to main menu.[/bold red]")

# Main Execution Loop
show_cover_art()
show_title()

while True:
    show_main_menu()
    choice = console.input("[bold red]Select an option: [/bold red]")

    if choice == "1":
        start_nyx()  # Start NYX
    elif choice == "2":
        tools_menu()
    elif choice == "3":
        settings_menu()
    elif choice == "4":
        console.print("[bold red]>> Exiting...[/bold red]")
        sys.exit()
    else:
        console.print("[bold red]Invalid selection! Try again.[/bold red]")









