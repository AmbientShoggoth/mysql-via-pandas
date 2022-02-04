
def cred_setup():
    from src.core.config_read import config_type_string_to_dict
    
    cred_path="data/credentials.ini"
    config_path="data/config.ini"
    
    
    
    
    ## get credentials from file, parse with config_type_string_to_dict 
    try:
        with open(cred_path,"r") as f:cred_dict=config_type_string_to_dict(f.read())
    except FileNotFoundError as err:
        input(f"Unable to find {cred_path}.\n\n{err}")
    
    # helper function for checking for missing dict values
    def dict_check(diction):
        missing_indices=False
        for key,value in diction.items():
            if not value:
                missing_indices=True
                print(f"credentials.ini: '{key}' missing value.")
        return(missing_indices)
    
    # use helper function, exit if missing
    if dict_check(cred_dict):
        input(f"Parameters missing from {cred_path}: rectify, then retry.")
        from sys import exit
        exit()
    
    # class to hold various credentials
    class cred:
        username=cred_dict["sp_username"]
        app_password=cred_dict["sp_app_password"]
        site_url=cred_dict["sp_site_url"]
        start_path=cred_dict["sp_start_path"]
        user=f'{cred_dict["sql_user"]}:{cred_dict["sql_user_password"]}'
        host=cred_dict["sql_db_ip"]
        port=cred_dict["sql_db_port"]
        schema=cred_dict["sql_db_schema"]
        
        URI=f"mysql://{user}@{host}:{port}/{schema}"
        full_url=site_url+start_path
    
    ## get config variables from file, parse
    try:
        with open(config_path,"r") as f:config_dict=config_type_string_to_dict(f.read())
    except FileNotFoundError as err:
        input(f"Unable to find {config_path}.\n\n{err}")
    
    # Retrieve flask secret, and check for its existence: exit if missing.
    flask_secret_string="flask_secret"
    if not flask_secret_string in config_dict or not config_dict[flask_secret_string]:
        input(f"No {flask_secret_string} found in '{config_path}'.\nDelete config.ini and rerun this script to generate a new file and new flask secret;\nOR run data/generate_secret.py and copy the output secret into config.ini;\nOR create your own secret.")
        from sys import exit
        exit()
    else:
        flask_secret_key=config_dict[flask_secret_string]
    
    output_folder="./output"
    
    return(cred,flask_secret_key,output_folder)

cred,flask_secret_key,output_folder=cred_setup()
del cred_setup