# mysql-via-pandas
Example of how one can use a Flask webapp to trigger various pandas-based scripts to obtain and export data from a mysql database using python and pandas.
For proper functionality, one should set up a proper webserver e.g. NGINX, rather than attempting to use Flask's own webserver.
Tested on Raspbian 10, with Python 3.7.3.

Github: https://github.com/AmbientShoggoth/mysql-via-pandas

ToDo:
* Restore gui as alternative usage method
* Port over (and anonymize) some of my less basic scripts

# Usage Instructions:
* Download/clone repository
* Run 'run.py' for the first time, generating ./data/ 'credentials.ini','config.ini','users.csv'
* Enter sharepoint & MySQL details and credentials into 'credentials.ini'
* Replace auto-generated flask secret_key in config.ini if desired
* User './adduser.py' to add at least one user to users.csv - passwords use passlib.hash.pbkdf2_sha256 hashing.
* Run 'run.py', if no errors: visit localhost:3090, or local ip:3090 and see if it works.
* Adjust 'basic_example.py' to match your MySQL database and desired usage - adjust 'basic_example' route in 'run.py' as needed.
* Test 'basic_example.py'

One option for (more) proper deployment is to use a proper webserver e.g. NGINX rather than Flask's own webserver.
This link was useful for doing so on a Rasberry Pi 2: [Running Flask under NGINX on the Raspberry Pi](https://www.raspberrypi-spy.co.uk/2018/12/running-flask-under-nginx-raspberry-pi/)

### Config & Credentials:
* Ensure no # are present in variables, as any following characters will be treated as comments
* Ensure no = are present in variables
* Fresh copies of each .ini will be generated when run.py is run, if they are missing.


# Flask Secret
For Flask to function, a token is needed. The options are:
* Run 'run.py' without data/config.ini present to generate a secret;
* Use 'data/generate_secret.py' to generate a secret, then copy the generated token to the flask_secret parameter in 'data/config.ini'.
* Generate a secret in another way and enter it as the flask_secret parameter in 'data/config.ini'.

