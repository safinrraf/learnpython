#!/usr/bin/env python3.9

import logging
import os
import socket
import sys


SCRIPT_NAME="start.start.py"
LOG_FORMAT = '%(asctime)s %(host)s %(tag)s %(user)s %(message)s'


def log(message):
    additional_info={'user': os.getlogin(), 'host': socket.gethostname(), 'tag': SCRIPT_NAME}
    logging.info (message, extra=additional_info)


def main(argv):
    tuple = (1,"a",True, False, "Hello")
    log(tuple)
    log(tuple[0:3])


if __name__ == "__main__":
    logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
    print("Python version:", sys.version)

    main(sys.argv[1:])