import os
import sys
import time
import curses
import psutil
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text
from ascii_graph import Pyasciigraph
import pyfiglet

console = Console()

def show_cover_art():
    art = """
        (\__/)
        (o_o) 
        / \🩸
    """
    console.print(Panel.fit(f"[bold red]{art}[/bold red]", title="[bold red]WELCOME TO HADES[/bold red]"))

def show_title():
    ascii_banner = pyfiglet.figlet_format("HADES", font="Bloody")
    console.print(f"[bold red]{ascii_banner}[/bold red]")

def show_main_menu():
    console.print("\n[bold red][1] SYSTEM MONITOR[/bold red]")
    console.print("[bold red][2] STAND-ALONE TOOLS[/bold red]")
    console.print("[bold red][3] SETTINGS[/bold red]")
    console.print("[bold red][4] EXIT[/bold red]\n")

def system_monitor(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000)
    while True:
        stdscr.clear()
        cpu_usage = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        net = psutil.net_io_counters()

        stdscr.addstr(2, 2, f"CPU Usage: {cpu_usage}%")
        stdscr.addstr(3, 2, f"Memory Usage: {mem.percent}%")
        stdscr.addstr(4, 2, f"Network Sent: {net.bytes_sent / 1024:.2f} KB | Received: {net.bytes_recv / 1024:.2f} KB")
        stdscr.refresh()
        time.sleep(1)

def ascii_graph():
    data = [("CPU", psutil.cpu_percent()), ("RAM", psutil.virtual_memory().percent)]
    graph = Pyasciigraph()
    for line in graph.graph("System Usage", data):
        console.print(line)

def hacking_animation():
    for _ in track(range(10), description="Executing Command..."):
        time.sleep(0.5)

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

def create_tmux_session():
    os.system("tmux new-session -d -s HADES")
    os.system("tmux split-window -h")
    os.system("tmux split-window -v")
    os.system("tmux select-pane -t 0")
    os.system("tmux send-keys 'python3 system_monitor.py' C-m")
    os.system("tmux select-pane -t 1")
    os.system("tmux send-keys 'python3 network_monitor.py' C-m")
    os.system("tmux select-pane -t 2")
    os.system("tmux send-keys 'python3 extra_tool.py' C-m")
    os.system("tmux attach-session -t HADES")

# Main Execution Loop
show_cover_art()
show_title()

while True:
    show_main_menu()
    choice = console.input("[bold red]Select an option: [/bold red]")
    if choice == "1":
        curses.wrapper(system_monitor)
    elif choice == "2":
        tools_menu()
    elif choice == "3":
        settings_menu()
    elif choice == "4":
        console.print("[bold red]>> Exiting...[/bold red]")
        sys.exit()
    else:
        console.print("[bold red]Invalid selection! Try again.[/bold red]")









