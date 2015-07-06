from apiclient import errors
from treelib import Tree
import pickle
from termcolor import colored

# Node in directory structure
class node(object):
    def __init__(self, parentID, fileID, name, ntype):
        self.parentID = parentID
        self.fileID = fileID
        self.name = name
        self.ntype = ntype
        
def build_directory_tree(service):
    print colored("*** Building directory tree ***", 'blue')
    
    # initialize a new directory structure
    directory = Tree()
    directory.create_node("Root", "root")
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            
            # Get children of folderID
            children = service.children().list(folderId='root', **param).execute()

            # For each child in folder, get ID, name and Type
            # and write to the directory tree
            for child in children.get('items', []):
                try:
                    file__ = service.files().get(fileId=child['id']).execute()
                    directory.create_node(file__['title'], child['id'], parent = 'root', data=node('root', child['id'], file__['title'], file__['mimeType']))
                except errors.HttpError, error:
                    print 'An error occurred: %s' % error
            
            # Get next page token for current folderID
            page_token = children.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError, error:
            print colored('An error occurred: %s', 'red') % error
            break
    
    print colored("*** Directory tree stored at %s ***", 'blue') % 'dump.txt'
    datafile = open('dump.txt', 'w')
    pickle.dump(directory, datafile)
    datafile.close()

def show_directory_contents(current_dir):
    datafile = open('dump.txt', 'r')
    #directory = Tree()
    directory = pickle.load(datafile)
    files = directory.is_branch(current_dir)
    for i in range(0, len(files)):
        print directory.get_node(files[i]).data.name
    #directory.show()
    
