from os.path import exists
from shutil import copy2

def main():
    """Tests if config files exists, and creates them if not. Returns None if all files exist."""
    file_dict={
        "data/credentials.ini":"data/fresh/credentials.ini",
        "data/config.ini":"data/fresh/config.ini",
        "data/users.csv":"data/fresh/users.csv",
        }
    
    copy_tracker=[]
    for destination,freshfile in file_dict.items():
        if not exists(destination):
            copy2(freshfile,destination)
            copy_tracker.append(destination)
            print(f"Generated {destination}")
    if not copy_tracker:return() # return if no changes made
    #Otherwise:
    
    # generate secret for config.ini: for flask's use
    if "data/config.ini" in copy_tracker:
        from secrets import token_hex
        with open("data/config.ini","r") as f:
            config_string=f.read()
        secret=token_hex(16)
        config_string=config_string.replace("flask_secret=",f"flask_secret={secret}")
        with open("data/config.ini","w") as f:
            f.write(config_string)
        print(f"Generated token for Flask: located in data/config.ini, replace if desired.")
    
    if "data/users.csv" in copy_tracker:
        print("Use adduser.py to add new users.")
    
    return(copy_tracker)
    

if __name__=="__main__":main()