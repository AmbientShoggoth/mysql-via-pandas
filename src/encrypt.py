from os import path as os_path
from sys import exit as sys_exit
from cryptography.fernet import Fernet

def main():

    parent_dir=os_path.dirname(os_path.realpath(__file__)).split("mysql-via-pandas")[0]+"mysql-via-pandas/"

    try:
        with open(f"{parent_dir}credentials.ini","r") as f:raw_cred=f.read().encode()
    except FileNotFoundError:
        print("credentials1.ini missing")
        sys_exit(1)

    key=Fernet.generate_key()
    fernet=Fernet(key)


    with open(f"{parent_dir}/key.txt","wb") as f:f.write(key)
    print("Key in 'key.txt'. Keep your key safe!")
    fried_cred=fernet.encrypt(raw_cred)
    with open(f"{parent_dir}/data/safe_credentials.dat","wb") as f:raw_cred=f.write(fried_cred)

if __name__ == '__main__':main()