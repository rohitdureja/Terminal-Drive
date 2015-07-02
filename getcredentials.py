import os
import md5
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
SCOPES = [
          'https://www.googleapis.com/auth/drive',
          'email'
          ]
CLIENT_SECRET_FILE = 'json/client_secret.json'
APPLICATION_NAME = 'Terminal Drive'

# Get user credentials from file, or generates new if don't exist
# Returns the path to the credential file
def get_credential_file(email):
    # create md5 digest of email
    credential_file_name = md5.new(email).hexdigest()
    
    # create path to credentials directory and user credentials file
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, credential_file_name)
 
    # Retrieve the credential file if its exists
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        # Generate new credentials
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credential_file_name

# returns the user credentials
def get_credentials(credential_file):
    
    print credential_file
    # create path to credentials directory and user credentials file
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, credential_file)
    
    # Retrieve the credential file if its exists
    store = Storage(credential_path)
    credentials = store.get()
    
    if credentials:
        return credentials
    else:
        return False