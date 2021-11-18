from os import path as os_path,environ as os_environ
from sys import exit as sys_exit
from cryptography.fernet import Fernet,InvalidToken

def main(env_key_name=None):

    parent_dir=os_path.dirname(os_path.realpath(__file__)).split("mysql-via-pandas")[0]+"mysql-via-pandas/"
    
    try:
        with open(f"{parent_dir}/data/safe_credentials.dat","r") as f:fried_cred=f.read().encode()
    except FileNotFoundError:
        print("credentials.dat missing")
        return(False)
    
    if env_key_name:
        key=os_environ.get(env_key_name)
        if not key:
            print(f"No key found in environment variable: '{env_key_name}'")
            env_key_name=None
    
    if not env_key_name:key=input("Enter your encryption key: ")
    
    while True:
        try:
            fernet=Fernet(key)
            break
        except ValueError:
            print(f"Invalid encryption key")
            if env_key_name:input("Check your key in your environment variables. Try again?")
            else:key=input("Try entering your key again: ")
    
    
    
    try:raw_cred=fernet.decrypt(fried_cred)
    except InvalidToken as err:print(f"Invalid token: {err}")
    return(raw_cred.decode())

if __name__ == '__main__':main()