import flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired

from os import makedirs, chdir as os_chdir
from os.path import isdir as os_isdir, dirname as os_dirname, realpath as os_realpath
os_chdir(os_dirname(os_realpath(__file__)))

import logging
logging.basicConfig(filename="logging.log")

from csv import reader
from passlib.hash import pbkdf2_sha256 as hashing
from os.path import isfile

import flask_login
from urllib.parse import urlparse, urljoin

from sys import exit

import src.core.base_setup
config_status=src.core.base_setup.main()
if config_status:
    from sys import exit
    input(f"Config files have been generated. Ensure they are properly configured, then run again.")
    exit()

#import src here
import src.basic_example
#import src.

login_required=flask_login.login_required
redirect,request=flask.redirect,flask.request

class User(flask_login.UserMixin):# inherit from UserMixin
    def __init__(self, name, id, passhash):
        self.name=name
        self.id=id
        self.passhash=passhash

with open("./data/users.csv",newline="",encoding="utf-8-sig") as csvfile:
    USERS={int(uid):User(name,int(uid),passw) for uid,name,passw in reader(csvfile,delimiter=",")}
USER_NAMES = { u.name:u for u in USERS.values() }


class LoginForm(FlaskForm): # see login route
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class DateRangeForm(FlaskForm):
    startdate = DateField("Start Date",validators=[DataRequired()])
    enddate = DateField("End Date",validators=[DataRequired()])
    submit = SubmitField("Submit")

def is_safe_url(target): # make sure users are redirected to same host
    ref_url = urlparse(flask.request.host_url)
    test_url = urlparse( urljoin(flask.request.host_url,target) )
    return( test_url.scheme in ("http","https") and ref_url.netloc==test_url.netloc )

print("\n\n\n")


from src.core.credentials import flask_secret_key
app = flask.Flask(__name__) #
app.secret_key=flask_secret_key

# login section
login_manager=flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    #return(User.get(user_id))
    return(USERS.get(int(user_id)))


### Add sharepoint folder links here - for heading to output from /index without needing to run script
links_dict={
    "basic_example":"https://londonvillagenetwork.sharepoint.com/:f:/s/LVNKeyDocuments/EqHguCnT3J5DqlMmNqKqZskBNOLjwQFsi2l3hxfHMJZZYQ?e=FO3Pgx",
    #"":"placeholder",
}

@app.route("/")
@app.route("/index")
@login_required
def index():
    return(flask.render_template("index.html",**links_dict))

@app.route("/login", methods=["GET","POST"])
def login():
    # use wtforms-based login form to represent and validate client-side form data
    form = LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        if username in USER_NAMES and hashing.verify(form.password.data,USER_NAMES[username].passhash):
            remember=flask.request.form.get("remember", "no") == "yes"
            if flask_login.login_user(USER_NAMES[username], remember=remember):
                flask.flash("Logged in.")
                
                next = flask.request.args.get("next")
                if not is_safe_url(next):
                    return(flask.abort(400))
                return(redirect(next or flask.url_for("index")))
                
        flask.flash("Login Failed.")
        return( flask.render_template("login.html", form=form))
    return( flask.render_template("login.html", form=form))


@app.route("/logout")
@login_required
def logout():
    #remove username from session if it's there
    #flask.session.pop("username",None)
    flask_login.logout_user()
    flask.flash("Logged out.")
    return( redirect(flask.url_for("login")))


### Add routes for scripts here

@app.route("/basic_example")
@login_required
def basic_example():
    message_, success=src.basic_example.main()
    if success:template_string="basic_example.html"
    else:template_string="failure.html"
    return(flask.render_template(template_string,message=message_))   


###

@login_manager.unauthorized_handler
def unauthorized_callback():
    return( redirect(flask.url_for('login')+"?next="+request.path) )

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3090, debug=True)