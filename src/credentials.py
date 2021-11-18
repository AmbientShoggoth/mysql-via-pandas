from os import path as os_path
import os
from sys import argv,exit as sys_exit
from platform import system as get_system

def main():
    # get run.py directory
    parent_dir=os_path.dirname(os_path.realpath(__file__)).split("mysql-via-pandas")[0]+"mysql-via-pandas/"
    
    def config_error(err_info,err_code=1):
        input(f"\nThere's an issue with your config.ini: {err_info}\n")
        sys_exit(err_code)
    
    def config_type_string_to_dict(in_string):
        """Convert contents of ini files to dict"""
        string_list=in_string.split("\n")
        string_list=[i.split("#")[0].replace(" ","").split("=") for i in string_list if i and "=" in i]
        return({pair[0]:pair[1] for pair in string_list})
        
    # Read config file
    try:
        with open(f"{parent_dir}config.ini","r") as f:
            config_string=f.read()
    except FileNotFoundError:config_error("config.ini missing")
    config_dict=config_type_string_to_dict(config_string)
    
    if not config_dict:config_error("no valid content.")
    
    
    if os_path.isfile(f"{parent_dir}/data/safe_credentials.dat"):
        print("Attempting to use encrypted credentials.")
        import src.decrypt
        credentials_string=src.decrypt.main(config_dict["env_var_key_name"])
    else:
        try:
            with open(f"{parent_dir}credentials.ini","r") as f:
                credentials_string=f.read()
        except FileNotFoundError:
            input("Unable to find safe_credentials.dat or credentials.ini")
            sys_exit(2)
    
    credentials_dict=config_type_string_to_dict(credentials_string)
    global cred
    class cred:
        class sql:
            user=credentials_dict["sql_user"]
            password=credentials_dict["sql_user_password"]
            db_ip=credentials_dict["sql_db_ip"]
            db_port=credentials_dict["sql_db_port"]
            db_schema=credentials_dict["sql_db_schema"]
            
        class sp:
            if config_dict["enable_sharepoint_uploads"]=="1":
                enabled=True
                username=credentials_dict["sp_username"]
                app_password=credentials_dict["sp_app_password"]
                site_url=credentials_dict["sp_site_url"]
                full_url=site_url+credentials_dict["sp_start_path"]
            else:enabled=False
    return(cred)
    
if __name__ == '__main__':main()