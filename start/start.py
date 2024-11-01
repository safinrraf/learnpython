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
    tuple_var1 = (1, "a", True, False, "Hello")
    dic_var1 = {"Apple":10,"Mango":11,"Lichi":1234545678945678765567890}
    log(dic_var1)
    dic_var1["Banana"] = 1234
    log(dic_var1)
    dic_var1["Banana"] = "1"
    log(type(dic_var1["Banana"]))
    log(type(dic_var1["Apple"]))

if __name__ == "__main__":
    logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
    print("Python version:", sys.version)

    main(sys.argv[1:])