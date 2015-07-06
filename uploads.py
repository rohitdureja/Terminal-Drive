from apiclient import errors
from apiclient.http import MediaFileUpload
from termcolor import colored

# Uploads a file in the current directory
def upload_file(service, command, current_dir):
    # Search if TermDrive folder exists
    folder_exists = False;
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            param['q'] = "title = 'TermDrive'"
            # Query for folder  
            folder = service.children().list(folderId=current_dir, **param).execute()
            if(folder['items'] == []): # folder doesn't exist
                folder_exists = False; # keep flag false
            else:
                folder_exists = True;
                folder = folder['items'][0]
                break;
            # Continue to search on next page
            page_token = folder.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
            break
    
    # if folder exists
    if(folder_exists == True):
        print colored('*** TermDrive folder found at %s/TermDrive ***', 'blue') % current_dir
    else: # create the folder
        print colored("*** TermDrive folder doesn't exist at %s/TermDrive ***", 'red') % current_dir
        body = {
                'title': 'TermDrive',
                'description': 'Folder to use with TermDrive application',
                'parents': current_dir,
                'mimeType': 'application/vnd.google-apps.folder'
                }
        try:
            folder = service.files().insert(body=body).execute()
            print colored('*** TermDrive folder created at %s/TermDrive ***', 'blue') % current_dir
        except errors.HttpError, error:
            print colored('An error occured: %s', 'red') % error
            print colored('Cannot create folder to use with TermDrive', 'red')
            return None

    # Upload the file passed as parameter to Drive
    try:
        media_body = MediaFileUpload(command[1], mimetype='text/plain', resumable=True)
    except IOError, e:
        print colored('An error occurred: %s', 'red') %e
        return
    # Configure file metadata
    body = {
            'title': 'Test Document',
            'description': 'A sample document',
            'parents': [{'id' : folder['id']}],
            'mimeType': 'text/plain'
            }
    try:
        # Upload the file
        upload_file = service.files().insert(body=body, media_body=media_body).execute()
        print colored('*** Success! File successfully uploaded to %s/TermDrive/%s', 'blue') % (current_dir, body['title'])
    except errors.HttpError, error:
        print colored('An error occurred: %s', 'red') % error
        