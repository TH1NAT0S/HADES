import json
import time

CONFIG_FILE = "config.json"

def load_config():
    """Loads NYX's behavior settings from a file."""
    try:
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("[NYX] Config file missing! Using default settings.")
        return {"personality": "neutral", "mode": "basic", "logging": False}

def nyx_loop():
    """Main loop for NYX to interact with HADES."""
    config = load_config()
    print(f"[NYX] Running in {config['mode']} mode with a {config['personality']} personality.")
    
    while True:
        user_input = input("[NYX] > ")
        if user_input.lower() == "exit":
            print("[NYX] Shutting down...")
            break
        process_input(user_input)

def process_input(user_input):
    """Sends the input to executer.py for execution."""
    with open("executer.py", "w") as file:
        file.write(f'# Auto-generated command from NYX\nCOMMAND = "{user_input}"\n')
    print("[NYX] Command logged. Waiting for execution...")

if __name__ == "__main__":
    nyx_loop()
