from directorytree import build_directory_tree, show_directory_contents
from uploads import upload_file

import logging
def service_menu(service):
    logger = logging.getLogger("runtime_log")
    logger.debug("service")
    
    current_dir = "root"
    try:
        while True:
            command = raw_input('>> ')
            command = command.split()
            
            # List current directory contents
            if(command[0] == "ls"):
                show_directory_contents(current_dir)
    
            # List available commands
            elif(command[0] == "help"):
                print "help"
            
            # Build directory structure
            elif(command[0] == "build"):
                build_directory_tree(service)
            
            # Download file from drive
            elif(command[0] == "download"):
                print "download"
                
            # Upload file to drive
            elif(command[0] == "upload"):
                upload_file(service, command, current_dir)
                
            # Quit application
            elif(command[0] == "quit"):
                break;
            
            else:
                # Invalid command
                print "'%s' is not a valid command. For a list of commands, type 'help'" % command[0]
                
    except KeyboardInterrupt:
        print "quit"
        