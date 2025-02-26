import os
import curses
import psutil
import time
import tmuxp
from rich.console import Console
from rich.progress import track
from rich.text import Text
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from ascii_graph import Pyasciigraph

console = Console()

def system_status(stdscr):
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

def create_tmux_session():
    os.system("tmux new-session -d -s HADES")
    os.system("tmux split-window -h -t HADES")
    os.system("tmux split-window -v -t HADES")
    os.system("tmux select-layout tiled")
    os.system("tmux send-keys -t HADES:0.0 'python3 system_monitor.py' C-m")
    os.system("tmux send-keys -t HADES:0.1 'python3 network_monitor.py' C-m")
    os.system("tmux send-keys -t HADES:0.2 'python3 ai_interface.py' C-m")
    os.system("tmux attach-session -t HADES")

def hacking_animation():
    for _ in track(range(10), description="Executing Command..."):
        time.sleep(0.5)

def nyx_ai():
    console.print("[bold red]Nyx:[/bold red] Initializing AI...")
    time.sleep(1)
    console.print("[bold green]Nyx:[/bold green] System secure. Awaiting command.")

if __name__ == "__main__":
    create_tmux_session()
