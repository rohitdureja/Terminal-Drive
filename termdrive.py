#!/usr/bin/python
 
import httplib2
from apiclient import discovery

import logging
import pprint
from getuser import get_user
 

# Enable logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
 
def main():
    credentials = get_user('rohit.dureja@gmail.com')
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
 
    results = service.files().list(maxResults=10).execute()
    items = results.get('items', [])
    if not items:
        print 'No files found.'
    else:
        print 'Files:'
        for item in items:
            print '{0} ({1})'.format(item['title'], item['id'])

if __name__=="__main__":
    main()

# def main():
#     """Shows basic usage of the Google Drive API.
# 
#     Creates a Google Drive API service object and outputs the names and IDs
#     for up to 10 files.
#     """
#     credentials = get_credentials()

# 
# if __name__ == '__main__':
#     main()