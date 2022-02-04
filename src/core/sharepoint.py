from shareplum import Office365,site as sp_site,Site
import shareplum as sp

def init(site_url,dir_url,sp_username,app_password):
    """ Initiate module through creation of a shareplum.site._Site365 object. Requires site url, base directory url, username and password."""
    authcookie = Office365(site_url, username=sp_username, password=app_password).GetCookies()
    version=sp_site.Version.v365
    global site
    site = Site(dir_url, version=version, authcookie=authcookie)
    
def get_folder(end_path):
    """Returns shareplum.Site.Folder object using input path."""
    return(site.Folder(end_path))

def list_files(folder):
    """Returns list of the files in input folder."""
    return([file["Name"] for file in folder.files])

def get_file_url(folder_,filename_):
    #add error handling at some point
    for file in folder_.files:
        if file["Name"]==filename_:return(file["LinkingUrl"])
