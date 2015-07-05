#!/usr/bin/python
from treelib import Node, Tree

import httplib2
from apiclient import discovery, errors

import logging
import pprint
from getuser import get_user
 
# Node in directory structure
class node(object):
    def __init__(self, parentID, fileID, name, ntype):
        self.parentID = parentID
        self.fileID = fileID
        self.name = name
        self.ntype = ntype

# Enable logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
 
def main():
    credentials = get_user('rohit.dureja@gmail.com')
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
    
    # initialise directory structure
    directory = Tree()
    directory.create_node("Root", "root")
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            children = service.children().list(folderId='root', **param).execute()

            for child in children.get('items', []):
                #print 'File Id: %s' % child['id']
                try:
                    file__ = service.files().get(fileId=child['id']).execute()
                    #print 'Title: %s' % file__['title']
                    #print 'MIME type: %s' % file__['mimeType']
                    directory.create_node(file__['title'], child['id'], parent = 'root', data=node('root', child['id'], file__['title'], file__['mimeType']))
                except errors.HttpError, error:
                    print 'An error occurred: %s' % error
            
            page_token = children.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
            break
    
    directory.show()
    
#     results = service.files().list(maxResults=10, 'application/vnd.google-apps.folder').execute()
#     items = results.get('items', [])
#     if not items:
#         print 'No files found.'
#     else:
#         print 'Files:'
#         for item in items:
#             print '{0} ({1})'.format(item['title'], item['id'])

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