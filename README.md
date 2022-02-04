# mysql-via-pandas
Example of how one can use a Flask webapp to trigger various pandas-based scripts to obtain and export data from a mysql database using python and pandas.
For proper functionality, one should set up a proper webserver e.g. NGINX, rather than attempting to use Flask's own webserver.
Tested on Raspbian 10, with Python 3.7.3.


### Config & Credentials:
Ensure no # are present in variables, as any following characters will be treated as comments
Ensure no = are present in variables

Fresh copies of each .ini will be generated when run.py is run, if they are missing.


# Flask Secret
For Flask to function, a token is needed. The options are:
* Run 'run.py' without data/config.ini present to generate a secret;
* Use 'data/generate_secret.py' to generate a secret, then copy the generated token to the flask_secret parameter in 'data/config.ini'.
* Generate a secret in another way and enter it as the flask_secret parameter in 'data/config.ini'.

