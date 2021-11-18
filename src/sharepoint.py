from shareplum import Office365,site as sp_site,Site
import shareplum as sp

def init(cred_sp):
    """ Initiate module through creation of a shareplum.site._Site365 object. Requires site url, base directory url, username and password."""
    if cred_sp.enabled:
        authcookie = Office365(cred_sp.site_url, username=cred_sp.username, password=cred_sp.app_password).GetCookies()
        version=sp_site.Version.v365
        global site
        site = Site(dir_url, version=version, authcookie=authcookie)
    return(cred_sp.enabled)

def get_folder(end_path):
    """Returns shareplum.Site.Folder object using input path."""
    return(site.Folder(end_path))

def list_files(folder):
    """Returns list of the files in input folder."""
    return([file["Name"] for file in folder.files])
