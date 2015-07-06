#!/usr/bin/python

import httplib2
from apiclient import discovery
import logging

from servicemenu import service_menu
from getuser import get_user

# Enable logging
FORMAT = '%(levelname)s: %(asctime)s %(filename)s %(funcName)s :: %(message)s'
logging.basicConfig(filename='termdrive.log',level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("runtime_log")
 
def main():
    # Get user credentials
    credentials = get_user('rohit.dureja@gmail.com')
    
    # Connect to Google Drive and establish a service connection
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
    
    # Call the main application loop
    service_menu(service)
        
# Main function
if __name__=="__main__":
    main()
