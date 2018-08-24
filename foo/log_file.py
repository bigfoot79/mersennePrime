# detect mersenne prime numbers (test code only)
# Written by Vince, started 19/04/2018

# version 1.0       19/04/2018   Vincent      Initial program code
# version 1.1       01/06/2018   Vincent      Adding log to file system
#                                             Separate py into modules/package

# import declarations
import datetime
import os

def get_timestamp():
    # Create a logging system, as a means of debugging and evaluating code efficiency.
    # generate a date stamp that is consistent
    # ASH: google datetime format ???

    str_now = datetime.datetime.now()
    str_date = str(str_now.year)
    if (str_now.month < 10):
        str_date = str_date + "-0" + str(str_now.month)
    else:
        str_date = str_date + "-" + str(str_now.month)
    if (str_now.day < 10):
        str_date = str_date + "-0" + str(str_now.day)
    else:
        str_date = str_date + "-" + str(str_now.day)
    if (str_now.hour < 10):
        str_date = str_date + "-0" + str(str_now.hour)
    else:
        str_date = str_date + "-" + str(str_now.hour)
    if (str_now.minute < 10):
        str_date = str_date + ":0" + str(str_now.minute)
    else:
        str_date = str_date + ":" + str(str_now.minute)
    if (str_now.second < 10):
        str_date = str_date + ":0" + str(str_now.second)
    else:
        str_date = str_date + ":" + str(str_now.second)

    return str_date


def log_file_create():
    fName = "log_system.log"
    with open(fName,"w") as f:
        # Add file header
        str_message = get_timestamp() + "     New file created"
        f.write(str_message + "\n")
        # Add username
        str_message = get_timestamp() + "     Created by user: <" + os.getenv("userName") + ">"
        f.write(str_message + "\n")
        # Add COMPUTERNAME
        str_message = get_timestamp() + "     Created on computer: <" + os.getenv("COMPUTERNAME") + ">"
        f.write(str_message + "\n\n")
        # Add data headers
        str_message = get_timestamp() + "     Prime                                    Mersenne Prime   Status                   "
        f.write(str_message + "\n")


def log_file_append(str_message):
    fName = "log_system.log"
    with open(fName,"a") as f:
        str_message = get_timestamp() + "     " + str_message
        f.write(str_message + "\n")


