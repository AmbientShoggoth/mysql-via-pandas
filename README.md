# mysql-via-pandas
Example of how one can use pandas to obtain and present data from a mysql database using python and pandas.


### Config & Credentials:
Ensure no # are present in variables, as any following characters will be treated as comments
Ensure no = are present in variables

Fresh copies of each .ini can be found in the data folder.

# Encryption
Keep your credentials safe with some encryption by running run.py and selecting the 'Encrypt' option. This will generate an encrypted copy of credentials.ini inside the data folder, along with the encryption key in key.txt in the same folder. Credentials.ini can then be deleted, though it is recommended to test the encrypted version first.
You will be prompted for the encryption key each time you run a script requiring credentials, or can set the key as an environment variable and adjust 'env_var_key_name' in config.ini to match the variable name.
running encrypt.py and deleting credentials.ini

# Sharepoint
If sharepoint usage is disabled, scripts which include downloading of files from sharepoint will not run, however scripts which involve uploading of files to SharePoint will run without that functionality.
