from os import path as os_path
import os
from sys import argv,exit as sys_exit
from platform import system as get_system

def main():
    
    parent_dir=os_path.dirname(os_path.realpath(__file__)).split("mysql-via-pandas")[0]+"mysql-via-pandas/"
    
    def config_error(err_info,err_code=1):
        print(f"\nThere's an issue with your config.ini: {err_info}\n")
        sys_exit(err_code)

    def config_type_string_to_dict(in_string):
        string_list=in_string.split("\n")
        string_list=[i.split("#")[0].replace(" ","").split("=") for i in string_list if i and "=" in i]
        return({pair[0]:pair[1] for pair in string_list})
        

    # Read config file
    try:
        with open(f"{parent_dir}config.ini","r") as f:
            config_string=f.read()
    except FileNotFoundError:config_error("config.ini missing")
    
    # Filter out blank lines, comments, spaces, and convert to dict
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
            print("Unable to find safe_credentials.dat or credentials.ini")
        
    credentials_dict=config_type_string_to_dict(credentials_string)
    for i,j in credentials_dict.items():print(f"{i}: {j}")
    
    """
    try:env_vars_toggle=int(config_dict["use_env_vars"])
    except ValueError:
        print("env_vars_toggle should be either 1 or 0. Assuming 0")
        env_vars_toggle=False # 
    except KeyError:config_error("use_env_vars missing")""";
    
    
    
        
    #if int(config_dict["use_env_vars"]): # use env variables
        
    


    #os_path.dirname(os_path.realpath(__file__)) # py script directory
    
    """
    platform_string=get_system()
    if platform_string=="Windows":split_char=";" # windows
    else:split_char=":" # macos, linux""";

    print("Yes, indeed")
    
    
    
    """
    class cred:
        env_vars=os_environ.get("lvnvariables")
        username,app_password,user,host,port,schema,site_url,start_path=env_vars.split(";")
        URI=f"mysql://{user}@{host}:{port}/{schema}"
        full_url=site_url+start_path
        winuser=os_environ.get("username")
    """;
    """
    class cred:
        env_vars=os_environ.get("lvnvariables")
        username,app_password,user,host,port,schema,site_url,start_path=env_vars.split(";")
        URI=f"mysql://{user}@{host}:{port}/{schema}"
        full_url=site_url+start_path
        winuser=os_environ.get("username")

    elif system()=="Darwin":#macos
        class cred:
            lvnvars=os_environ.get("lvnvariables")
            username,app_password,user,host,port,schema,site_url,start_path=lvnvars.split(":")
            
            user=user.replace("£",":")
            site_url=site_url.replace("£",":")
            
            URI=f"mysql://{user}@{host}:{port}/{schema}"
            full_url=site_url+start_path
            #winuser=os_environ.get("username")
    """;
    
if __name__ == '__main__':main()