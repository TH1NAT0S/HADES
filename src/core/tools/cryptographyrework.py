import os
import hashlib
import base64
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

console = Console()

def show_title():
    ascii_banner = pyfiglet.figlet_format("HADES", font="Bloody")
    console.print(f"[bold red]{ascii_banner}[/bold red]")

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 32-byte encryption key from a password."""
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def encrypt_aes(data: bytes, key: bytes) -> bytes:
    """Encrypt data using AES-CBC."""
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = data + b' ' * (16 - len(data) % 16)  # Simple padding
    return iv + encryptor.update(padded_data) + encryptor.finalize()

def decrypt_aes(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypt AES-CBC encrypted data."""
    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data[16:]).rstrip()

def encrypt_chacha(data: bytes, key: bytes) -> bytes:
    """Encrypt data using ChaCha20."""
    nonce = os.urandom(16)
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return nonce + encryptor.update(data) + encryptor.finalize()

def decrypt_chacha(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypt ChaCha20 encrypted data."""
    nonce = encrypted_data[:16]
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data[16:])

def multi_stage_encrypt(data: str, passphrase1: str, passphrase2: str) -> str:
    """Encrypt data with AES first, then ChaCha20."""
    salt = os.urandom(16)
    key1 = derive_key(passphrase1, salt)
    key2 = derive_key(passphrase2, salt)
    aes_encrypted = encrypt_aes(data.encode(), key1)
    chacha_encrypted = encrypt_chacha(aes_encrypted, key2)
    return base64.b64encode(salt + chacha_encrypted).decode()

def multi_stage_decrypt(encrypted_data: str, passphrase1: str, passphrase2: str) -> str:
    """Decrypt data that was encrypted with multi-stage encryption."""
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    salt = encrypted_data_bytes[:16]
    key1 = derive_key(passphrase1, salt)
    key2 = derive_key(passphrase2, salt)
    chacha_decrypted = decrypt_chacha(encrypted_data_bytes[16:], key2)
    aes_decrypted = decrypt_aes(chacha_decrypted, key1)
    return aes_decrypted.decode()

def main_menu():
    """Simple TUI for encryption and decryption"""
    show_title()

    while True:
        console.print("\n[bold green]Select an option:[/bold green]")
        console.print("[1] Encrypt a message")
        console.print("[2] Decrypt a message")
        console.print("[3] Exit")

        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3"])

        if choice == "1":
            message = Prompt.ask("\nEnter the message to encrypt")
            pass1 = Prompt.ask("Enter passphrase 1", password=True)
            pass2 = Prompt.ask("Enter passphrase 2", password=True)
            
            encrypted = multi_stage_encrypt(message, pass1, pass2)
            console.print(f"\n[bold cyan]Encrypted Message:[/bold cyan] {encrypted}")

        elif choice == "2":
            encrypted_message = Prompt.ask("\nEnter the encrypted message")
            pass1 = Prompt.ask("Enter passphrase 1", password=True)
            pass2 = Prompt.ask("Enter passphrase 2", password=True)

            try:
                decrypted = multi_stage_decrypt(encrypted_message, pass1, pass2)
                console.print(f"\n[bold yellow]Decrypted Message:[/bold yellow] {decrypted}")
            except Exception as e:
                console.print("\n[bold red]Decryption failed![/bold red] Check your passphrases.")
            

        elif choice == "3":
            console.print("\n[bold magenta]Goodbye![/bold magenta]")
            break

if __name__ == "__main__":
    main_menu()
