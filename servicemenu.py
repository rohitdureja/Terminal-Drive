def service_menu(credentials):
    
    try:
        while True:
            command = raw_input('>> ')
            command = command.split()
            
            # List current directory contents
            if(command[0] == "ls"):
                print "ls"
                
            # List available commands
            if(command[0] == "help"):
                print "help"
            
            # Build directory structure
            if(command[0] == "build"):
                print "build"
            
            # Download file from drive
            if(command[0] == "download"):
                print "download"
                
            # Upload file to drive
            if(command[0] == "upload"):
                print "upload"
                
            # Quit application
            elif(command[0] == "quit"):
                print "quit"
                break;
            
            else:
                # Invalid command
                print "'%s' is not a valid command. For a list of commands, type 'help'" % command[0]
                
    except KeyboardInterrupt:
        print "quit"
        