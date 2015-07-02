#!/usr/bin/python

import logging
import pprint
from getuser import get_user


# Enable logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

def main():
    user = get_user('rohit.dureja@hodtmail.com')
    print user

if __name__=="__main__":
    main()